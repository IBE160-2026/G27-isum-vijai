---
title: 'MVP-002 – Gemini AI-generering fra forelesningsnotater'
type: 'feature'
created: '2026-11-15'
status: 'done'
route: 'dispatch'
review_loop_iteration: 0
baseline_commit: 'f528b5179aef03e0fe0eec6f9cb7f7eb819281a9'
context:
  - '{project-root}/product-brief.md'
  - '{project-root}/_bmad-output/planning-artifacts/prds/prd-G27-isum-vijai-2026-10-23/prd.md'
  - '{project-root}/docs/decisions/DECISION_LOG.md'
  - '{project-root}/_bmad-output/implementation-artifacts/spec-mvp-001-pdf-ingestion.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Appen bruker lokal ekstraktiv oppsummering og en fast demoquiz, mens Product Brief krever notatbasert sammendrag, begreper og quiz med innstillinger.

**Approach:** Legg til en valgfri Gemini-flyt med `google-genai` for tekst eller lokalt uttrekket PDF-tekst. Behold lokal modus som standard, krev aktiv personvernbekreftelse før hvert eksternt kall, og behold eksisterende PDF- og lokalbehandling.

## Boundaries & Constraints

**Always:** Bruk offisiell Gemini Developer API og `google-genai`; konfigurer modell; hent nøkkel bare fra `GEMINI_API_KEY` eller Streamlit Secrets og send den eksplisitt til klienten. Ikke foreta kall ved opplasting eller uten eksplisitt genereringshandling og samtykke. Opplys om ekstern behandling, Free Tier-vilkår og at innhold ikke garanteres korrekt. Behandle notater som upålitelige promptdata; bruk strukturert, validert respons; vis trygge feil uten nøkkel, notater eller stack trace. Ingen varig notatlagring. Gemini-valget er foreløpig, ikke et dokumentert gruppevedtak.

**Never:** Ikke OCR, betalt API-aktivering, automatisk ekstern behandling, ekte studentdata i tester, ny tjeneste eller persistens, endring av Product Brief/PRD, eller lukking av DEC-001–DEC-005. Ikke fjern/erstatt lokal sammendragsflyt eller godkjent PDF-funksjon. Ikke commit, push eller opprett PR.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Lokal standard | Tekst/PDF, lokal modus | Eksisterende lokale sammendrags-/begrepsresultater og demoquiz; ingen nettverkskall | Eksisterende forståelige valideringsfeil |
| Gemini med samtykke | Gyldig notattekst, innstillinger, avkrysset samtykke og generering | Strukturert sammendrag, begreper med forklaringer, quiz med fasit | Trygg tjenestefeil |
| Manglende samtykke/nøkkel | AI-modus uten bekreftelse eller konfigurasjon | Ingen API-kall | Veiledning om nødvendig handling; ingen hemmelighet vist |
| Utilstrekkelige notater | Kildeteksten gir ikke grunnlag for valgt antall quizspørsmål | Ingen spørsmål diktes opp; resten av resultatet kan vises hvis gyldig | Tydelig beskjed om færre grunnlag enn ønsket |
| Ugyldig/tom respons | Mangelfull JSON, feil antall spørsmål eller ugyldige felt | Ingen delvis/ugyldig resultat vises | Trygg valideringsfeil |
| Tjenestefeil | Rate limit, timeout, nettverks-/SDK-feil | Ingen rå leverandørdetaljer vises | Norsk melding med trygg mulighet for nytt forsøk |
| PDF til Gemini | PDF lastet opp, lokalt uttrekk fullført, deretter eksplisitt samtykke og generering | Bare uttrekksteksten sendes ved generering | Parserfeil stopper før nettverkskall |

</frozen-after-approval>

## Code Map

