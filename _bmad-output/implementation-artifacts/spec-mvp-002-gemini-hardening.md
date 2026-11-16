---
title: 'MVP Sprint 002 – modellstandard og kvalitetsrettelser'
type: 'bugfix'
created: '2026-11-16'
status: 'done'
route: 'dispatch'
review_loop_iteration: 0
baseline_commit: '34cf52e41c0b4fd04c845d0360b58a7136a17f15'
context:
  - '{project-root}/_bmad-output/implementation-artifacts/spec-mvp-002-gemini-ai.md'
  - '{project-root}/docs/decisions/DECISION_LOG.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Sprint 002 bruker fortsatt `gemini-2.5-flash` som fallback selv om `gemini-3.5-flash-lite` er listet for den godkjente API-nøkkelen og brukt i rapporterte manuelle tester. UI-en kan også beholde samtykke eller quiztilstand på tvers av endringer, og en tom modellquiz kan ende i en ugyldig 0-av-0-visning.

**Approach:** Sett den dokumenterte og testede modellen som standard, behold `GEMINI_MODEL`-overstyring og lokal modus, og lukk trygt avgrensede tilstands-/valideringsfeil med regresjonstester. Bevar gjeldende personvernregler og DEC-003 som åpen beslutning.

## Boundaries & Constraints

**Always:** Ingen eksterne Gemini-kall; ingen endring av nøkkel/Secrets; samtykke kreves for Gemini; notater er upålitelige; kildevalidering beholdes; testene bruker syntetiske data og mock; PDF-uttrekksgrenser og lokal behandling bevares. Bevar `PROMPT_HISTORY_GAPS.md` og alle eksisterende promptoppføringer.

**Never:** Ikke avgjør DEC-003 eller endre personvernvilkår, ikke fjern kildevalidering, ikke endre originalmappen, ikke les/endre `.memlog.md`/Secrets, og ikke utfør Git-operasjoner som commit, push eller merge.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Ny Gemini-standard | Ingen `GEMINI_MODEL` | Adapter velger `gemini-3.5-flash-lite`; eksplisitt miljøoverstyring vinner | Ingen nettverkskall i test |
| Notatendring etter samtykke | Gemini-modus, avkrysset samtykke, endret tekst/PDF | Resultat ryddes og samtykke må gis på nytt før generering | Ingen Gemini-kall uten ny bekreftelse |
| Endret quizinnstilling | Eksisterende quiz/feedback, endret antall/lengde/vanskelighet | Gammelt resultat og feedback ryddes | Ingen stale score eller motstridende antall |
| Tom quiz | Strukturert respons med tom `questions` | Avvises som ugyldig svar; UI viser ikke 0-av-0 quiz | Trygg valideringsmelding |
| Lang tekst | Gemini-input over dokumentert grense | Avvises før provider-kall; lokal modus påvirkes ikke | Forklarende grensemelding |

</frozen-after-approval>

## Code Map

- `prototype/gemini_service.py` — modellfallback, responsvalidering og grense for Gemini-notater; behold SDK-/JSON-schema- og kildebevisflyten.
- `app.py` — checkbox, tekst/PDF-inndata, innstillinger, resultatvisning og quizfeedback; Streamlit `on_change` brukes allerede til å rydde resultat ved input-/modusendring.
- `prototype/pdf_ingestion.py` — eksisterende grenser: 10 MiB, 200 sider og 1 000 000 uttrekkede tegn; bruk samme tegnverdi som Gemini-inngangsgrense.
- `tests/test_gemini_service.py`, `tests/test_app.py`, `tests/test_pdf_ingestion.py` — mockbaserte adapter-, AppTest- og lokal PDF-regresjoner.
- `tests/test_prompt024_traceability_docs.py` — dekker PROMPT 024-sporbarhet, men ikke inventar/gap-regler for hele promptarkivet.
- `docs/decisions/DECISION_LOG.md` — DEC-003 er fortsatt uavklart om leverandørgodkjenning, kostnad, dataflyt og oppbevaring.
- `docs/CODEX_PROMPT_LOG.md`, `docs/prompts/PROMPT_HISTORY_GAPS.md`, `docs/CHANGELOG_PROCESS.md`, `docs/PROJECT_CONTEXT.md`, `docs/testing/TEST_LOG.md`, `docs/bmad/WORKFLOW_STATUS.md`, `_bmad-output/implementation-artifacts/spec-mvp-002-gemini-ai.md` — append-only historikk og Sprint-status; gap-registeret skal ikke endres eller overskrives.

## Tasks & Acceptance

