"""Dokumentasjonstester for PROMPT 024 sin snapshot- og testsporbarhet."""

import ast
from pathlib import Path
import re
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
MAIN_SHA = "444135e946b5635c812a24d44037c80fbf815e45"
PROMPT_023_SHA = "89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503"
SNAPSHOT_TEST_FILES = {
    MAIN_SHA: ("tests/test_generator.py",),
    PROMPT_023_SHA: ("tests/test_generator.py", "tests/test_app.py"),
}


def section(text, heading):
    """Return one heading section, stopping at the next heading of same depth."""
    match = re.search(rf"(?m)^(##+ )(?P<title>[^\n]*{re.escape(heading)}[^\n]*)$", text)
    if not match:
        raise AssertionError(f"Fant ikke Markdown-seksjonen: {heading}")
    depth = len(match.group(1))
    rest = text[match.end() :]
    end = re.search(rf"(?m)^#{{1,{depth}}} \S", rest)
    return rest[: end.start()] if end else rest


def markdown_table(text, required_headers):
    """Parse the first Markdown table with the requested header columns."""
    lines = text.splitlines()
    for index, line in enumerate(lines[:-1]):
        if not line.lstrip().startswith("|") or not lines[index + 1].lstrip().startswith("|"):
            continue
        headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not set(required_headers).issubset(headers):
            continue
        separator = lines[index + 1]
        if not re.fullmatch(r"\|?[\s:|-]+\|?", separator.strip()):
            continue
        rows = []
        for row_line in lines[index + 2 :]:
            if not row_line.lstrip().startswith("|"):
                break
            cells = [cell.strip() for cell in row_line.strip().strip("|").split("|")]
            if len(cells) == len(headers):
                rows.append(dict(zip(headers, cells)))
        return rows
    raise AssertionError(f"Fant ikke Markdown-tabell med kolonnene {required_headers}")


def assert_snapshot_evidence(test_plan, test_log):
    main_section = section(test_plan, "Dekning på `main`")
    feature_section = section(test_plan, "Dekning på PROMPT 023-snapshotet")
    assert MAIN_SHA in main_section
    assert PROMPT_023_SHA not in main_section
    main_link = (
        f"[`tests/test_generator.py` på main-snapshotet]"
        f"(https://github.com/IBE160-2026/G27-isum-vijai/blob/{MAIN_SHA}/tests/test_generator.py)"
    )
    assert main_link in main_section
    assert "Dette snapshotet har seks pytest/unittest-tester." in main_section
    assert f"Snapshot: `{PROMPT_023_SHA}`" in feature_section
    generator_link = (
        f"[`tests/test_generator.py` (11 tester)]"
        f"(https://github.com/IBE160-2026/G27-isum-vijai/blob/{PROMPT_023_SHA}/tests/test_generator.py)"
    )
    app_link = (
        f"[`tests/test_app.py` (4 tester)]"
        f"(https://github.com/IBE160-2026/G27-isum-vijai/blob/{PROMPT_023_SHA}/tests/test_app.py)"
    )
    assert generator_link in feature_section
    assert app_link in feature_section

    prompt_log = section(test_log, "Automatisk regresjonskjøring – PROMPT 023")
    assert "15 passed" in prompt_log
    assert "før commitopprettelsen" in prompt_log
    assert PROMPT_023_SHA in prompt_log
    assert "ikke et testresultat på `main`" in prompt_log