- `app.py` — Streamlit tekst/PDF-valg, lokal genereringshandling, resultatvisning og interaktiv demoquiz. Behold lokal flyt; legg AI-modus til uten automatisk kall.
- `prototype/generator.py` — inputvalidering, lokal oppsummering/begreper og `generate_result`; lokal algoritme skal ikke erstattes.
- `prototype/pdf_ingestion.py` — `extract_pdf_text(bytes)` med 10 MiB/200-side/1 000 000-tegnsgrenser; PDF skal fortsatt behandles lokalt først.
- `tests/test_app.py`, `tests/test_generator.py`, `tests/test_pdf_ingestion.py` — AppTest, generator- og syntetiske PDF-fixtures.
- `requirements.txt` — eneste avhengighetsfil; legg til `google-genai` når storyen godkjennes.
- `docs/decisions/DECISION_LOG.md` — DEC-003 leverandør/kostnad/dataflyt og DEC-004 testmodus er åpne; DEC-005 har bare pypdf-delbeslutning.
- `docs/testing/TEST_PLAN.md`, `docs/testing/TEST_LOG.md`, `README.md`, `docs/*` og `_bmad-output/implementation-artifacts/spec-mvp-001-pdf-ingestion.md` gir eksisterende test-, bruks- og BMAD-spor; bevar historikken.
- `product-brief.md` og PRD §5–7 fastsetter funksjonsmål. PRD §6.2/§6.3 og §9 sier ekstern KI, kostnad, dataflyt, quizformat og grenser er uavklart; `architecture/technology.md` beskriver et annet prosjekt og skal ikke brukes.

## Tasks & Acceptance

**Execution:**
- [x] `prototype/gemini_service.py` — implementert nøkkeloppslag, konfigurerbar modell, strukturert generering/validering og trygg tjenestefeil.
- [x] `app.py` — lokal/Gemini-modus, innstillinger, personverninformasjon og samtykke før generering; tekst og lokalt PDF-uttrekk går gjennom samme AI-adapter.
- [x] `requirements.txt` — offisiell `google-genai`-SDK lagt til uten API-nøkkel eller betalt konfigurasjon.
- [x] `tests/test_gemini_service.py`, `tests/test_app.py` — mockklient tester struktur, utilstrekkelig dekning, ugyldig svar, manglende nøkkel/samtykke og trygge feil; eksisterende tester dekker lokal tekst/PDF.
- [x] `docs/decisions/DECISION_LOG.md` — Gemini/SDK er dokumentert som foreløpig implementasjonsvalg med offisielle kilder; DEC-003 og øvrige beslutninger forblir åpne.
- [x] `README.md`, `docs/testing/TEST_LOG.md`, `docs/testing/TEST_PLAN.md` og denne spesifikasjonen oppdatert append-only med testbevis og begrensninger.
- [x] `docs/CODEX_PROMPT_LOG.md`, `docs/CHANGELOG_PROCESS.md`, `docs/PROJECT_CONTEXT.md` og `docs/bmad/WORKFLOW_STATUS.md` — loggfør PR #3/#4-merge-SHA-er, Sprint 002-arbeid, review og gjenstående beslutninger uten å skrive om eldre status.

**Acceptance Criteria:**
- Given tekst eller en lokalt uttrekt PDF, when lokal modus brukes, then lokal flyt virker uten nettverkskall.
- Given en bruker velger Gemini-modus, when samtykke ikke er aktivt, then notater sendes ikke.
- Given aktivt samtykke og gyldig input, when generering startes, then resultatet har sammendrag, forklarte begreper og valgt antall notatbaserte quizspørsmål med nøyaktig fire alternativer, ett riktig svar og kort forklaring.
- Given notatene ikke støtter valgt antall spørsmål, when generering skjer, then systemet gir tydelig beskjed og dikter ikke opp spørsmål eller svar.
- Given AI-innstillingene vises, when studenten velger lengde, vanskelighetsgrad og antall, then valgene er kort/middels/lang, lett/middels/vanskelig og 1–10 spørsmål; standardene er middels og 5 spørsmål.
- Given manglende nøkkel, ugyldig respons eller ekstern feil, when generering forsøkes, then appen viser en forståelig feil uten å lekke hemmeligheter eller rå notater.
- Given syntetiske tester, when pytest kjøres med mockede SDK-kall, then verifiseres tekst-/PDF-integrasjon og feiltilfellene uten ekte Gemini-kall.