**Execution:**
- [x] `prototype/gemini_service.py` og `tests/test_gemini_service.py` — endre standardmodell og test standard, override, maksimal input og avvisning av tom quiz.
- [x] `app.py` og `tests/test_app.py` — nullstill samtykke/resultat ved notat-/PDF-endring, og resultat/feedback ved innstillingsendring; test hver overgang og tom quizvisning.
- [x] Ny dokumentasjonstest — kontroller at PROMPT 001–026 og 028 fortsatt er representert, PROMPT 027 er markert som gap og rekonstruert tekst er tydelig merket; ikke omskriv arkivet.
- [x] Test- og BMAD-filer nevnt i Code Map — append-only status for modellbytte, funn, testbevis, åpne DEC-003-forbehold og bevart prompt-historikk.

**Acceptance Criteria:**
- Given standardmiljø uten `GEMINI_MODEL`, when Gemini-adapteren bygges, then SDK-kallet bruker `gemini-3.5-flash-lite`, og eksplisitt miljøoverstyring fungerer fortsatt.
- Given endret input eller Gemini-innstilling etter en generering, when Streamlit kjører om, then tidligere resultat/feedback fjernes; endret input krever nytt aktivt samtykke.
- Given en tom quizrespons eller notater over den felles grensen på 1 000 000 tegn, when validering/generering startes, then appen stopper trygt uten ugyldig quizvisning eller provider-kall for overgrensen.
- Given lokal modus eller PDF, when eksisterende lokale flyter kjøres, then lokal modus forblir uavhengig av Gemini og PDF-uttrekkets nåværende grenser/flyt bevares.
- Given dokumentasjonstester, when hele testsettet kjøres, then nummerert promptinventar/gap-regler kontrolleres uten å kreve at PROMPT 027 finnes.
- Given DEC-003, when Sprint-status dokumenteres, then beslutningen forblir åpen og gjeldende samtykke/advarsel endres ikke.

## Implementation Notes

Implementert i worktree `feature/mvp-002-gemini-ai` med baseline `34cf52e41c0b4fd04c845d0360b58a7136a17f15`. Gemini fallbackmodellen er `gemini-3.5-flash-lite`; `GEMINI_MODEL` og eksplisitt modellargument overstyrer fortsatt. Adapteren bruker `MAX_EXTRACTED_CHARACTERS` fra PDF-uttrekket, avviser overgrensen før nøkkeloppslag og avviser tomme spørsmål. Streamlit nullstiller aktivt samtykke ved inputendring og fjerner resultat/quizfeedback/svarvalg ved input-/modus-/innstillingsendring og før ny generering. Lokal modus og kildebeviskontroll er beholdt.

Promptinventar/gap-regler ligger i `tests/test_prompt_history_inventory_docs.py`. `PROMPT_HISTORY_GAPS.md` er ikke endret. DEC-003 er fortsatt uavklart; ingen ekte Gemini-kall eller Secrets-lesing ble gjort.

**Senere beslutning (2026-11-16):** Brukeren vedtok en begrenset DEC-003 for valgfri prototypebruk med syntetiske, offentlige eller anonymiserte data uten personopplysninger/konfidensielt innhold. Produksjonsbruk og forholdene i punkt C krever ny beslutning. Dette vedtaket kom etter den godkjente hardening-spesifikasjonen og endrer ikke dens historiske frozen intent.


## Spec Change Log


## Review Triage Log

