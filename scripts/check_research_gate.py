#!/usr/bin/env python3
"""MP Research Gate.

Fail-closed validator for implementation-like changes.

Rules:
- unknown implementation locations are protected by default,
- every protected file in the current diff must be listed exactly in a build
  request that is itself added/modified in the same diff,
- build requests bind to one component, a pinned research record, and a
  versioned human authorization source,
- narrow repairs may reuse an accepted research record; major changes still
  require a fresh per-change build request.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_RESEARCH_DECISIONS = {"USE", "ADAPT", "BUILD"}
ALLOWED_INTEGRATION_ROLES = {
    "DEPENDENCY",
    "COMPONENT",
    "REFERENCE_IMPLEMENTATION",
    "BENCHMARK",
    "REJECTED",
}
ALLOWED_SEARCH_STATUS = {"DONE", "NO_RESULT"}
ALLOWED_CHANGE_KINDS = {"MAJOR", "NARROW_REPAIR"}

PROTECTED_PREFIXES = (
    "src/",
    "app/",
    "pipeline/",
    "components/",
    "models/",
    "adapters/",
)

EXEMPT_EXACT = {
    "scripts/check_research_gate.py",
    "tests/test_research_gate.py",
    ".github/workflows/research-gate.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/CODEOWNERS",
    "AGENTS.md",
}

GOVERNANCE_DATA_PREFIXES = (
    "research/",
    "governance/",
    "audits/",
    "evidence/",
    "experiments/",
    "docs/",
)

GOVERNANCE_DATA_SUFFIXES = {
    ".json",
    ".yaml",
    ".yml",
    ".csv",
    ".tsv",
}

DRAFT_CONTRACT_SUFFIXES = {
    ".json",
    ".yaml",
    ".yml",
    ".md",
}

SAFE_METADATA_EXACT = {
    "README.md",
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    ".gitignore",
    ".gitattributes",
    ".editorconfig",
}

SAFE_NON_IMPLEMENTATION_SUFFIXES = {
    ".md",
    ".rst",
    ".txt",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
}

EXECUTABLE_OR_CODE_SUFFIXES = {
    ".py",
    ".pyi",
    ".js",
    ".mjs",
    ".cjs",
    ".ts",
    ".tsx",
    ".jsx",
    ".go",
    ".rs",
    ".java",
    ".kt",
    ".kts",
    ".c",
    ".cc",
    ".cpp",
    ".cxx",
    ".h",
    ".hh",
    ".hpp",
    ".cs",
    ".rb",
    ".php",
    ".swift",
    ".scala",
    ".sh",
    ".bash",
    ".zsh",
    ".fish",
    ".ps1",
    ".bat",
    ".cmd",
    ".ipynb",
    ".sql",
    ".proto",
}

DEPENDENCY_EXACT = {
    "pyproject.toml",
    "poetry.lock",
    "uv.lock",
    "Pipfile",
    "Pipfile.lock",
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "environment.yml",
    "environment.yaml",
    "docker-compose.yml",
    "docker-compose.yaml",
    "Cargo.toml",
    "Cargo.lock",
    "go.mod",
    "go.sum",
}

BUILD_REQUEST_PREFIX = "governance/build_requests/"
BUILD_REQUEST_TEMPLATE = "governance/build_requests/TEMPLATE.json"
RESEARCH_PREFIX = "research/records/"
RESEARCH_TEMPLATE = "research/records/TEMPLATE.json"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def changed_files(base: str, head: str) -> list[str]:
    out = git("diff", "--name-only", f"{base}...{head}")
    return [line.strip() for line in out.splitlines() if line.strip()]


def changed_name_status(base: str, head: str) -> dict[str, str]:
    out = git("diff", "--name-status", f"{base}...{head}")
    result: dict[str, str] = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        path = parts[-1]
        result[path] = status
    return result


def normalize_repo_path(path: str) -> str:
    normalized = str(PurePosixPath(path))
    if normalized.startswith("../") or normalized.startswith("/"):
        raise ValueError(f"path escapes repository: {path}")
    return normalized


def is_protected(path: str) -> bool:
    """Fail closed for implementation-like files outside known layout."""
    path = normalize_repo_path(path)
    p = PurePosixPath(path)
    name = p.name
    lower = name.lower()
    suffix = p.suffix.lower()

    if path in EXEMPT_EXACT or path in SAFE_METADATA_EXACT:
        return False

    # Dependency/runtime manifests are protected by function, regardless of
    # directory. They must be classified before documentation/data exemptions.
    if name in DEPENDENCY_EXACT:
        return True
    if lower.startswith("requirements") and lower.endswith(".txt"):
        return True
    if lower.startswith("dockerfile"):
        return True

    # Contract drafts are exempt only when they are design/data artifacts in
    # explicitly allowed formats. A file such as contracts/adapter.draft.py
    # remains executable code and is protected.
    if path.startswith("contracts/"):
        is_design_draft = ".draft." in name and suffix in DRAFT_CONTRACT_SUFFIXES
        return not is_design_draft

    if path.startswith(PROTECTED_PREFIXES):
        if path.startswith("adapters/") and lower == "readme.md":
            return False
        return True

    # Executable/code content is protected before generic data-directory
    # exemptions so code cannot hide under docs/, governance/, research/, etc.
    if suffix in EXECUTABLE_OR_CODE_SUFFIXES:
        return True

    if path.startswith(GOVERNANCE_DATA_PREFIXES):
        if suffix in SAFE_NON_IMPLEMENTATION_SUFFIXES or suffix in GOVERNANCE_DATA_SUFFIXES:
            return False
        # Unknown artifact under governance/research remains protected.

    if suffix in SAFE_NON_IMPLEMENTATION_SUFFIXES:
        return False

    return True


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: top-level JSON must be an object")
    return data


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_nonempty_text_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and len(value) > 0
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def is_iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_search(block: object, label: str, errors: list[str]) -> None:
    if not isinstance(block, dict):
        errors.append(f"{label}: missing search object")
        return

    status = block.get("status")
    if status not in ALLOWED_SEARCH_STATUS:
        errors.append(f"{label}.status must be DONE or NO_RESULT")

    if not is_iso_date(block.get("date")):
        errors.append(f"{label}.date must be a real ISO date YYYY-MM-DD")

    if not is_nonempty_text_list(block.get("queries")):
        errors.append(f"{label}.queries must contain at least one non-empty query")

    candidates = block.get("candidates")
    if not isinstance(candidates, list) or not all(
        isinstance(item, str) and bool(item.strip()) for item in candidates
    ):
        errors.append(f"{label}.candidates must be a list of non-empty strings")
    elif status == "DONE" and len(candidates) == 0:
        errors.append(
            f"{label}: status DONE requires at least one candidate; "
            "use NO_RESULT when the search produced no viable candidates"
        )
    elif status == "NO_RESULT" and len(candidates) != 0:
        errors.append(f"{label}: status NO_RESULT requires candidates=[]")


def validate_research_record(path: Path) -> tuple[dict | None, list[str]]:
    errors: list[str] = []
    try:
        data = load_json(path)
    except ValueError as exc:
        return None, [str(exc)]

    if not isinstance(data.get("record_version"), int) or data.get("record_version", 0) < 1:
        errors.append(f"{path.relative_to(ROOT)}: record_version must be integer >= 1")

    required_text = (
        "component_id",
        "problem",
        "comparison_summary",
        "integration_role",
        "decision",
        "replaces_what",
        "why",
        "review_status",
        "human_decision",
    )
    for key in required_text:
        if not is_nonempty_text(data.get(key)):
            errors.append(f"{path.relative_to(ROOT)}: {key} is required and must be non-empty")

    validate_search(data.get("vertical_search"), "vertical_search", errors)
    validate_search(data.get("horizontal_search"), "horizontal_search", errors)

    role = data.get("integration_role")
    if role not in ALLOWED_INTEGRATION_ROLES:
        errors.append(
            f"{path.relative_to(ROOT)}: integration_role must be one of "
            f"{sorted(ALLOWED_INTEGRATION_ROLES)}"
        )

    decision = data.get("decision")
    if decision not in ALLOWED_RESEARCH_DECISIONS:
        errors.append(
            f"{path.relative_to(ROOT)}: decision must be USE, ADAPT or BUILD "
            "to authorize implementation"
        )

    if decision == "BUILD" and not is_nonempty_text(data.get("build_justification")):
        errors.append(
            f"{path.relative_to(ROOT)}: BUILD requires build_justification "
            "explaining why USE/ADAPT candidates were insufficient"
        )

    inspected = data.get("inspected_candidates")
    if not isinstance(inspected, list) or not all(
        isinstance(item, str) and bool(item.strip()) for item in inspected
    ):
        errors.append(
            f"{path.relative_to(ROOT)}: inspected_candidates must be a list of non-empty strings"
        )

    found_candidates: list[str] = []
    for key in ("vertical_search", "horizontal_search"):
        block = data.get(key)
        if isinstance(block, dict) and isinstance(block.get("candidates"), list):
            found_candidates.extend(block.get("candidates") or [])

    if found_candidates and (not isinstance(inspected, list) or len(inspected) == 0):
        errors.append(
            f"{path.relative_to(ROOT)}: candidates were found, but inspected_candidates is empty"
        )

    if data.get("review_status") != "PASS":
        errors.append(f"{path.relative_to(ROOT)}: review_status must be PASS")

    if data.get("human_decision") != "ACCEPTED":
        errors.append(f"{path.relative_to(ROOT)}: human_decision must be ACCEPTED")

    validate_authorization(
        data.get("human_acceptance"),
        f"{path.relative_to(ROOT)}.human_acceptance",
        errors,
    )

    return data, errors


def validate_authorization(auth: object, label: str, errors: list[str]) -> None:
    if not isinstance(auth, dict):
        errors.append(f"{label}: authorization object is required")
        return

    for key in ("decision_id", "source", "subject_version"):
        if not is_nonempty_text(auth.get(key)):
            errors.append(f"{label}.{key} is required and must be non-empty")

    if not isinstance(auth.get("state_version"), int) or auth.get("state_version", 0) < 1:
        errors.append(f"{label}.state_version must be integer >= 1")


def validate_build_request(
    path: Path,
    changed_status: dict[str, str],
) -> tuple[dict | None, list[str]]:
    errors: list[str] = []
    try:
        data = load_json(path)
    except ValueError as exc:
        return None, [str(exc)]

    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    if rel not in changed_status:
        errors.append(
            f"{rel}: build request must be added or modified in the current diff; "
            "historical requests cannot authorize new code changes"
        )

    for key in (
        "change_id",
        "change_kind",
        "component_id",
        "description",
        "research_record",
        "research_record_sha256",
        "authorized_decision",
        "review_status",
        "human_decision",
    ):
        if not is_nonempty_text(data.get(key)):
            errors.append(f"{rel}: {key} is required and must be non-empty")

    if data.get("change_kind") not in ALLOWED_CHANGE_KINDS:
        errors.append(f"{rel}: change_kind must be MAJOR or NARROW_REPAIR")

    files = data.get("authorized_files")
    if not is_nonempty_text_list(files):
        errors.append(
            f"{rel}: authorized_files must be a non-empty list of exact repository paths"
        )
        files = []
    else:
        normalized: list[str] = []
        for item in files:
            try:
                n = normalize_repo_path(item)
            except ValueError as exc:
                errors.append(f"{rel}: {exc}")
                continue
            if any(char in n for char in "*?[]"):
                errors.append(
                    f"{rel}: authorized_files must use exact paths, not globs: {item}"
                )
            normalized.append(n)
        if len(set(normalized)) != len(normalized):
            errors.append(f"{rel}: authorized_files contains duplicates")

    if data.get("review_status") != "PASS":
        errors.append(f"{rel}: review_status must be PASS")

    if data.get("human_decision") != "ACCEPTED":
        errors.append(f"{rel}: human_decision must be ACCEPTED")

    validate_authorization(data.get("authorization"), f"{rel}.authorization", errors)

    research_rel = str(data.get("research_record", ""))
    research_path = ROOT / research_rel
    research = None
    if not research_rel:
        pass
    elif not research_rel.startswith(RESEARCH_PREFIX) or research_rel == RESEARCH_TEMPLATE:
        errors.append(
            f"{rel}: research_record must point to a non-template file under {RESEARCH_PREFIX}"
        )
    elif not research_path.is_file():
        errors.append(f"{rel}: research_record does not exist: {research_rel}")
    else:
        research, research_errors = validate_research_record(research_path)
        errors.extend(research_errors)

        expected_hash = str(data.get("research_record_sha256", ""))
        actual_hash = sha256_file(research_path)
        if expected_hash != actual_hash:
            errors.append(
                f"{rel}: research_record_sha256 mismatch; expected {expected_hash!r}, "
                f"actual {actual_hash}"
            )

    if research:
        if data.get("component_id") != research.get("component_id"):
            errors.append(
                f"{rel}: component_id {data.get('component_id')!r} does not match "
                f"research component_id {research.get('component_id')!r}"
            )
        if data.get("authorized_decision") != research.get("decision"):
            errors.append(
                f"{rel}: authorized_decision {data.get('authorized_decision')!r} "
                f"does not match research decision {research.get('decision')!r}"
            )

    if data.get("change_kind") == "NARROW_REPAIR" and not is_nonempty_text(
        data.get("repair_of")
    ):
        errors.append(f"{rel}: NARROW_REPAIR requires non-empty repair_of")

    return data, errors


def main() -> int:
    if len(sys.argv) >= 3:
        base, head = sys.argv[1], sys.argv[2]
    else:
        base = os.environ.get("BASE_SHA", "")
        head = os.environ.get("HEAD_SHA", "HEAD")

    if not base:
        print(
            "Research Gate configuration error: BASE_SHA/base commit is required.",
            file=sys.stderr,
        )
        return 2

    files = changed_files(base, head)
    status = changed_name_status(base, head)
    protected = [p for p in files if is_protected(p)]

    print("MP Research Gate")
    print(f"Base: {base}")
    print(f"Head: {head}")
    print(f"Changed files: {len(files)}")
    print(f"Protected implementation-like files: {len(protected)}")

    if not protected:
        print("PASS: no protected implementation changes in this diff.")
        return 0

    changed_request_paths = sorted(
        ROOT / p
        for p in files
        if p.startswith(BUILD_REQUEST_PREFIX)
        and p.endswith(".json")
        and p != BUILD_REQUEST_TEMPLATE
    )

    if not changed_request_paths:
        print(
            "FAIL: protected implementation changes exist but no build request "
            "was added/modified in this diff.",
            file=sys.stderr,
        )
        for path in protected:
            print(f"  - {path}", file=sys.stderr)
        return 1

    valid_requests: list[tuple[Path, dict]] = []
    all_errors: list[str] = []

    for path in changed_request_paths:
        data, errors = validate_build_request(path, status)
        if errors:
            all_errors.extend(errors)
        elif data:
            valid_requests.append((path, data))

    uncovered: list[str] = []
    duplicate_coverage: list[str] = []
    coverage: dict[str, str] = {}

    for changed in protected:
        matches: list[str] = []
        for req_path, req in valid_requests:
            if changed in req.get("authorized_files", []):
                matches.append(
                    str(req_path.relative_to(ROOT)).replace("\\", "/")
                )
        if len(matches) == 1:
            coverage[changed] = matches[0]
        elif len(matches) == 0:
            uncovered.append(changed)
        else:
            duplicate_coverage.append(f"{changed} <- {matches}")

    if all_errors:
        print("Research/build record validation errors:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)

    if uncovered:
        print(
            "Protected files not explicitly authorized by a current build request:",
            file=sys.stderr,
        )
        for path in uncovered:
            print(f"  - {path}", file=sys.stderr)

    if duplicate_coverage:
        print(
            "Protected files authorized by more than one build request:",
            file=sys.stderr,
        )
        for item in duplicate_coverage:
            print(f"  - {item}", file=sys.stderr)

    if all_errors or uncovered or duplicate_coverage:
        print("FAIL: MP Research Gate is not satisfied.", file=sys.stderr)
        return 1

    print("Coverage:")
    for path, request in coverage.items():
        print(f"  - {path} <- {request}")

    print(
        "PASS: every protected implementation change is explicitly bound to a "
        "current, accepted Research Gate authorization."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
