# Sluttrevisjon – plan og kilder

**Dato:** 2026-11-16. **Branch:** `chore/ibe160-final-quality-audit`. **Base:** `origin/main` ved `fef77e85f078b6e5ecdb82f09a903b8a6a1d4fc1`.

## Metode og omfang

Kontrollen er retrospektiv og evidensbasert. Den sammenholder brief/tilbakemelding, README, beslutninger, BMAD-spesifikasjoner, kildekode, pytest-tester og Git-status. Kode/Docs undersøkes i separat worktree. Tester skal bruke syntetiske data og mocks. Ingen eksterne Gemini-forespørsler utføres.

## Tilgjengelige kilder

- Offisiell IBE160-emnebeskrivelse for Høst 2026: [emnebeskrivelsen](https://www.himolde.no/studier/emner/log/2026/host/ibe160.html). Den beskriver mappeinnlevering med prosjektkode/funksjonalitet og dokumentasjon av KI-bruk/kvalitetssikring (70 %) samt refleksjonsrapport (30 %).
- Product brief: [`../../product-brief.md`](../../product-brief.md); faglærervurdering: [`../../tilbakemelding-product-brief.md`](../../tilbakemelding-product-brief.md), datert 2026-10-06 og knyttet til brief-snapshot `dc2a630`.
- README: [`../../README.md`](../../README.md); testplan/-logg: [`../testing/TEST_PLAN.md`](../testing/TEST_PLAN.md), [`../testing/TEST_LOG.md`](../testing/TEST_LOG.md).
- Beslutninger/BMAD: [`../decisions/DECISION_LOG.md`](../decisions/DECISION_LOG.md), [`../bmad/WORKFLOW_STATUS.md`](../bmad/WORKFLOW_STATUS.md), `_bmad-output/implementation-artifacts/` og PRD-utkastet [`prd.md`](../../_bmad-output/planning-artifacts/prds/prd-G27-isum-vijai-2026-10-23/prd.md), med review-rubric og PRD-tilbakemelding i samme mappe.
- Kode: `app.py`, `prototype/`, `tests/`; syntetiske cases i [`../../testdata/synthetic_cases.json`](../../testdata/synthetic_cases.json).
- Promptarkiv: [`../CODEX_PROMPT_LOG.md`](../CODEX_PROMPT_LOG.md), [`../prompts/`](../prompts/), [`../prompts/PROMPT_HISTORY_GAPS.md`](../prompts/PROMPT_HISTORY_GAPS.md).

## Manglende kilder

Repoet inneholder ikke den fullstendige oppgaveteksten eller sensorveiledningen for gruppeinnleveringen. Offisiell emnebeskrivelse bekrefter eksamensformen, gruppevis refleksjonsrapport og rapporttemaer, men ikke konkret gruppespesifikasjon, detaljrubrikk, format, omfang eller leveringssted. Den tilgjengelige lokale lærerkilden er avgrenset feedback på product brief, i tillegg til separat PRD-tilbakemelding. Et BMAD-PRD finnes i `_bmad-output/planning-artifacts/prds/prd-G27-isum-vijai-2026-10-23/`; det er uttrykkelig `draft`, og review-rubricen sier at det ikke er build-ready fordi produkt-/stakkbeslutninger og målbare akseptgrenser fortsatt er åpne. Separate komplette epics/stories ble ikke funnet. Ikke publiserte krav markeres `NOT VERIFIED`; de utledes ikke. Refleksjonsrapporten må fullføres og leveres i riktig kanal etter at formatkrav er hentet.

## Avgrensning

Dette er en revisjonsrapport fra 2026-11-16, ikke en samtidig historisk prosesslogg eller formell faglærergodkjenning. Resultater fra tidligere manuelle Gemini-tester er brukerrapporterte og ikke gjentatt. Prompt 027 forblir et dokumentert historisk hull.
