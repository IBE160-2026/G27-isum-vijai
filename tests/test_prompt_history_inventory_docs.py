"""Kontroller append-only nummerering og gapmerking i promptarkivet."""

import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_prompt_inventory_preserves_expected_ids_and_unresolved_gap():
    prompt_log = (ROOT / "docs/CODEX_PROMPT_LOG.md").read_text(encoding="utf-8")
    gap_register = (ROOT / "docs/prompts/PROMPT_HISTORY_GAPS.md").read_text(encoding="utf-8")

    heading_ids = [int(number) for number in re.findall(r"(?m)^## PROMPT (\d{3})(?:\s|$)", prompt_log)]
    heading_counts = Counter(heading_ids)
    assert list(dict.fromkeys(heading_ids)) == [*range(1, 27), 28]
    expected_counts = {number: 1 for number in range(1, 27)}
    # PROMPT 023 has three archived stages, and PROMPT 028 has two; both
    # repetitions are explicitly documented as historical, not new IDs.
    expected_counts.update({23: 3, 28: 2})
    for number, expected_count in expected_counts.items():
        assert heading_counts[number] == expected_count
    assert 27 not in heading_counts
    assert "PROMPT 027 mangler" in gap_register
    assert "uavklart nummereringshull" in gap_register
    reconstruction_marker = "Original prompttekst ikke gjenfunnet – rekonstruert sammendrag."
    reconstructed_activities = (
        "PR #3-integrasjon og dokumentasjon i PDF-branchen",
        "MVP-001 PDF-implementering, review og integrasjon",
        "MVP Sprint 002 Gemini-implementering og valg",
        "Gemini Secrets, første manuelle feil, testisolering og exception-diagnostikk",
    )
    for activity in reconstructed_activities:
        rows = [line for line in gap_register.splitlines() if line.startswith("|") and activity in line]
        assert len(rows) == 1
        assert reconstruction_marker in rows[0]


def test_decision_003_approves_only_restricted_prototype_use():
    decision_log = (ROOT / "docs/decisions/DECISION_LOG.md").read_text(encoding="utf-8")
    decision_003 = decision_log.split("### [DEC-003]", 1)[1].split("### [DEC-004]", 1)[0]
    assert "**Dato:** 2026-11-16." in decision_003
    assert "A. Godkjent prototypebruk" in decision_003
    assert "syntetiske, offentlig tilgjengelige eller anonymiserte notater" in decision_003
    assert "B. Ikke-godkjent produksjonsbruk" in decision_003
    assert "Produksjonsbruk med personopplysninger er ikke godkjent" in decision_003
    assert "C. Krever ny beslutning" in decision_003
    assert "juridisk, institusjonell eller formell gruppe-/emnegodkjenning" in decision_003
    assert "Ingen juridisk eller institusjonell godkjenning" not in decision_003
    assert "Gjeldende leverandørvilkår og eventuelle emnekrav må følges" in decision_003
    assert "Det loves ikke gratis bruk, lagringstid eller sletting" in decision_003
