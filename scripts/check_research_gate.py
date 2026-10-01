#!/usr/bin/env python3
"""MP Research Gate.

Blocks protected implementation changes unless they are covered by an accepted
research record and build request.

Stdlib only: intended to run in GitHub Actions without extra dependencies.
"""

from __future__ import annotations

import fnmatch
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_RESEARCH_DECISIONS = {"USE", "ADAPT", "BUILD"}
ALLOWED_SEARCH_STATUS = {"DONE", "NO_RESULT"}

PROTECTED_PREFIXES = (
    "src/",
    "app/",
    "pipeline/",
    "components/",
    "models/",
)

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
}

def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()

def changed_files(base: str, head: str) -> list[str]:
    out = git("diff", "--name-only", f"{base}...{head}")
    return [line.strip() for line in out.splitlines() if line.strip()]

def is_protected(path: str) -> bool:
    if path.startswith(PROTECTED_PREFIXES):
        return True

    if path.startswith("adapters/"):
        return Path(path).name.lower() != "readme.md"

    if path.startswith("contracts/"):
        # Explicit drafts are design material, not an accepted implementation contract.
        return ".draft." not in Path(path).name

    name = Path(path).name
    lower = name.lower()

    if name in DEPENDENCY_EXACT:
        return True
    if lower.startswith("requirements") and lower.endswith(".txt"):
        return True
    if lower.startswith("dockerfile"):
        return True

    return False

def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc

def nonempty_list(value) -> bool:
    return isinstance(value, list) and len(value) > 0

def validate_search(block: object, label: str, errors: list[str]) -> None:
    if not isinstance(block, dict):
        errors.append(f"{label}: missing search object")
        return

    status = block.get("status")
    if status not in ALLOWED_SEARCH_STATUS:
        errors.append(f"{label}.status must be DONE or NO_RESULT")

    if not str(block.get("date", "")).strip():
        errors.append(f"{label}.date is required")

    if not nonempty_list(block.get("queries")):
        errors.append(f"{label}.queries must contain at least one recorded query")

    candidates = block.get("candidates")
    if not isinstance(candidates, list):
        errors.append(f"{label}.candidates must be a list")
    elif status == "DONE" and len(candidates) == 0:
        errors.append(
            f"{label}: status DONE requires at least one candidate; "
            "use NO_RESULT when the search produced no viable candidates"
        )

def validate_research_record(path: Path) -> tuple[dict | None, list[str]]:
    errors: list[str] = []
    try:
        data = load_json(path)
    except ValueError as exc:
        return None, [str(exc)]

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
        if not str(data.get(key, "")).strip():
            errors.append(f"{path.relative_to(ROOT)}: {key} is required")

    validate_search(data.get("vertical_search"), "vertical_search", errors)
    validate_search(data.get("horizontal_search"), "horizontal_search", errors)

    decision = data.get("decision")
    if decision not in ALLOWED_RESEARCH_DECISIONS:
        errors.append(
            f"{path.relative_to(ROOT)}: decision must be USE, ADAPT or BUILD "
            "to authorize implementation"
        )

    if decision == "BUILD" and not str(data.get("build_justification", "")).strip():
        errors.append(
            f"{path.relative_to(ROOT)}: BUILD requires build_justification "
            "explaining why USE/ADAPT candidates were insufficient"
        )

    found_candidates = []
    for key in ("vertical_search", "horizontal_search"):
        block = data.get(key)
        if isinstance(block, dict):
            found_candidates.extend(block.get("candidates") or [])

    if found_candidates and not nonempty_list(data.get("inspected_candidates")):
        errors.append(
            f"{path.relative_to(ROOT)}: candidates were found, but inspected_candidates is empty"
        )

    if data.get("review_status") != "PASS":
        errors.append(f"{path.relative_to(ROOT)}: review_status must be PASS")

    if data.get("human_decision") != "ACCEPTED":
        errors.append(f"{path.relative_to(ROOT)}: human_decision must be ACCEPTED")

    return data, errors