def git_snapshot_function_names(snapshot, paths):
    """Read test definitions from existing local Git objects without checkout/network."""
    names = set()
    for path in paths:
        result = subprocess.run(
            ["git", "show", f"{snapshot}:{path}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise AssertionError(
                f"Kan ikke lese nødvendig lokalt Git-objekt {snapshot}:{path}; "
                "hent ikke automatisk fra nettverk og kopier ikke kildefiler."
            )
        try:
            tree = ast.parse(result.stdout, filename=f"{snapshot}:{path}")
        except SyntaxError as exc:
            raise AssertionError(f"Ugyldig Python-kilde i {snapshot}:{path}: {exc}") from exc
        names.update(
            node.name
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        )
    return names


def assert_documented_test_references_exist(test_plan):
    for heading, snapshot in (
        ("Dekning på `main`", MAIN_SHA),
        ("Dekning på PROMPT 023-snapshotet", PROMPT_023_SHA),
    ):
        rows = markdown_table(
            section(test_plan, heading),
            {"ID", "Konkrete bevis og mangler"},
        )
        source_names = {
            path: git_snapshot_function_names(snapshot, (path,))
            for path in SNAPSHOT_TEST_FILES[snapshot]
        }
        for row in rows:
            evidence = row["Konkrete bevis og mangler"]
            explicit = list(
                re.finditer(
                    r"(?P<path>tests/test_(?:generator|app)\.py)::(?P<name>test_[A-Za-z0-9_]+)",
                    evidence,
                )
            )
            for reference in explicit:
                path, name = reference.group("path"), reference.group("name")
                assert path in source_names, (
                    f"Testplanen viser til {path}, som ikke finnes i snapshot {snapshot}"
                )
                assert name in source_names[path], (
                    f"Testplanen knytter {name} til {path}, men funksjonen finnes "
                    f"ikke i denne testfila ved {snapshot}"
                )

            explicit_spans = [(match.start(), match.end()) for match in explicit]
            names = [
                match
                for match in re.finditer(
                    r"(?<![\w./])(?:GeneratorTests\.)?(test_[A-Za-z0-9_]+)\b", evidence
                )
                if not any(start <= match.start() < end for start, end in explicit_spans)
            ]
            file_mentions = [
                match
                for match in re.finditer(r"tests/test_(?:generator|app)\.py", evidence)
                if not any(start <= match.start() < end for start, end in explicit_spans)
            ]
            for name_match in names:
                name = name_match.group(1)
                if not file_mentions:
                    matches = [path for path, definitions in source_names.items() if name in definitions]
                    assert len(matches) == 1, (
                        f"Testplanen viser til {name} i {len(matches)} testfiler ved {snapshot}; "
                        "forventet nøyaktig én fil"
                    )
                    continue

                # A trailing `i tests/test_*.py` identifies the function just
                # before it; otherwise use the nearest file mention in the row.
                following_in = [
                    path
                    for path in file_mentions
                    if path.start() > name_match.end()
                    and re.fullmatch(r"\s*`?\s*i\s*`?", evidence[name_match.end() : path.start()])
                ]
                path_match = following_in[0] if following_in else min(
                    file_mentions,
                    key=lambda path: min(
                        abs(path.start() - name_match.start()),
                        abs(path.end() - name_match.start()),
                    ),
                )
                path = path_match.group(0)
                assert name in source_names[path], (
                    f"Testplanen knytter {name} til {path}, men funksjonen finnes "
                    f"ikke i denne testfila ved {snapshot}"
                )


def assert_partial_rows_are_planned(test_plan):
    for heading in ("Dekning på `main`", "Dekning på PROMPT 023-snapshotet"):
        rows = markdown_table(
            section(test_plan, heading),
            {"ID", "Implementasjon", "Dekning", "Samlet teststatus"},
        )
        ids = [row["ID"] for row in rows]
        assert len(rows) == 9
        assert len(ids) == len(set(ids))
        by_id = {row["ID"]: row for row in rows}
        assert set(by_id) == {f"T-{number:03d}" for number in range(1, 10)}
        for row in rows:
            assert row["Implementasjon"]
            assert row["Dekning"] in {"Full", "Delvis", "Ingen"}
            assert row["Samlet teststatus"] == "PLANLAGT"
            if row["Dekning"] in {"Delvis", "Ingen"}:
                assert row["Samlet teststatus"] != "BESTÅTT"


def assert_prompt023_quiz_requirements_are_unimplemented(test_plan):
    rows = markdown_table(
        section(test_plan, "Dekning på PROMPT 023-snapshotet"),
        {"ID", "Implementasjon", "Dekning", "Samlet teststatus"},
    )
    by_id = {row["ID"]: row for row in rows}
    for test_id in ("T-004", "T-007"):
        assert by_id[test_id]["Implementasjon"] == "Ikke implementert"
        assert by_id[test_id]["Dekning"] == "Ingen"


def assert_no_manual_claim_for_apptest(test_log):
    prompt_log = section(test_log, "Automatisk regresjonskjøring – PROMPT 023")
    automatic = re.search(r"(?m)^- \*\*Miljø og testdata:\*\*(.*(?:\n(?!- \*\*).*)*)", prompt_log)
    assert automatic and "AppTest" in automatic.group(1)
    manual = re.search(r"(?m)^- \*\*Manuelle kontroller:\*\*\s*(.+)$", prompt_log)
    assert manual and re.search(r"ikke registrert", manual.group(1), re.IGNORECASE)
    assert "AppTest er automatisert UI-test" in prompt_log


class Prompt024TraceabilityDocsTests(unittest.TestCase):
    def setUp(self):
        self.test_plan = (ROOT / "docs/testing/TEST_PLAN.md").read_text(encoding="utf-8")
        self.test_log = (ROOT / "docs/testing/TEST_LOG.md").read_text(encoding="utf-8")

    def test_feature_023_evidence_stays_attributed_to_its_snapshot(self):
        assert_snapshot_evidence(self.test_plan, self.test_log)
        assert_documented_test_references_exist(self.test_plan)

        changed = self.test_plan.replace(
            f"Snapshot: `{PROMPT_023_SHA}`",
            f"Snapshot: `{MAIN_SHA}`",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_snapshot_evidence(changed, self.test_log)

        changed_count = self.test_plan.replace("(11 tester)", "(10 tester)", 1)
        with self.assertRaises(AssertionError):
            assert_snapshot_evidence(changed_count, self.test_log)

        changed_main_count = self.test_plan.replace(
            "Dette snapshotet har seks pytest/unittest-tester.",
            "Dette snapshotet har sju pytest/unittest-tester.",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_snapshot_evidence(changed_main_count, self.test_log)

        changed_main_link = self.test_plan.replace(
            f"blob/{MAIN_SHA}/tests/test_generator.py",
            f"blob/{PROMPT_023_SHA}/tests/test_generator.py",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_snapshot_evidence(changed_main_link, self.test_log)

        changed_link = self.test_plan.replace(
            f"blob/{PROMPT_023_SHA}/tests/test_app.py",
            f"blob/{MAIN_SHA}/tests/test_app.py",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_snapshot_evidence(changed_link, self.test_log)

        mixed_main = self.test_plan.replace(
            f"Snapshot: `{MAIN_SHA}`.",
            f"Snapshot: `{MAIN_SHA}` og `{PROMPT_023_SHA}`.",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_snapshot_evidence(mixed_main, self.test_log)

        changed_log = self.test_log.replace("før commitopprettelsen", "etter commitopprettelsen", 1)
        with self.assertRaises(AssertionError):
            assert_snapshot_evidence(self.test_plan, changed_log)

        fake_reference = self.test_plan.replace(
            "test_valid_text_returns_local_content_and_demo_quiz",
            "test_function_that_does_not_exist",
            1,
        )
        with self.assertRaisesRegex(AssertionError, "test_function_that_does_not_exist"):
            assert_documented_test_references_exist(fake_reference)

        wrong_file_reference = self.test_plan.replace(
            "tests/test_app.py::test_results_show_local_sources_and_demo_quiz_label",
            "tests/test_generator.py::test_results_show_local_sources_and_demo_quiz_label",
            1,
        )
        with self.assertRaisesRegex(AssertionError, "test_results_show_local_sources_and_demo_quiz_label"):
            assert_documented_test_references_exist(wrong_file_reference)

        wrong_unqualified_file = self.test_plan.replace(
            "`tests/test_generator.py` og `test_empty_input_shows_validation_error_in_ui`",
            "`tests/test_app.py` og `test_empty_input_shows_validation_error_in_ui`",
            1,
        )
        with self.assertRaisesRegex(AssertionError, "test_empty_text_is_rejected"):
            assert_documented_test_references_exist(wrong_unqualified_file)

        with self.assertRaisesRegex(AssertionError, "Kan ikke lese nødvendig lokalt Git-objekt"):
            git_snapshot_function_names("0" * 40, ("tests/test_generator.py",))

    def test_partial_coverage_remains_planned(self):
        assert_partial_rows_are_planned(self.test_plan)
        assert_prompt023_quiz_requirements_are_unimplemented(self.test_plan)

        changed = self.test_plan.replace("| T-002 | Implementert | Delvis | PLANLAGT |", "| T-002 | Implementert | Delvis | BESTÅTT |", 1)
        with self.assertRaises(AssertionError):
            assert_partial_rows_are_planned(changed)

        combined = self.test_plan.replace("| ID | Implementasjon | Dekning | Samlet teststatus |", "| ID | Implementasjon | Dekning / samlet teststatus | Samlet teststatus |", 1)
        with self.assertRaises(AssertionError):
            assert_partial_rows_are_planned(combined)

        main_heading = "## Dekning på `main`"
        feature_heading = "## Dekning på PROMPT 023-snapshotet"
        before_main, main_rest = self.test_plan.split(main_heading, 1)
        main_table, after_main = main_rest.split(feature_heading, 1)
        duplicate_row = next(line for line in main_table.splitlines() if line.startswith("| T-002 |"))
        duplicated_row_plan = (
            before_main + main_heading + main_table.replace(duplicate_row, f"{duplicate_row}\n{duplicate_row}", 1)
            + feature_heading + after_main
        )
        with self.assertRaises(AssertionError):
            assert_partial_rows_are_planned(duplicated_row_plan)

        feature_heading = "## Dekning på PROMPT 023-snapshotet"
        main_part, feature_part = self.test_plan.split(feature_heading, 1)
        marked_demo_as_generated = main_part + feature_heading + feature_part.replace(
            "| T-004 | Ikke implementert | Ingen | PLANLAGT |",
            "| T-004 | Implementert | Delvis | PLANLAGT |",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_prompt023_quiz_requirements_are_unimplemented(marked_demo_as_generated)

        main_part, feature_part = self.test_plan.split(feature_heading, 1)
        marked_citations_as_implemented = main_part + feature_heading + feature_part.replace(
            "| T-007 | Ikke implementert | Ingen | PLANLAGT |",
            "| T-007 | Implementert | Delvis | PLANLAGT |",
            1,
        )
        with self.assertRaises(AssertionError):
            assert_prompt023_quiz_requirements_are_unimplemented(marked_citations_as_implemented)

    def test_missing_manual_evidence_is_not_recast_as_apptest(self):
        assert_no_manual_claim_for_apptest(self.test_log)

        changed = self.test_log.replace("AppTest er automatisert UI-test", "AppTest er manuell kontroll", 1)
        with self.assertRaises(AssertionError):
            assert_no_manual_claim_for_apptest(changed)

        changed = self.test_log.replace("Ikke registrert. AppTest", "Gjennomført. AppTest", 1)
        with self.assertRaises(AssertionError):
            assert_no_manual_claim_for_apptest(changed)

        changed = self.test_log.replace("Ikke registrert. AppTest", "Ikke kjørt. AppTest", 1)
        with self.assertRaises(AssertionError):
            assert_no_manual_claim_for_apptest(changed)


if __name__ == "__main__":
    unittest.main()