## Implementation Notes

Ingen tidligere Sprint 002-spesifikasjon eller egnet arkitektur ble funnet. Baseline `f528b5179aef03e0fe0eec6f9cb7f7eb819281a9` ble kontrollert i isolert worktree `feature/mvp-002-gemini-ai`; arbeidsområdet var rent. Produktkildene er gjeldende Product Brief og PRD, fortsatt `draft`. Googles offisielle dokumentasjon (kontrollert 2026-11-15) opplyser at Free Tier-data kan brukes til produktforbedring; dette krever tydelig personverninformasjon og gir ikke grunnlag for å love konfidensialitet. Ingen ekte API-kall skal brukes i implementeringstester.

**Foreløpige produktvalg (2026-11-15):** Brukeren oppga kort/middels/lang sammendragslengde; 1–10 spørsmål (standard 5); lett/middels/vanskelig vanskelighetsgrad (standard middels); og flervalg med nøyaktig fire alternativer, ett riktig svar, fasit og kort forklaring. Spørsmål og forklaringer skal være forankret i notatene; utilstrekkelig dekning skal gi tydelig beskjed og ingen oppdiktet utfylling. Dette er brukeroppgitte, foreløpige valg for implementering, ikke dokumentert formell gruppebeslutning. PRD og beslutningsstatuser endres ikke.

## Spec Change Log

## Review Triage Log

