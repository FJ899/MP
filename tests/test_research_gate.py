#!/usr/bin/env python3

import hashlib
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = REPO_ROOT / "scripts" / "check_research_gate.py"

spec = importlib.util.spec_from_file_location("mp_gate", GATE_PATH)
gate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gate)


def run(*args, cwd: Path, check=True):
    return subprocess.run(
        list(args),
        cwd=cwd,
        text=True,
        capture_output=True,
        check=check,
    )


class GateClassificationTests(unittest.TestCase):
    def test_unknown_code_locations_are_protected(self):
        self.assertTrue(gate.is_protected("main.py"))
        self.assertTrue(gate.is_protected("tools/new_detector.py"))
        self.assertTrue(gate.is_protected("src/new_detector.py"))
        self.assertTrue(gate.is_protected("governance/evil.py"))
        self.assertTrue(gate.is_protected("contracts/candidate_event.schema.json"))

    def test_documentation_and_explicit_draft_are_not_protected(self):
        self.assertFalse(gate.is_protected("README.md"))
        self.assertFalse(gate.is_protected("research/REPO_RADAR.md"))
        self.assertFalse(gate.is_protected("contracts/candidate_event.schema.draft.json"))

    def test_invalid_search_and_role_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "research" / "records").mkdir(parents=True)
            record = {
                "record_version": 1,
                "component_id": "detector",
                "problem": "Choose detector",
                "vertical_search": {
                    "date": "YYYY-MM-DD",
                    "status": "DONE",
                    "queries": [""],
                    "candidates": ["a"],
                },
                "horizontal_search": {
                    "date": "2026-10-01",
                    "status": "DONE",
                    "queries": ["facade detector"],
                    "candidates": ["b"],
                },
                "inspected_candidates": ["a", "b"],
                "comparison_summary": "Compared",
                "integration_role": "INVALID_ROLE",
                "decision": "ADAPT",
                "replaces_what": "custom detector",
                "why": "evidence",
                "build_justification": "",
                "review_status": "PASS",
                "human_decision": "ACCEPTED",
                "human_acceptance": {
                    "decision_id": "H-1",
                    "source": "HUMAN_PROJECT_DECISION",
                    "state_version": 4,
                    "subject_version": "review-1",
                },
            }
            path = root / "research" / "records" / "detector.json"
            path.write_text(json.dumps(record), encoding="utf-8")

            old_root = gate.ROOT
            gate.ROOT = root
            try:
                _, errors = gate.validate_research_record(path)
            finally:
                gate.ROOT = old_root

            joined = "\n".join(errors)
            self.assertIn("real ISO date", joined)
            self.assertIn("non-empty query", joined)
            self.assertIn("integration_role", joined)

    def test_invalid_calendar_date_and_search_status_consistency(self):
        errors = []
        gate.validate_search(
            {
                "date": "2026-02-30",
                "status": "DONE",
                "queries": ["quality gate"],
                "candidates": [],
            },
            "bad_done",
            errors,
        )
        gate.validate_search(
            {
                "date": "2026-10-01",
                "status": "NO_RESULT",
                "queries": ["quality gate"],
                "candidates": ["unexpected/repo"],
            },
            "bad_no_result",
            errors,
        )
        joined = "\n".join(errors)
        self.assertIn("real ISO date", joined)
        self.assertIn("DONE requires at least one candidate", joined)
        self.assertIn("NO_RESULT requires candidates=[]", joined)


class GateEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        run("git", "init", "-q", cwd=self.root)
        run("git", "config", "user.email", "test@example.com", cwd=self.root)
        run("git", "config", "user.name", "Test", cwd=self.root)

        (self.root / "scripts").mkdir()
        (self.root / "research" / "records").mkdir(parents=True)
        (self.root / "governance" / "build_requests").mkdir(parents=True)
        (self.root / "src").mkdir()

        shutil.copy2(GATE_PATH, self.root / "scripts" / "check_research_gate.py")

        self.record = {
            "record_version": 1,
            "component_id": "detector",
            "problem": "Choose detector",
            "vertical_search": {
                "date": "2026-10-01",
                "status": "DONE",
                "queries": ["uav inspection"],
                "candidates": ["vertical/a"],
            },
            "horizontal_search": {
                "date": "2026-10-01",
                "status": "DONE",
                "queries": ["facade detector"],
                "candidates": ["horizontal/b"],
            },
            "inspected_candidates": ["vertical/a", "horizontal/b"],
            "comparison_summary": "Compared candidates",
            "integration_role": "COMPONENT",
            "decision": "ADAPT",
            "replaces_what": "custom detector",
            "why": "candidate fits",
            "build_justification": "",
            "review_status": "PASS",
            "human_decision": "ACCEPTED",
            "human_acceptance": {
                "decision_id": "H-RESEARCH-1",
                "source": "HUMAN_PROJECT_DECISION",
                "state_version": 4,
                "subject_version": "research-review-1",
            },
        }

        self.record_path = self.root / "research" / "records" / "detector.json"
        self.record_path.write_text(json.dumps(self.record, indent=2), encoding="utf-8")
        record_hash = hashlib.sha256(self.record_path.read_bytes()).hexdigest()

        old_request = {
            "change_id": "OLD",
            "change_kind": "MAJOR",
            "component_id": "detector",
            "description": "Old accepted implementation",
            "repair_of": "",
            "authorized_files": ["src/existing.py"],
            "research_record": "research/records/detector.json",
            "research_record_sha256": record_hash,
            "authorized_decision": "ADAPT",
            "authorization": {
                "decision_id": "H-OLD",
                "source": "HUMAN_PROJECT_DECISION",
                "state_version": 4,
                "subject_version": "old-subject",
            },
            "review_status": "PASS",
            "human_decision": "ACCEPTED",
        }
        (self.root / "governance" / "build_requests" / "old.json").write_text(
            json.dumps(old_request, indent=2),
            encoding="utf-8",
        )
        (self.root / "src" / "existing.py").write_text("print(1)\n", encoding="utf-8")

        run("git", "add", ".", cwd=self.root)
        run("git", "commit", "-qm", "base", cwd=self.root)
        self.base = run("git", "rev-parse", "HEAD", cwd=self.root).stdout.strip()

    def tearDown(self):
        self.tmp.cleanup()

    def gate(self, base, head):
        return run(
            "python",
            "scripts/check_research_gate.py",
            base,
            head,
            cwd=self.root,
            check=False,
        )

    def test_historical_request_cannot_cover_new_model_file(self):
        (self.root / "src" / "new_model_family.py").write_text(
            "print(2)\n", encoding="utf-8"
        )
        run("git", "add", "src/new_model_family.py", cwd=self.root)
        run("git", "commit", "-qm", "new model without fresh request", cwd=self.root)
        head = run("git", "rev-parse", "HEAD", cwd=self.root).stdout.strip()

        result = self.gate(self.base, head)
        self.assertEqual(result.returncode, 1)
        self.assertIn("no build request was added/modified", result.stderr)

    def test_narrow_repair_reuses_research_but_requires_fresh_build_request(self):
        (self.root / "src" / "existing.py").write_text("print(10)\n", encoding="utf-8")
        record_hash = hashlib.sha256(self.record_path.read_bytes()).hexdigest()
        request = {
            "change_id": "REPAIR-001",
            "change_kind": "NARROW_REPAIR",
            "component_id": "detector",
            "description": "Fix existing detector adapter bug",
            "repair_of": "BUG-17",
            "authorized_files": ["src/existing.py"],
            "research_record": "research/records/detector.json",
            "research_record_sha256": record_hash,
            "authorized_decision": "ADAPT",
            "authorization": {
                "decision_id": "H-REPAIR-001",
                "source": "HUMAN_REPAIR_DECISION",
                "state_version": 4,
                "subject_version": "repair-review-001",
            },
            "review_status": "PASS",
            "human_decision": "ACCEPTED",
        }
        request_path = self.root / "governance" / "build_requests" / "repair-001.json"
        request_path.write_text(json.dumps(request, indent=2), encoding="utf-8")

        run(
            "git",
            "add",
            "src/existing.py",
            "governance/build_requests/repair-001.json",
            cwd=self.root,
        )
        run("git", "commit", "-qm", "narrow repair", cwd=self.root)
        head = run("git", "rev-parse", "HEAD", cwd=self.root).stdout.strip()

        result = self.gate(self.base, head)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("PASS:", result.stdout)

    def test_unknown_root_code_is_blocked(self):
        (self.root / "main.py").write_text("print(3)\n", encoding="utf-8")
        run("git", "add", "main.py", cwd=self.root)
        run("git", "commit", "-qm", "unknown root implementation", cwd=self.root)
        head = run("git", "rev-parse", "HEAD", cwd=self.root).stdout.strip()

        result = self.gate(self.base, head)
        self.assertEqual(result.returncode, 1)
        self.assertIn("main.py", result.stderr)

    def test_glob_authorization_is_rejected(self):
        (self.root / "src" / "existing.py").write_text("print(11)\n", encoding="utf-8")
        record_hash = hashlib.sha256(self.record_path.read_bytes()).hexdigest()
        request = {
            "change_id": "BAD-GLOB",
            "change_kind": "MAJOR",
            "component_id": "detector",
            "description": "Bad broad authorization",
            "repair_of": "",
            "authorized_files": ["src/**"],
            "research_record": "research/records/detector.json",
            "research_record_sha256": record_hash,
            "authorized_decision": "ADAPT",
            "authorization": {
                "decision_id": "H-GLOB",
                "source": "HUMAN_PROJECT_DECISION",
                "state_version": 4,
                "subject_version": "glob-review",
            },
            "review_status": "PASS",
            "human_decision": "ACCEPTED",
        }
        request_path = self.root / "governance" / "build_requests" / "bad-glob.json"
        request_path.write_text(json.dumps(request, indent=2), encoding="utf-8")

        run(
            "git",
            "add",
            "src/existing.py",
            "governance/build_requests/bad-glob.json",
            cwd=self.root,
        )
        run("git", "commit", "-qm", "bad glob request", cwd=self.root)
        head = run("git", "rev-parse", "HEAD", cwd=self.root).stdout.strip()

        result = self.gate(self.base, head)
        self.assertEqual(result.returncode, 1)
        self.assertIn("exact paths, not globs", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
