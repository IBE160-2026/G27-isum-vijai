---
title: 'MVP-001 – PDF-opplasting og tekstuttrekk'
type: 'feature'
created: '2026-11-15'
status: 'done'
route: 'dispatch'
review_loop_iteration: 0
baseline_commit: '1227fb443e52815f831b3f5720b4f41844f72ad0'
context:
  - '{project-root}/product-brief.md'
  - '{project-root}/_bmad-output/planning-artifacts/prds/prd-G27-isum-vijai-2026-10-23/prd.md'
  - '{project-root}/docs/decisions/DECISION_LOG.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Prototypen tar imot innlimt tekst, men ikke PDF-notater som er del av Product Briefs v1-scope. Studenten kan derfor ikke bruke den planlagte dokumentflyten.

**Approach:** La studenten velge tekst eller PDF i Streamlit. For tekstbaserte PDF-er trekkes teksten ut lokalt og sendes til eksisterende `generate_result`; vis forståelige feil for tomme, ugyldige eller PDF-er uten uttrekkbar tekst.

## Boundaries & Constraints

**Always:** Behold eksisterende tekstflyt. Behandle PDF i minnet uten varig lagring. Skill parserfeil fra generatorfeil og vis ikke interne parserdetaljer. Bruk godkjent `pypdf` kun til maskinlesbare PDF-er. Avvis filer over 10 MiB, PDF-er med mer enn 200 sider og uttrekk over 1 000 000 tegn med forståelig feilmelding. Registrer pypdf som en avgrenset delbeslutning under DEC-005; la DEC-001–DEC-004 og resten av DEC-005 stå åpne.

**Never:** Ikke implementer OCR, KI-/ekstern API, nye sammendrags-/quizinnstillinger eller persistens. Ikke endre Product Brief eller PRD.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Gyldig PDF | Maskinlesbar, ubeskyttet PDF med tekst | Uttrekket brukes som notater i eksisterende sammendragsflyt | Ingen |
| Flere sider | Maskinlesbar PDF med tekst på flere sider | Teksten følger siderekkefølgen med lesbare sideskift | Ingen |
| Tom/ugyldig PDF | Tom fil eller ikke-PDF/korrupt innhold | Ingen resultat genereres | Kort, forståelig feilmelding |
| Ingen tekst | Skannet eller teksttom PDF | Ingen resultat genereres; OCR påstås ikke støttet | Forklar at PDF-en ikke inneholder uttrekkbar tekst |
| Begrensninger | Fil >10 MiB, >200 sider eller uttrekk >1 000 000 tegn | PDF avvises før sammendragsflyt | Forklar aktuell grense |
| Passordbeskyttet | Kryptert PDF | Ingen resultat genereres | Forklar at passordbeskyttet PDF ikke støttes |
| Tekstinput | Brukeren velger innlimt tekst | Eksisterende flyt virker uendret | Eksisterende validering |

</frozen-after-approval>

## Code Map

- `app.py` — Streamlit-formen tilbyr tekst/PDF og sender input til `generate_result`; PDF-uttrekk er koblet inn som adapter før generator-kallet.
- `prototype/generator.py` — eksisterende validering og lokal sammendrags-/begrepsgenerering tar `str`; hold generatorens tekstlogikk uendret.
- `.streamlit/config.toml` — begrenser mottatt opplastingsfil til 10 MiB før appbehandling.
- `requirements.txt` — inneholder Streamlit og pytest; pypdf er lagt til i avhengighetslisten.
- `tests/conftest.py`, `tests/test_pdf_ingestion.py`, `tests/test_app.py`, `tests/test_generator.py` — syntetiske PDF-fixtures, parsergrenser, AppTest-integrasjon og eksisterende generator-/feiltester.
- `product-brief.md` og PRD §5/§7/§9 — tekst og PDF er omtalt; PRD er `draft`; pypdf er godkjent for maskinlesbar PDF i denne MVP-funksjonen, mens eventuell OCR fortsatt ikke inngår.
- `docs/decisions/DECISION_LOG.md` — før brukerens avgrensede pypdf-delbeslutning under DEC-005 uten å lukke resten.

## Tasks & Acceptance