| Finding | Verdict and evidence | Route / resolution |
|---|---|---|
| Blind Hunter: PDF-uploaderen i Gemini-modus sa bare at PDF behandles lokalt. | low — PDF-uttrekket skjer lokalt, men teksten sendes eksternt ved samtykket generering; formuleringen kunne skjule det siste trinnet. | patch — Hjelpeteksten skiller nå lokal uttrekking fra senere samtykket Gemini-kall. |
| Blind Hunter: Gemini-fasit og forklaring ble vist før svar. | medium — Resultatrendereren viste fasit før studentens quizinnsending. | patch — Fasit og forklaring vises først i tilbakemeldingen etter innsending; AppTest verifiserer dette. |
| Blind Hunter: samtykke ble stående avkrysset etter en generering. | false — Ny generering krever fortsatt eksplisitt knappetrykk mens samtykkefeltet er synlig og aktivt; intensjonen krever aktiv bekreftelse før kall, ikke at den automatisk nullstilles. | Avvist — Tilstanden er et aktivt samtykke, og det gjøres ikke kall ved rerun/opplasting. |
| Blind Hunter: tekstnotater har ingen størrelsesgrense. | maybe-false — Koden setter ingen grense, men konsekvensen av en realistisk stor tekstinput avhenger av leverandørens kvoter og ønsket produktgrense. | defer — Registrert i `deferred-work.md` for avklaring før en grense innføres. |
| Blind Hunter: dupliserte quizalternativer kunne bestå. | medium — Valideringen sjekket fire strenger og at svaret var blant dem, men avviste ikke like alternativer. | patch — Tjenesten krever nå fire distinkte alternativer; tjenestetest dekker avvisning. |
| Blind Hunter: resultat fra forrige modus ble stående ved modusbytte. | medium — Modusbytte kunne beholde AI-resultat i lokal modus, blant annet med utilgjengelig `question_count`. | patch — Modusvelgeren tømmer nå resultat og tilbakemelding; AppTest kontrollerer overgangen. |
| Blind Hunter: strukturelt gyldige, ikke-forankrede svar ble godtatt. | medium — Den første validatoren inspiserte ikke kilden og kunne derfor ikke avvise sitater eller påstander som manglet i notatene. | patch — Strukturert svar krever ordrette kildesitater for begrep, spørsmål, svar og forklaring; sitater sjekkes som eksakte delstrenger. Begrensningen om semantisk feilbruk er synlig og dokumentert. |
| Edge Case Hunter: skifte til Lokal med ufullstendig Gemini-resultat kunne bruke udefinert `question_count`. | medium — Syntetisk UI-resultat med `insufficient_questions` viste denne banen dersom resultatet overlevde modusbytte. | patch — Samme modusbytte-rydding som over fjerner den nå; AppTest bekrefter. |
| Edge Case Hunter: fire like alternativer kunne bli presentert som fire valg. | medium — `len(options) == 4` tillot duplikater. | patch — Samme unike-alternativsvalidering som over avviser det. |
| Edge Case Hunter: akseptkravet om fire alternativer kunne oppfylles av gjentatte verdier. | medium — Før rettelsen kunne fire elementer være færre enn fire distinkte alternativer. | patch — Samme unike-alternativsvalidering dekker dette overlappende funnet. |
| Final QA: svaralternativer som bare skilte på casing eller whitespace ble ikke regnet som duplikater. | low — Slike valg kunne fremstå like for studenten selv om strengene var teknisk ulike. | patch — Alternativer normaliseres med whitespace-trimming/case-folding før unikhetskontroll; regresjonstest dekker varianten. |
| Final QA: tidligere resultat ble stående mens tekstnotatene ble endret i Streamlit-formen. | medium — Forminput trigget ikke rerun før innsending, så resultat fra gamle notater kunne fortsatt vises. | patch — Notatfelt og uploader bruker `on_change` for å tømme resultat og quizfeedback; AppTest dekker redigering før ny generering. |
| Verification Gap: Streamlit Secrets-fallback var ikke testet. | low — Manglende nøkkel-test beviste ikke at secrets-only nøkkel når SDK-klienten. | patch — Mocktest setter bare Streamlit Secret og verifiserer eksplisitt klientnøkkel. |
| Verification Gap: `GEMINI_MODEL`-overstyring var ikke testet. | low — Eksisterende test verifiserte bare standardmodell. | patch — Mocktest setter miljøvariabel og verifiserer at SDK-kallet bruker verdien. |
| Verification Gap: Gemini-fasit ble vist før svar. | medium — Resultatrendereren viste svaret før quizinnsending. | patch — Samme svarskjuling som over, verifisert av AppTest. |

## Verification

**Commands:**
- `python -m pytest -q` — hele suiten skal bestå.
- `python -m pytest -q tests/test_gemini_service.py tests/test_app.py tests/test_pdf_ingestion.py` — målrettede AI-/UI-/PDF-tester skal bestå.
- `git diff --check origin/main` — ingen whitespace-feil.
- Eksisterende Markdown-/dokumentasjonstester — konsistens og historikklenker skal bestå.

**Manual checks:** Ingen ekte Gemini-kall. Kontroller at lokal modus ikke kaller SDK, at samtykke vises før Gemini-kall, og at PDF ikke sendes ved opplasting alene.

**Implementeringsresultat (2026-11-15):** `python -m pytest -q` fra isolert MVP-001-miljø ga `46 passed in 1.33s`. Målrettede Gemini/UI/PDF-tester inngår i totalen. Ingen ekte Gemini-kall eller nettleserbasert manuell kontroll ble utført. Tjenesten mapper timeout eksplisitt, rate-limit etter SDK-feiltype/status, og øvrige tjenestefeil til trygg generisk melding. Kostnadsansvar, produksjonsgodkjenning og dataflyt er fortsatt åpne under DEC-003.

**Oppfølgingsverifikasjon (2026-11-15):** Korrigert Gemini-resultatvisning slik at demoquiz-merknad bare vises i lokal modus, og lagt til mockbasert AppTest for tekstgenerering, quizresultat og utilstrekkelig antall spørsmål. Full pytest-suite: `47 passed in 1.47s`; målrettet Gemini/UI/PDF-suite: `33 passed in 1.10s`; `git diff --check` exit 0. Ingen ekte Gemini-kall eller manuell nettlesertest.