def validate_build_request(path: Path) -> tuple[dict | None, list[str]]:
    errors: list[str] = []
    try:
        data = load_json(path)
    except ValueError as exc:
        return None, [str(exc)]

    for key in ("change_id", "description", "research_record", "authorized_decision"):
        if not str(data.get(key, "")).strip():
            errors.append(f"{path.relative_to(ROOT)}: {key} is required")

    scopes = data.get("scope")
    if not nonempty_list(scopes) or not all(isinstance(x, str) and x.strip() for x in scopes):
        errors.append(f"{path.relative_to(ROOT)}: scope must be a non-empty list of globs")

    if data.get("review_status") != "PASS":
        errors.append(f"{path.relative_to(ROOT)}: review_status must be PASS")

    if data.get("human_decision") != "ACCEPTED":
        errors.append(f"{path.relative_to(ROOT)}: human_decision must be ACCEPTED")

    research_rel = str(data.get("research_record", ""))
    research_path = ROOT / research_rel
    research = None
    if not research_rel:
        pass
    elif not research_path.is_file():
        errors.append(f"{path.relative_to(ROOT)}: research_record does not exist: {research_rel}")
    else:
        research, research_errors = validate_research_record(research_path)
        errors.extend(research_errors)

    if research:
        if data.get("authorized_decision") != research.get("decision"):
            errors.append(
                f"{path.relative_to(ROOT)}: authorized_decision "
                f"{data.get('authorized_decision')!r} does not match research decision "
                f"{research.get('decision')!r}"
            )

    return data, errors

def main() -> int:
    if len(sys.argv) >= 3:
        base, head = sys.argv[1], sys.argv[2]
    else:
        base = os.environ.get("BASE_SHA", "")
        head = os.environ.get("HEAD_SHA", "HEAD")

    if not base:
        print("Research Gate configuration error: BASE_SHA/base commit is required.", file=sys.stderr)
        return 2

    files = changed_files(base, head)
    protected = [p for p in files if is_protected(p)]

    print("MP Research Gate")
    print(f"Base: {base}")
    print(f"Head: {head}")
    print(f"Changed files: {len(files)}")
    print(f"Protected implementation-like files: {len(protected)}")

    if not protected:
        print("PASS: no protected implementation changes in this diff.")
        return 0

    requests_dir = ROOT / "governance" / "build_requests"
    request_paths = sorted(
        p for p in requests_dir.glob("*.json")
        if p.name != "TEMPLATE.json"
    )

    if not request_paths:
        print(
            "FAIL: protected implementation changes exist but no build request records exist.",
            file=sys.stderr,
        )
        for path in protected:
            print(f"  - {path}", file=sys.stderr)
        return 1

    valid_requests: list[tuple[Path, dict]] = []
    all_errors: list[str] = []

    for path in request_paths:
        data, errors = validate_build_request(path)
        if errors:
            all_errors.extend(errors)
        elif data:
            valid_requests.append((path, data))

    uncovered: list[str] = []
    coverage: dict[str, str] = {}

    for changed in protected:
        matched = None
        for req_path, req in valid_requests:
            if any(fnmatch.fnmatch(changed, pattern) for pattern in req["scope"]):
                matched = str(req_path.relative_to(ROOT))
                break
        if matched:
            coverage[changed] = matched
        else:
            uncovered.append(changed)

    if all_errors:
        print("Research/build record validation errors:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)

    if uncovered:
        print("Protected files not covered by an accepted build request:", file=sys.stderr)
        for path in uncovered:
            print(f"  - {path}", file=sys.stderr)

    if all_errors or uncovered:
        print("FAIL: MP Research Gate is not satisfied.", file=sys.stderr)
        return 1

    print("Coverage:")
    for path, request in coverage.items():
        print(f"  - {path} <- {request}")

    print("PASS: every protected implementation change is covered by an accepted Research Gate record.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