| Finding | Verdict and evidence | Route / resolution |
|---|---|---|
| Innholdsreview: tilgang til standardmodellen er ikke live-kontrollert i denne endringen. | false — `docs/testing/TEST_LOG.md` dokumenterer den tidligere bruker-godkjente `models.list()`-forespørselen med `generateContent` for `gemini-3.5-flash-lite`; samme logg dokumenterer brukerens vellykkede manuelle tekst- og PDF-generering med denne modellen. Denne endringen foretok ingen ny forespørsel. | Avvist — Tidligere evidens gjelder; ingen ny modellkontroll ble utført. |
| Innholdsreview: spek og verifikasjon motsier modelltilgang. | false — Avsnittet «Etter godkjent `models.list()`» i testloggen skiller tilgangslisten fra genererings-/JSON-verifikasjon. Nåværende spec sier at denne endringen ikke gjorde et eksternt kall, ikke at tidligere tilgang mangler. | Avvist — Historisk evidens og nåværende verifikasjonsgrense er ulike forhold. |
| Innholdsreview: ugyldig tom quiz kan vise sammendrag/begreper før UI-vakten stopper. | low — Den defensive UI-vakten lå etter sammendrag-/begrepsrendering; dersom en tom quizverdi nådde UI, ville delresultatet bli vist før resultattilstanden ble fjernet. | patch — Vakt flyttet før all AI-resultatvisning; regresjonstest bekrefter at sammendrag ikke rendres. |
| Innholdsreview: README forklarte ikke når samtykke nullstilles. | low — Endringer i input/modus nullstiller bekreftelsen, men README beskrev ikke at ny bekreftelse kreves for nye notater. | patch — README forklarer at samtykke nullstilles ved tekst-, PDF- eller modusendring. |
| Innholdsreview: dokumentasjonstesten kontrollerte ikke rekkefølgen på nummererte prompts. | low — Korrekte ID-er i feil rekkefølge ville passere den tidligere tellingstesten. | patch — Testen kontrollerer første forekomst-rekkefølgen for 001–026 og 028. |
| Innholdsreview: flere like rekonstruksjonsrader kunne skjule en rad uten markør. | low — `next(...)` kontrollerte bare første rad med aktivitetsnavn og overså duplikater. | patch — Testen krever én rad per kjent gruppe og kontrollerer markøren på den raden. |
| Innholdsreview: testloggen manglet reproducerbare kjørekommandoer. | false — Den nye testloggoppføringen inneholder eksakte målrettede, dokumentasjons- og fullsuite-kommandoer. | Avvist — Kommandoene er registrert. |
| Kvalitetskontroll: tidligere radiosvar kunne bli med ved ny Gemini-generering selv om resultat og poengsum ble tømt. | medium — Genereringshandleren fjernet bare resultater/feedback; `answer_*`-nøkler lå igjen i Streamlit-tilstanden og kunne gjenbrukes av quizradioene. | patch — Handleren bruker felles ryddingsfunksjon som også fjerner svarvalg; AppTest bekrefter at gammel feedback fjernes og at quiz starter fra standardvalg. |
| Promptinventartesten brukte et sett og kunne overse dupliserte overskrifter. | low — Den opprinnelige testlogikken kollapset like ID-er til ett settmedlem. Prompttesten teller nå overskrifter for hver påkrevde ID, med de dokumenterte tellingene for PROMPT 023 og 028. | patch — Assertions ble styrket. |
| Promptinventartesten burde avvise alle nummererte ID-er utenfor 001–026 og 028. | false — Kravet ber om at de eksisterende ID-ene fortsatt er representert og at 027 forblir gap; det forbyr ikke fremtidige nummererte oppføringer. Testen kontrollerer nå tellingene for påkrevde ID-er og fravær av 027, samtidig som nye ID-er kan legges til. | Avvist — Ingen ytterligere begrensning innført. |
| Fire generiske rekonstruksjonsmarkører kunne skjule at én kjent aktivitetsgruppe mistet markeringen. | low — En duplisert markør kunne kompensere for en manglende markør i en annen kjent gruppe. Testen kontrollerer nå markøren separat på hver av de fire dokumenterte rekonstruerte aktivitetsradene og tillater fremtidige rader. | patch — Radvise assertions ble lagt til. |
| Innstillingstesten kontrollerte synlig poengsum, men ikke lagret quizfeedback. | low — Testen beviste ikke at `quiz_feedback` ble fjernet fra Streamlit-tilstanden. Den kontrollerer nå at både `prototype_result` og `quiz_feedback` er borte etter innstillingsendring. | patch — Tilstandsassertions ble lagt til. |
| PDF-erstatningstesten kontrollerte samtykke, men ikke tidligere resultat/feedback. | low — Overgangstesten opprettet tidligere ikke et resultat og quizfeedback før PDF-en ble erstattet. Den gjør det nå og verifiserer at begge tilstandene ryddes. | patch — PDF-overgangstesten ble utvidet. |
| AppTest for overgrensetekst målte ikke provider-kall direkte. | false — Adaptertesten sender overgrensetekst til en fake klient og bekrefter at `models.calls` fortsatt er tom; AppTest verifiserer brukerens grensemelding gjennom samme adapter. Samlet dekker de at provider ikke kalles og at appen stopper trygt. | Avvist — Eksisterende adapterbevis dekker provider-grensen. |
| Testloggen kunne ha registrert fullsuite før siste dokumentasjonsendring. | false — Fullsuite ble kjørt på nytt etter alle kode-, test- og dokumentasjonsrettelser under review; sluttkjøringen står nedenfor. | Avvist — Sluttverifikasjon kjørt på gjeldende tre. |
| README beskrev fortsatt `gemini-2.5-flash` som standard. | low — Koden bruker nå `gemini-3.5-flash-lite`, så den gamle README-instruksen var misvisende. | patch — README-standarden ble oppdatert. |


## Verification

**Commands:**
- `./.venv/bin/python -m pytest -q` — hele suiten bestått.
- Dokumentasjonstestene — promptinventar/gap-test bestått.
- `git diff --check` — ingen whitespace-feil.

**Resultat (2026-11-16):** Målrettet Gemini/UI/PDF/dokumentasjonssuite `79 passed`; dokumentasjonstestene `5 passed`; fullsuite `99 passed`. `git diff --check` exit 0 etter dokumentasjonstillegg. Ingen eksterne provider-kall.