**PDF-integrasjonsverifikasjon (2026-11-15):** AppTest dekker nå opplasting av syntetisk PDF, lokal uttrekking, fravær av kall ved opplasting og mockgenerering etter eksplisitt samtykke. Full pytest-suite: `48 passed in 1.37s`; målrettet Gemini/UI/PDF-suite: `34 passed in 1.14s`; `git diff --check` exit 0. Ingen ekte Gemini-kall eller manuell nettlesertest.

**Gjennomgangsverifikasjon (2026-11-15):** Etter triagerettelser bestod full pytest-suite med `59 passed in 1.66s`; målrettet Gemini/UI/PDF-suite med `45 passed in 1.27s`; `git diff --check` mot baseline bestod. Syntetiske tester dekker at sitater for begrepsterm/-forklaring og quizspørsmål, svar og forklaring må finnes som eksakte delstrenger i notatene. Dette gir etterprøvbar tekstlig støtte, men kan ikke garantere at sitatet semantisk beviser påstanden eller at annet KI-innhold er feilfritt. Ingen ekte Gemini-kall eller manuell nettlesertest. Gjenstående: avklar maksimal tekststørrelse med hensyn til leverandørkvoter; DEC-003 og produksjonsgodkjenning, kostnadsansvar og dataflyt forblir åpne.

**Endelig dokumentasjonsverifikasjon (2026-11-15):** Etter siste dokumentoppdatering bestod full pytest-suite med `59 passed in 1.72s`, målrettet Gemini/UI/PDF-suite med `45 passed in 1.32s`, og `git diff --check` mot baseline.

**Tillegg etter kvalitetskontroll (2026-11-15):** Konfigurerte eksplisitt 30 000 ms SDK-timeout via offisielle `HttpOptions`, med mocktest. Sitatkontrollen normaliserer nå store/små bokstaver og whitespace og krever også kildebevis for sammendraget. Dette gir strengere tekstlig kontroll, ikke garanti mot semantiske hallusinasjoner. Seneste fullsuite- og dokumentasjonskjøringer står i `docs/testing/TEST_LOG.md`.

**Siste kjøring etter alle kode- og dokumentasjonsendringer (2026-11-15):** Isolert miljø `/private/tmp/G27-isum-vijai-mvp001-venv`: full pytest `60 passed in 1.73s`; målrettet Gemini/UI/PDF `46 passed in 1.33s`; diff-check mot `f528b5179aef03e0fe0eec6f9cb7f7eb819281a9` bestod.

**Final QA (2026-11-15):** Nytt isolert Python 3.12.12-miljø installerte `requirements.txt`; `google-genai 1.75.0` og adapterimport bestod. Etter QA-rettelser bestod siste fullsuite `63 passed in 2.05s`, målrettet Gemini/UI/PDF `49 passed in 1.81s` og dokumentasjonstester `3 passed in 0.25s`. Streamlit health-check returnerte `ok` uten Gemini-nøkler i prosessmiljøet. `git diff --check f528b5179aef03e0fe0eec6f9cb7f7eb819281a9` bestod etter loggoppdateringen; lokal commit ble ikke opprettet før kontrollene var fullført. Ingen ekte Gemini-kall eller studentdata.

**Endelig Git-/konfigurasjonsspor (2026-11-15):** Lokal commit `875a8f57205467d30b9b81f9a31084cc80b6bf5f` (`feat: add Gemini AI summaries and grounded quizzes`) ble opprettet med author/committer `AksVijai <akshayah.vijai@himolde.no>`; ingen push/PR. Brukeren opplyste at nøkkelen er lagt inn i Streamlit Secrets, men lokal vs. Community Cloud er ikke avklart. Nøkkelen er ikke lest/testet og ingen ekte API-kall er gjort. Den lokale `.streamlit/secrets.toml`-filen mangler, og Git har ingen ignore-regel for `.streamlit/secrets.toml` eller `secrets.toml`; dette må avklares før en lokal hemmelighetsfil eventuelt opprettes.