**Execution:**
- [x] `prototype/pdf_ingestion.py`, `requirements.txt`, `.streamlit/config.toml` — trekk ut tekst med pypdf fra maskinlesbare PDF-er uten OCR, innenfor fil-/side-/tekstgrenser.
- [x] `app.py` — tilby PDF-upload, send vellykket uttrekk gjennom dagens `generate_result`-flyt, og fjern tidligere resultat når studenten bytter inputformat.
- [x] `tests/conftest.py`, `tests/test_pdf_ingestion.py`, `tests/test_app.py` — dekk gyldig én-/flersiders (inkludert norske tegn), tom, ugyldig, teksttom, kryptert PDF og grenser; verifiser PDF→generator i UI, trygg feil og at gammel tekst/resultat ikke blandes inn.
- [x] `docs/testing/TEST_PLAN.md`, `docs/testing/TEST_LOG.md` — registrer PDF-scenarioene og faktiske kjøringer uten å oppgradere bredere testcase-status.
- [x] `README.md`, `docs/CODEX_PROMPT_LOG.md`, `docs/CHANGELOG_PROCESS.md`, `docs/PROJECT_CONTEXT.md`, `docs/bmad/WORKFLOW_STATUS.md`, `docs/decisions/DECISION_LOG.md` — dokumenter bruk, godkjent pypdf-delbeslutning, faktisk implementering/teststatus og gjenstående MVP-arbeid; bevar historikk og hold DEC-001–004 åpne.
- [x] `_bmad-output/implementation-artifacts/spec-mvp-001-pdf-ingestion.md` — oppdater tasks, implementation notes og status etter faktisk arbeid; ikke marker bredere BMAD-/produktarbeid fullført.

**Acceptance Criteria:**
- Given en gyldig tekstbasert PDF, when studenten velger PDF og genererer, then brukes det uttrekkede innholdet som input til eksisterende sammendrags- og begrepsfunksjon.
- Given en tom eller ugyldig PDF, when den behandles, then vises en forståelig feil uten traceback eller resultat.
- Given en skannet/teksttom PDF, when den behandles, then forklares manglende uttrekkbar tekst og ingen OCR hevdes.
- Given tekstmodus, when studenten bruker dagens lim-inn-flyt, then fungerer den som før.

## Implementation Notes

Baseline er `origin/main` `1227fb443e52815f831b3f5720b4f41844f72ad0` i isolert worktree `feature/mvp-001-pdf-ingestion`. Brukeren opplyste 2026-11-15 at gruppen har godkjent pypdf som PDF-verktøy for maskinlesbare PDF-er. Dette registreres som delbeslutning under DEC-005; øvrige teknologivalg og eventuell framtidig OCR står åpne. Filgrensene er 10 MiB, 200 sider og 1 000 000 tegn for å holde behandling avgrenset.

**Implementasjonsstatus (2026-11-15):** `prototype/pdf_ingestion.py` leser bytes i minnet, avviser filer over grensen før parsing, krypterte PDF-er og for mange sider før uttrekk, og håndhever tegn-grensen fortløpende via pypdf sin `visitor_text`-callback. Den gir trygge norske feilmeldinger for parserfeil og manglende tekst. Streamlit tilbyr tekst-/PDF-valg og sender uttrekket til den uendrede generatoren; tidligere resultater fjernes ved formatbytte. `.streamlit/config.toml` setter opplastingsgrensen før appbehandling. pypdf-delbeslutningen er ført under DEC-005; DEC-001–DEC-004 og resten av DEC-005 forblir åpne. Build Step 04-reviewen er utført og patchfunn rettet. Denne enkeltstående PDF-integreringsstoryen er `done`; det markerer ikke hele MVP-en eller bredere produkt-/BMAD-arbeid som fullført.

## Verification

**Commands:**
- `/private/tmp/G27-isum-vijai-mvp001-venv/bin/python -m pytest -q` — `35 passed in 1.65s` etter reviewrettelser i isolert worktree 2026-11-15.
- `/private/tmp/G27-isum-vijai-mvp001-venv/bin/python -m pytest -q tests/test_pdf_ingestion.py tests/test_app.py` — `21 passed in 1.43s` etter reviewrettelser.
- `git diff --check origin/main` — exit 0.