**Feildiagnose (2026-11-15):** Brukeren rapporterte at lokal Streamlit på `localhost:8502` og Gemini-UI fungerer, men første manuelle generering viste generell tilkoblingsfeil. Dette er ikke bevis på fungerende Gemini-integrasjon. Adapteren brukte standard `gemini-2.5-flash`, konfigurerbar `GEMINI_MODEL`, 30 sekunders timeout og streng responsvalidering. Tidligere ble flere autentiserings-, modell-, kvote-, nettverks- og JSON-feil klassifisert likt. Adapteren er oppdatert med separate sikre meldinger og mocktester. Lokal `.streamlit/secrets.toml` er bekreftet til stede, ikke tracked og ignorert av Git; innhold/nøkkel er ikke lest. Ingen ekte kontrollkall eller studentdata ble brukt. En tidlig testkjøring forsøkte utilsiktet nettverk med syntetisk `notes` gjennom Streamlit Secrets før testen ble isolert; resultatet var generell nettverksfeil, og om Gemini mottok forespørselen kan ikke fastslås.

**Presisering etter fullsuite (2026-11-15):** En UI-test hadde samme uønskede bruk av lokal Secret og ble også isolert. Begge automatiserte testene forsøkte nettverk kun med syntetiske notater; mottak hos Gemini kan ikke bekreftes. De isolerte testene dekker manglende nøkkel uten Secrets-oppslag. Sluttresultat: fullsuite `72 passed in 2.60s`; `git diff --check` bestod. Ingen studentnotater ble sendt, og ekte Gemini-integrasjon er fortsatt ikke verifisert.

**Rotårsaksanalyse – oppfølging (2026-11-15):** Den rapporterte teksten produseres av catch-all-fallbacken i `_provider_error_message()` etter at `generate_gemini_result()` fanger et hvilket som helst ikke-`GeminiServiceError`-unntak. `app.py` viser adapterfeilen direkte. Dermed kunne tidligere nettverksklassifisering skjule programmeringsfeil; den beviser ikke nettverksrotårsak. SDK `google-genai 1.75.0`-signaturene og lokal validering av JSON response config/schema er kontrollert. API-nøkkelmodus bruker SDK-default `v1beta`, timeout 30 000 ms. Ingen request-parametere er endret. Diagnostikken bruker nå SDK `APIError`-statuskode/statusenum og typer for timeout/transport; ukjente feil gir `GEMINI-UNKNOWN`; uventet Secrets-feil gir `GEMINI-SECRETS`. API-serverens godkjenning, nøkkel-/modelltilgang og årsaken til manuell feil er ukjent. Ingen ekte generering er verifisert. Se siste testresultater i `docs/testing/TEST_LOG.md`.

**Sluttverifisering:** Målrettet Gemini/UI `51 passed in 2.69s`; siste full pytest etter dokumentasjonsoppdatering `77 passed in 2.95s`; `git diff --check` bestod. Ingen ekte Gemini-kall.

**GEMINI-MODEL-oppfølging (2026-11-15):** Den rapporterte `[GEMINI-MODEL]`-feilen er observert, men kan ikke fastslås som rotårsak uten modelltilgang for brukerens API-nøkkel. Adapteren bruker `model`-argumentet når eksplisitt gitt, ellers `GEMINI_MODEL` fra prosessmiljøet, med `gemini-2.5-flash` som standard. Variabelen var ikke satt i Codex-prosessen; separat Streamlit-/Cloud-prosess er ikke kontrollert. API-key-flow bruker offisiell `google-genai` 1.75.0 Gemini Developer API; lokal SDK-kilde viser API-key-endepunktet `generativelanguage.googleapis.com`, `v1beta` og `Models.list()` med `name`/`supported_actions`. Det er lagt til en manuell CLI-diagnostikk som krever `--list-models --confirm-external-call`, lister kun ID-er/handlinger og aldri logger nøkkel eller provider-body. Ingen `models.list()` eller `generate_content` ble kalt. Google dokumenterer `gemini-3.5-flash-lite` som stabil, med strukturert output og Free Tier-pris, men nøkkelspesifikk tilgang er uverifisert. Ingen modellstandard/-verdi er endret. Se testloggen for nye mocktester.

**Etter godkjent `models.list()` (2026-11-15):** Én godkjent modellisting fra denne worktreen inkluderte `gemini-2.5-flash` og `gemini-3.5-flash-lite`, begge med `generateContent`, samt øvrige Flash-ID-er i `docs/testing/TEST_LOG.md`. Dette bekrefter at nøkkelen som diagnostikken fant kan liste modellene, men tester ikke faktisk generering, JSON-schema-aksept eller en annen Streamlit-/Cloud-prosess. Googles modell-/prisdokumentasjon bekrefter `gemini-3.5-flash-lite` som stabil, tekstgenererende, structured-output-kompatibel og tilgjengelig på Free Tier. Den anbefales som alternativ; standarden er ikke endret. Den tidligere `[GEMINI-MODEL]`-feilen er fortsatt observert, ikke bekreftet rotårsak.

**Midlertidig lokal prøve (2026-11-15):** Etter brukerens godkjenning startet en separat Streamlit-prosess fra dette worktreet med `GEMINI_MODEL=gemini-3.5-flash-lite` på `127.0.0.1:8503`; den eksisterende instansen på 8502 ble ikke endret. Den aktive prosessvariabelen ble bekreftet uten å vise andre miljøverdier. Standardmodell/kildekode, `.env`, Secrets og nøkkel ble ikke endret. Ingen genereringskall er utført; manuell brukerprøve gjenstår. Full pytest `83 passed in 3.01s`; se TEST_LOG for dekket lokal-, PDF- og samtykkeflyt.


**Manuell testoppdatering (2026-11-15):** Brukeren bekreftet tekstbasert E2E-generering på port 8503 med lokal `GEMINI_MODEL=gemini-3.5-flash-lite` og syntetiske prosjektledelsesnotater: relevant sammendrag, tre begreper og tre relevante firevalgsquizspørsmål. Fem var ønsket. Koden sender fem videre, instruerer modellen til å lage færre ved manglende kildegrunnlag, aksepterer færre gyldige spørsmål og viser antallet; det ble ikke funnet hardkodet maksimum på tre eller et forkastingsfilter. Den eksakte årsaken til modellens tre spørsmål kan ikke bevises uten den manuelle responsen. Ikke svekk kildevalideringen. Quizretting/poeng og PDF via Gemini gjenstår som manuelle verifikasjoner. Denne rapporterte testen er avgrenset til tekstgenerering, ikke full sprintgodkjenning.


**Sluttkontroll – manuelle akseptprøver rapportert av bruker (2026-11-15):** Tekst med `gemini-3.5-flash-lite` på port 8503 ga relevant sammendrag/begreper, fire av fem spørsmål og 4/4 i siste quiz. En tidligere quiz ga 0/4, men svarvalg er ikke dokumentert. PDF `testnotater_informasjonssystemer_databaser.pdf`: opplasting og tekstuttrekk fungerte, Gemini genererte relevant sammendrag, tre begreper, tre av fem spørsmål, og quiz ga 1/3 med fasit/forklaringer som ifølge bruker samsvarte med notatene. Dette er brukeroppgitt evidens, ikke reproduksjon i sluttkontroll. Kildekodens standard er fortsatt `gemini-2.5-flash`; alternativet ble bare satt i lokal port 8503-prosess. Full pytest: 83 bestått; `git diff --check` bestod. Sprintens manuelle hovedflyter er rapportert testet. Færre spørsmål enn ønsket er tillatt av grounding-regelen og innebærer ikke i seg selv feil.