**Manual checks:** Ikke utført i nettleser. AppTest-regresjoner verifiserer eksisterende tekstmodus; parseren testes med gyldig maskinlesbar, tom, ugyldig og teksttom PDF. Full testcase-status for T-001–T-009 forblir `PLANLAGT`.

## Review Triage Log

| Finding | Verdict and evidence | Route / resolution |
|---|---|---|
| Blind Hunter: tekstgrensen ble sjekket etter at hele siden var ekstrahert. | medium — En stor tekstside kunne bli materialisert før grensen ble oppdaget. | patch — Bruker `visitor_text` for å avbryte under ekstraksjonen; grenseoverskridende testcase består. |
| Edge Case Hunter: samme tekstgrense ble sjekket etter full side-ekstraksjon. | medium — Samme rotårsak som funnet over; callbacken avbryter før ekstraksjonen fullføres. | patch — Samme patch som over. |
| Blind Hunter: PDF-fixturen støttet bare ASCII. | low — Norske forelesningsnotater kunne ikke representeres i de syntetiske parser-testene. | patch — Fixturen bruker WinAnsi/cp1252 og testen verifiserer æøå/ÆØÅ. |
| Blind Hunter: grenseverdiene manglet i akseptansekriteriene. | false — Grensene står eksplisitt i godkjente constraints og input/edge-case-matrisen, og testene dekker dem; dette gir ikke et uverifisert implementeringsgap. | Avvist — Ingen endring av spesifikasjonens godkjente scope. |
| Blind Hunter: T-001 manglet UI-test med feil filtype. | false — UI-velgeren er begrenset til PDF-filer, og parser-testene avviser ugyldige PDF-bytes før sammendraget kjøres. | Avvist — Ingen påvist feil i brukerflyten. |
| Blind Hunter: opplastingsgrensen kunne være uklar før opplasting. | false — Både Streamlit-uploaderens `help` og serverkonfigurasjonen oppgir/ håndhever 10 MiB-grensen; README beskriver den også. | Avvist — Informasjonen er allerede synlig i opplastingskontrollen. |
| Blind Hunter: tidligere 26-testresultat kunne forveksles med sluttresultat. | low — Testloggen hadde et eldre resultat uten eksplisitt merking om at det var et mellomresultat. | patch — Overskriften og statuslinjen identifiserer nå kjøringen som mellomkjøring erstattet av sluttkjøringen. |
| Edge Case Hunter: gammelt sammendrag kunne vises etter formatbytte. | medium — Radioendring rerunner appen mens `prototype_result` lå igjen i session state; test viste at gammelt innhold ble vist under nytt format. | patch — Radioens `on_change` fjerner tidligere resultat og quizfeedback; AppTest dekker overgangen. |
| Blind Hunter: `strict=True` kan avvise PDF-er med strukturelle avvik. | false — Ingen akseptert krav lover støtte for feilformede PDF-er; oppdraget ber uttrykkelig om forståelig avvisning av ugyldige/korrupt PDF-er. Ingen konkret gyldig PDF som feiler ble påvist. | Avvist — Streng parsingsfeil følger oppgitt feilbehandling. |

Verification Gap Reviewer: ingen verifikasjonsgap funnet.

## Post-PR #3-integrasjon (2026-11-15)

PR #3-mergecommit `73fafcc0443019bf58ab69aaece503d17010c754` ble hentet som `origin/main` og integrert i PDF-branchen med mergecommit `ef834cd2a49383940ed1739a6654feb8a4a9672c`. PDF-commit `967d48abd1372beea239db7db576e0de2f5f7daf` er bevart som første forelder. Fire dokumentasjonskonflikter ble løst ved å beholde begge historikkdelene; applikasjonskode krevde ingen konfliktløsning. Etter integreringen bestod full pytest-suite med 35 tester, målrettede PDF/UI-/dokumentasjonstester med 24 tester, og `git diff --check`. PR #4 ble ikke pushet eller merget. Dette endrer ikke PDF-storyens opprinnelige baseline eller beslutningsstatus.
