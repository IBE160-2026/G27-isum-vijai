# Prosjektkontekst

## Gjeldende status – MVP SPRINT 002 (2026-11-15)

- **Git-baseline:** Brukeren bekreftet PR #3 MERGED på `73fafcc0443019bf58ab69aaece503d17010c754` og PR #4 MERGED på `f528b5179aef03e0fe0eec6f9cb7f7eb819281a9` (2026-11-15T12:48:19Z). Denne isolerte worktreen og `origin/main`-referansen brukt ved oppstart står på `f528b5179aef03e0fe0eec6f9cb7f7eb819281a9`.
- **Arbeidskopi:** Sprint 002 er lokalt committet på `feature/mvp-002-gemini-ai`, `/private/tmp/G27-isum-vijai-mvp-002-gemini`, SHA `875a8f57205467d30b9b81f9a31084cc80b6bf5f`, med `feat: add Gemini AI summaries and grounded quizzes`. Ingen push eller PR; lokal `main` forble `16a34ed30aca147e1b79a0a98eb855bde1fa6a00`; `origin/main`-referansen forble `f528b5179aef03e0fe0eec6f9cb7f7eb819281a9`.
- **Funksjon:** Valgfri Gemini-modus genererer sammendrag, begreper med forklaring og notatbasert flervalgquiz. Lokal modus er standard. Eksisterende pypdf-uttrekk skjer lokalt; Gemini-kall skjer først etter genereringshandling og aktiv samtykkebekreftelse.
- **Sikkerhet/personvern:** Nøkkel hentes fra `GEMINI_API_KEY` eller Streamlit Secrets og sendes eksplisitt til klienten; modell `GEMINI_MODEL` kan overstyres. Appen lagrer ikke notater varig. Free Tier behandles som ekstern behandling med produktforbedringsvilkår og synlig advarsel.
- **Begrensninger:** Sitatsjekk viser ordrett tekststøtte, men beviser ikke semantisk korrekthet. Ingen maksimalgrense for innlimt tekst er valgt. Ingen ekte Gemini-kall eller manuell nettlesertest er utført.
- **Kvalitet:** Siste QA: fullsuite 63 bestått (`2.05s`); målrettet Gemini/UI/PDF 49 (`1.81s`); dokumentasjonstest 3 (`0.25s`). Nytt isolert miljø installerte alle `requirements.txt`-avhengigheter, inkludert `google-genai 1.75.0`; adapterimport bestod. Streamlit health-check svarte `ok` med Gemini-nøkkelvariabler fjernet; `git diff --check` mot baseline bestod. Ingen ekte Gemini-kall.
- **Beslutninger:** Gemini og UI-valgene er foreløpige brukeroppgitte implementeringsvalg, ikke dokumentert formelt gruppevedtak. DEC-001–DEC-005 forblir åpne; PRD er `draft`; Product Brief Validate og hele MVP-en er ikke fullført.
- **Streamlit Secrets:** Brukeren opplyste at Gemini-nøkkel er lagt i Streamlit Secrets; lokal vs. Community Cloud er ikke avklart. Nøkkelen ble ikke lest eller testet. Den lokale `.streamlit/secrets.toml`-filen finnes ikke i denne worktreen; Git-kontrollen fant ingen ignore-regel for `.streamlit/secrets.toml` eller `secrets.toml`, og filene er ikke tracked. Ikke anta lokal konfigurasjon eller at et ekte kall virker.

## MVP-002 Gemini – feildiagnose (2026-11-15)

- Brukeren rapporterte at Streamlit kjører på `localhost:8502`, Gemini-modus er synlig, og første manuelle generering viste den generelle tilkoblingsfeilen. Dette dokumenterer ikke at ekte integrasjon fungerer.
- `.streamlit/secrets.toml` finnes i denne worktreen, er ikke tracked, og ignoreres nå av Git. Filinnhold/nøkkel ble ikke lest. Denne loggingen retter den tidligere Secrets-statusen ovenfor.
- Adapteren bruker `gemini-2.5-flash` som standard, `GEMINI_MODEL` som overstyring og 30 sekunders timeout. Før rettelsen ble HTTP 401/403/404, kvote, nettverk og ugyldig JSON i hovedsak vist som samme generelle feil. Strukturell validering av modellenes svar var allerede streng.
- **Sannsynlig årsak:** Den viste teksten kom fra adapterens generiske fallback, som kunne skjule ugyldig/avvist nøkkel, modelltilgang, nettverk, ufullstendig JSON eller andre SDK-feil. Derfor er en ukategorisert leverandør-/transportfeil sannsynlig, men nøyaktig årsak er ikke dokumentert. Appens egen kildevalidering gir særskilte meldinger og virker mindre sannsynlig.
- Feilhåndteringen gir nå egne, trygge meldinger for ugyldig nøkkel, modelltilgang, rate limit, kvote, timeout, nettverksfeil, tomt/ugyldig svar og appens innholds-/kildevalidering. Ingen rå SDK-feilmelding vises.
- Testkjøring avdekket at både manglende-nøkkel-testen og en UI-test kunne hente lokal Streamlit Secret og forsøke nettverk. Begge er isolert ved å stubbe nøkkeloppslaget. Forsøkene med bare syntetisk testtekst ga generell nettverksfeil; det kan ikke fastslås om Gemini mottok forespørsler. Ingen studentnotater ble brukt. Fullsuite består med 72 tester; `git diff --check` bestod. Ekte integrasjon er uverifisert.

### Oppfølging: rotårsaksanalyse

- Den rapporterte teksten kom fra den brede exception-handleren i `generate_gemini_result()` → `_provider_error_message()`; `app.py` viste `GeminiServiceError` direkte. Dermed kunne en intern `TypeError` bli presentert som generell Gemini-/tilkoblingsfeil. Manuell exception-type/status er ikke lagret, så ekstern rotårsak er ukjent.
- SDK 1.75.0 ble kontrollert lokalt: `Client`/`generate_content`-signaturene stemmer; API-nøkkelmodus velger automatisk `v1beta`; 30 000 ms er timeout i millisekunder; JSON MIME-type og schema er støttede felter. Lokal schema-validering bestod. Dette bekrefter ikke serveraksept.
- Feilklassifisering bruker nå SDK `APIError` statuskode/statusenum, kjente timeout-/transporttyper og konfigurasjons-`ValueError`. Ukjente feil får `GEMINI-UNKNOWN`; uventede Secrets-feil får `GEMINI-SECRETS`. Ingen exception-tekst eller sensitive data logges.
- Ingen modell- eller request-parametere er endret. Ingen ekte generering er verifisert. Se siste kjøringsresultater i `docs/testing/TEST_LOG.md`.
- Sluttverifisering etter oppfølgingen: målrettet Gemini/UI `51 passed in 2.69s`; siste fullsuite etter dokumentasjonsoppdatering `77 passed in 2.95s`; `git diff --check` exit 0. Kun mockede kall.

## Prompt-historikkontroll (2026-11-15)

- Promptloggen hadde 30 nummererte overskrifter og 27 unike ID-er (001–026 og 028). PROMPT 023 og 028 har flere overskrifter for oppfølging; PROMPT 027 mangler. Branchnavnet `docs/027-documentation-completion` beviser ikke at oppdraget var nummerert 027.
- PROMPT 028s originalanalyse og godkjenning er bevart i egne filer. PDF-/Gemini- og integrasjonsoppdrag etter PROMPT 028 er dokumentert i logger, men flere originalprompter ble ikke gjenfunnet; fullstendige hull og Git-proveniens er beskrevet i [PROMPT_HISTORY_GAPS.md](prompts/PROMPT_HISTORY_GAPS.md).
- De to originale brukeroppdragene i denne samtalen er arkivert ordrett som unummererte kilder. Ingen historisk prompt-ID er oppfunnet. Sessionlogger ble ikke åpnet fordi ingen prompt-only uttrekksmåte kunne utelukke hemmeligheter. `.memlog.md`, API-nøkler/Secrets og originalarbeidsmappen ble ikke lest eller endret.
- Denne kontrollen verifiserte lokalt relevante Git-objekter for PR #3-/PR #4-merge, PDF-arbeid og Sprint 002. Sprint 002-committen er lokal; push/PR og live PR-status er ikke bekreftet.

## Gemini modelltilgang (2026-11-15)

- Gjeldende kode bruker `GEMINI_MODEL` fra prosessmiljøet når satt, ellers `gemini-2.5-flash`. I Codex-prosessen var variabelen unset; dette fastslår ikke modellverdien i en separat Streamlit-/Cloud-prosess. Secrets ble ikke lest.
- Worktree-venv har offisiell `google-genai` 1.75.0. Adapteren bruker Gemini Developer API med `models.generate_content`, JSON MIME type og `response_schema`; lokal SDK-kilde viser API-key-base URL og standard `v1beta`. Dette er offline-kodekontroll, ikke provider-tilgangsverifikasjon.
- `prototype.gemini_diagnostics` lister modell-ID og `supported_actions` via `models.list()`. CLI krever `--list-models --confirm-external-call`; standardkjøring sender ikke noe. Ingen reell diagnostikk eller generering er utført.
- `gemini-3.5-flash-lite` er dokumentert som stabil, Free Tier-priset og støtter strukturert output. Tilgang for brukerens nøkkel gjenstår. `GEMINI-MODEL` er observert, ikke bekreftet rotårsak. Ingen modellendring er gjort; anbefalt neste steg er godkjent `models.list()` før endring av `GEMINI_MODEL`.
- **Etter godkjent diagnostikk:** Én `models.list()`-forespørsel returnerte `generateContent` for gjeldende `gemini-2.5-flash` og kandidat `gemini-3.5-flash-lite`; også øvrige Flash-kandidater står i testloggen. Dette er nøkkelspesifikk modelliste-tilgjengelighet, ikke en faktisk genererings-/JSON-schema-test. Anbefalt alternativ er `gemini-3.5-flash-lite`; standarden står uendret mens bruker vurderer modellendring.
- **Lokal prøveoverstyring:** En separat Streamlit-prosess på port 8503 ble startet med `GEMINI_MODEL=gemini-3.5-flash-lite`; bare den variabelen ble lest tilbake fra prosessmiljøet for å bekrefte konfigurasjonen. Ingen nøkkel ble vist eller endret, ingen generering er utført. 8502-prosessen ble latt urørt. Brukeren må gjennomføre manuell generering før suksess kan bekreftes.

## Gjeldende status – Git Integration 002 (2026-11-15)

- **PR #3:** Brukeren bekreftet at PR #3 er merget 2026-11-15T12:08:00Z med merge-SHA `73fafcc0443019bf58ab69aaece503d17010c754`. `git fetch origin main` bekreftet at `origin/main` peker på denne SHA-en.
- **PDF-branch:** `feature/mvp-001-pdf-ingestion` inneholder nå main via mergecommit `ef834cd2a49383940ed1739a6654feb8a4a9672c`, med PDF-commit `967d48abd1372beea239db7db576e0de2f5f7daf` og PR #3-merge som foreldre. PROMPT 028-artefakter og logger er med.
- **Konflikter og tester:** Fire dokumentlogger ble sammenflettet ved å bevare begge historikkdelene. Etter merge: full pytest-suite 35 bestått; målrettede PDF/UI-/dokumentasjonstester 24 bestått; `git diff --check` bestod.
- **PR #4:** Sist bekreftet av brukeren som `OPEN` og `MERGEABLE`; dette er ikke en ny live-kontroll. Ingen push er utført etter lokal merge, og PR #4 er ikke merget.
- **Produktstatus:** PDF-ingestion-storyen er fullført. PRD forblir `draft`; Product Brief Validate er ikke fullført; pypdf er en delbeslutning under DEC-005, og resten av DEC-005 samt DEC-001–DEC-004 står åpne. Hele MVP-en er ikke fullført.

## Historisk status – PROMPT 028 publisert før PR #3-merge (2026-11-15)

- **Publisert arbeid:** PROMPT 028-integreringen etter PR #2 er committet som `ec19c95a63e169ab90174abb2299bbdaba1ed357` på `docs/028-product-brief-alignment-post-pr2` og publisert i [PR #3](https://github.com/IBE160-2026/G27-isum-vijai/pull/3). Dokumentasjonsarbeidet er gjennomført, men PR #3 er ikke merget.
- **Sist verifiserte PR-status:** 2026-11-15 kl. 10:09:30 UTC: `OPEN`, base `main`, head `ec19c95a63e169ab90174abb2299bbdaba1ed357`, `MERGEABLE`. Ingen automatiske CI-checks var rapportert (`statusCheckRollup: []`). Statusen er fra før denne loggoppdateringen og skal ikke leses som en etterfølgende live-kontroll.
- **Avventer ved kontrolltidspunktet:** Gruppens gjennomgang og godkjenning før eventuell merge. PR #2 var merget i `1227fb443e52815f831b3f5720b4f41844f72ad0`; PR #3 ble senere merget som dokumentert ovenfor.
- **Produkt/BMAD:** Product Brief Validate er ikke fullført. PRD er fortsatt `draft`, og DEC-001–DEC-005 er fortsatt åpne. PROMPT 028-integreringsoppgaven er fullført; statusopplysningen om ventende PR #3-merge er historisk.

## Gjeldende status – PROMPT 028 etter PR #2 (2026-11-15)

- **Bekreftet merge:** `origin/main` peker på PR #2-mergecommit `1227fb443e52815f831b3f5720b4f41844f72ad0`, med foreldre `35ff46c422948330844f77ff07816ca86c815fc1` og PR #2-head `a5778f25991d9b88fa4c3c186d5b2d2536c36212`. Commit-tiden er `2026-11-14 21:49:15 +01:00`; PR-ens GitHub `merged_at`-felt ble ikke hentet fra Codex-miljøet.
- **Bekreftet basis:** Arbeidsbranch `docs/028-product-brief-alignment-post-pr2` er basert på `origin/main` SHA `1227fb443e52815f831b3f5720b4f41844f72ad0`. Den historiske PROMPT 028-kilden `72c0b67d2ac715f925d6b41a56a4636c97b4b83a` er bevart.
- **Teststatus:** Full pytest-suite bestod med 18 tester; `tests/test_prompt024_traceability_docs.py` bestod med 3. `git diff --check` var ren. Kjøringene er ført i [testloggen](testing/TEST_LOG.md).
- **Produktstatus:** Produktkode er ikke endret. Product Brief og PRD er uendret; PRD står `draft`, DEC-001–DEC-005 står `Uavklart`. Implementasjonsgapene i PROMPT 028-kravmatrisen består.
- **Utførelse:** Bare separat worktree endret; ingen commit, push, merge, rebase eller PR. `.memlog.md` er ikke lest eller endret.

## Historisk PROMPT 028-status (2026-10-26)

Den daterte PROMPT 028-analysen ble laget mot `main` `16a34ed30aca147e1b79a0a98eb855bde1fa6a00` og deretter kontrollert mot `120bb9052b7d477698fc4510ba302d11f4480c4e`. PR #2 var fortsatt åpen ved disse kontrollene. Disse snapshottene, testene, backup-referansen og daværende branch-statusen er bevart i PROMPT 028-oppføringene i [promptloggen](CODEX_PROMPT_LOG.md), testloggen og [implementasjonsartefaktet](../_bmad-output/implementation-artifacts/prompt-028-product-brief-alignment.md); de er ikke gjeldende status etter mergecommitten ovenfor.

Backup-filen som ble rapportert 2026-10-26 (`/private/tmp/prompt028-backup.UiRvpw/PROMPT_028_changes.tgz`, SHA-256 `dfc32820421a48f1360d18d70fa0fbb155d35a40049fdf57167c8d6ad335b2df`) ble ikke funnet ved den skrivebeskyttede kontrollen 2026-11-15. Ingen backup eller worktree ble slettet i denne oppgaven; arbeidskopien i opprinnelig worktree og commit `72c0b67…` står fortsatt som egne kilder.

Oppdatert: 2026-10-18

## Observert status – MVP-001 PDF-opplasting (2026-11-15)

- PDF-opplasting i Streamlit sender lokalt uttrekket tekst til uendret `generate_result`-flyt. `pypdf` leser filen i minnet; tekstgrensen håndheves under uttrekk. Bytte mellom tekst/PDF fjerner tidligere resultat. OCR, ekstern PDF-behandling og varig lagring er ikke implementert.
- Avvisningsgrenser: 10 MiB input, 200 sider og 1 000 000 uttrekkstegn. Passordbeskyttede, ugyldige, tomme og teksttomme PDF-er får brukerrettet feilmelding uten interne parserdetaljer.
- `pypdf` er godkjent som avgrenset PDF-verktøy under DEC-005; øvrige teknologivalg i DEC-005 står åpne. DEC-001–DEC-004 er fortsatt uavklart; PRD forblir `draft`.
- Implementasjonen og testene er i isolert worktree `/private/tmp/G27-isum-vijai-mvp-001-pdf`, branch `feature/mvp-001-pdf-ingestion`, og er lokalt committet etter review. Endringen er ikke pushet. Reviewrettelser er verifisert med fullsuite 35 bestått og 21 målrettede PDF/UI-tester; se spesifikasjonen og testloggen. PR #3-arbeid og opprinnelig arbeidsmappe er holdt utenfor.

> **Historisk øyeblikksbilde:** Opplysningene i dokumentasjonen nedenfor beskriver statusen per 2026-10-18. De er bevart som historikk og er ikke dagens status.

## Prosjekt

- **Bekreftet:** Prosjektnavnet i produktbriefen er «Foredragsnotater → Sammendrag & Quizgenerator».
- **Bekreftet:** Gruppen er G27 – G27-isum-vijai. README oppgir medlemmene Thor E Isum, Akshayah Vijai og Abena Vijai.
- **Bekreftet:** Dette er et gruppeprosjekt i IBE160 Programmering med KI ved Høgskolen i Molde, høsten 2026.

## Formål og gjeldende produktbrief

- **Bekreftet:** Produktet skal hjelpe studenter med å gjøre forelesningsnotater i tekst- eller PDF-format om til sammendrag, sentrale begreper og quiz med fasit. Briefen beskriver valg av sammendragslengde, quizvanskelighetsgrad og antall spørsmål.
- **Kilde:** [`../product-brief.md`](../product-brief.md) er gjeldende brief i repoet. Tilbakemeldingen omtaler den som repoets eneste brief.
- **Bekreftet:** Briefens v1-scope utelukker automatisk karaktersetting, Canvas-integrasjon, deling, langvarig prestasjonsanalyse, ekstern innhenting av materiale og betaling.

## Faglærerens tilbakemelding, 6. oktober 2026

- **Bekreftet:** [`../tilbakemelding-product-brief.md`](../tilbakemelding-product-brief.md) er datert 2026-10-06 og vurderer briefen som et godt utgangspunkt med justeringer.
- **Bekreftet:** Tilbakemeldingen peker på behov for større v1-omfang, målbare suksesskriterier og en plan for KI-tjeneste, kostnader/nøkkel og testmodus.
- **Bekreftet:** Den foreslår blant annet interaktiv quiz, lagring per emne/forelesning og kildehenvisning per spørsmål. Dette er forslag fra tilbakemeldingen, ikke vedtatte krav.
- **Bekreftet:** Den anbefaler faste testnotater med fasit, mock-svar for automatiske tester og at sensor skal kunne kjøre løsningen uten gruppens API-nøkkel.

## Krav og mulige utvidelser

### Bekreftet i gjeldende brief

- Notater skal kunne lastes opp eller limes inn som tekst/PDF.
- Applikasjonen skal generere sammendrag, begrepsliste og quiz med fasit.
- Brukeren skal kunne velge sammendragslengde, vanskelighetsgrad og antall spørsmål.
- Resultatet skal presenteres oversiktlig, og dokumentfeil skal gi tydelig tilbakemelding.

### Foreslått, ikke vedtatt

- Interaktiv quiz med svar, forklaring og poengsum.
- Lagring per emne eller forelesning.
- Kilde/avsnittshenvisning for quizspørsmål.
- Faste testnotater med forventede begreper og mock-svar.
- Testmodus med ferdige eksempelsvar slik at appen kan kjøres uten API-nøkkel.

### Uavklart

- Om interaktiv quiz, lagring og kildehenvisninger skal inngå i v1.
- Om quizen skal være flervalg, fritekst eller begge deler.
- Hvilken KI-tjeneste som skal brukes, hvordan nøkkel håndteres og hvem som dekker eventuell kostnad.
- Hvordan testmodus skal fungere.
- Teknologistakk, lagringsmodell og PDF-behandling.
- Konkrete målbare kriterier for kvalitet og kildebinding.

## Gjeldende utviklingsstatus

- **Bekreftet:** Repoet inneholder README, produktbrief og tilbakemelding. Ved opprettelsen av denne dokumentasjonen finnes det ingen applikasjonskode, PRD, arkitektur eller epics i repoet.
- **Bekreftet:** Git-historikken inneholder commits for initialisering, README, produktbrief og tilbakemelding. Promptene bak disse arbeidsøktene er ikke arkivert her.
- **Bekreftet (etter PROMPT 007):** BMAD BMM/Core v6.12.4 er installert i prosjektet og konfigurert for Codex CLI. Se [BMAD-status](bmad/WORKFLOW_STATUS.md).
- **Bekreftet:** Ingen applikasjonskode, PRD, arkitektur eller epics er lagt til som del av BMAD-installasjonen.

## Neste anbefalte steg

1. Gruppen avklarer hvilke foreslåtte utvidelser som skal inn i v1, quizformat, KI-tjeneste, testmodus og teknologistakk.
2. Oppdater produktbriefen med vedtatte valg og målbare suksesskriterier.
3. Bruk den installerte BMAD-konfigurasjonen til å utarbeide PRD/arkitektur og planlegge stories når gruppen er klar.
4. Legg til testnotater først når gruppen har laget og godkjent dem; ikke bruk kursbeskyttet materiale uten avklaring.

## Observert status – 2026-10-23

Skrivebeskyttet kontroll gjennomført 2026-10-23 kl. 22:35 Europe/Oslo. PR-status ble kontrollert på nytt via `gh pr view 1 --json state,baseRefName,headRefName,headRefOid,updatedAt,url` kl. 22:35 Europe/Oslo (GitHub `updatedAt`: 2026-10-23T18:46:07Z; [PR #1](https://github.com/IBE160-2026/G27-isum-vijai/pull/1)).

Oppfølgende skrivebeskyttet PR-kontroll gjennomført 2026-10-24 kl. 16:23 Europe/Oslo. PR #1 var fortsatt `OPEN`, base `main`, head `feature/023-local-text-processing`, head-SHA `89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503`; GitHub `updatedAt` var fortsatt `2026-10-23T18:46:07Z` ([PR #1](https://github.com/IBE160-2026/G27-isum-vijai/pull/1)).

- **`main`:** baseline `444135e946b5635c812a24d44037c80fbf815e45`. På dette snapshotet finnes prototypens seks automatiserte tester i `tests/test_generator.py`; funksjonene og begrensningene per testcase er kartlagt i [testplanen](testing/TEST_PLAN.md).
- **`main`-prototyp (PROMPT 022):** Streamlit med norsk UI og lokale demonstrasjonsdata; resultatet er ikke ekte KI-generering.
- **PR #1:** åpen, base `main`, head-branch `feature/023-local-text-processing`, head `89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503` ([PR #1](https://github.com/IBE160-2026/G27-isum-vijai/pull/1)). PROMPT 023 legger lokal tekstbehandling uten KI til, mens quiz fortsatt vises som demo. Endringene og de tilhørende 15 testene tilhører dette PR-snapshotet, ikke `main` før merge.
- **Testbevis:** den dokumenterte 15-testkjøringen fant sted 2026-10-23 før head-committen ble opprettet, på arbeidsfila som senere ble commit `89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503`. Kommando og arbeidsmappe er ført fra PROMPT 023-samtalehistorikken i [testloggen](testing/TEST_LOG.md). Klokkeslett og separat rå pytest-utskrift er ikke bevart. Ingen separat manuell kontroll er dokumentert.
- **PRD og beslutninger:** PRD-en forblir `draft`. DEC-001–DEC-005 forblir `Uavklart`; denne statuskontrollen endrer ikke beslutningsstatus.
- **Etter merge:** gjennomgå og rydde opp i `_bmad-output/implementation-artifacts/deferred-work.md` når fila er tilgjengelig i det felles repositoryet. PROMPT 024 oppretter eller kopierer ikke fila.

## Observert status – 2026-10-25

Skrivebeskyttet kontroll av PR #1 ble gjort 2026-10-25 kl. 01:00 Europe/Oslo (2026-10-24 kl. 23:00 UTC) med `gh pr view 1 --json state,baseRefName,headRefName,headRefOid,updatedAt,url`. Resultat: PR #1 er fortsatt `OPEN`, base `main`, head-branch `feature/023-local-text-processing`, head-SHA `89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503`; GitHub `updatedAt` er `2026-10-23T18:46:07Z`. PR-en er ikke merget ([PR #1](https://github.com/IBE160-2026/G27-isum-vijai/pull/1)).

- **`main`:** fortsatt knyttet til baseline `444135e946b5635c812a24d44037c80fbf815e45` i den separate main-worktreen. PROMPT 026 har ikke endret `main`.
- **Dokumentasjonsbranch:** `docs/024-test-traceability` står på samme baseline `444135e946b5635c812a24d44037c80fbf815e45`, med ucommittede PROMPT 024/025-endringer og PROMPT 026-dokumentasjonsendringer. Ingen commit er opprettet.
- **PROMPT 023:** endringene er fortsatt bare representert av PR #1-headen; de tilhører ikke `main` mens PR-en er åpen.
- **PRD og beslutninger:** PRD-status er fortsatt `draft`. DEC-001–DEC-005 står fortsatt `Uavklart`; ingen produktbeslutning ble endret.
- **Testproveniens:** PROMPT 026-kjøringen med ni beståtte tester gjelder dokumentasjonsbranchen og er ført i [testloggen](testing/TEST_LOG.md). De historiske 15 PROMPT 023-testene er fortsatt separat før-commit-evidens.

## Observert status – PROMPT 024/025 og PROMPT 026-ferdigstilling (2026-10-25)

- **Branch:** `docs/027-documentation-completion`, branchen for den lokale dokumentasjonscommitten.
- **Storystatus:** PROMPT 024/025 og PROMPT 026 er `done` etter BMAD Build Step 05. PRD er fortsatt `draft`; DEC-001–DEC-005 er fortsatt `Uavklart`.
- **GitHub:** Konto `Abenagit` har push-rettighet til `IBE160-2026/G27-isum-vijai`. Endringene er ikke pushet; ingen separat PR for denne dokumentasjonsbranchen er opprettet.
- **Uendret referanse:** `main` er fortsatt `444135e946b5635c812a24d44037c80fbf815e45`; PR #1 er fortsatt `OPEN`, base `main`, head `feature/023-local-text-processing` på `89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503` (kontrollert 2026-10-25). PROMPT 023 er ikke merget.
- **Teststatus:** Hele lokale pytest-suiten består med ni tester; historisk PROMPT 023-kjøring på 15 tester er fortsatt separat før-commit-evidens.


- **Oppdatert 2026-11-15 – manuell tekstgenerering:** Brukeren bekreftet vellykket Gemini E2E-generering av sammendrag, tre begreper og tre relevante firevalgsoppgaver fra syntetiske prosjektledelsesnotater med lokal overstyring `gemini-3.5-flash-lite` på port 8503. Quizretting/poeng og PDF gjennom Gemini er ikke manuelt verifisert. UI ber som standard om fem; generatoren tillater færre dersom notatene ikke støtter flere og viser faktisk antall. Ingen skjult grense på tre eller etterfølgende quizfilter ble funnet. Det eksakte modellvalget mellom tre og fem kan ikke rekonstrueres uten responsdata. Se `docs/testing/TEST_LOG.md`.


- **Sluttkontroll Sprint 002 (2026-11-15):** Brukeren rapporterte teksttest med `gemini-3.5-flash-lite` på port 8503: relevant sammendrag/begreper, fire av fem spørsmål og 4/4 riktige; en eldre 0/4-test mangler dokumentasjon av valgte svar. Brukeren rapporterte også PDF `testnotater_informasjonssystemer_databaser.pdf` med fungerende opplasting/uttrekk, relevant Gemini-sammendrag, tre begreper, tre av fem spørsmål og quizresultat 1/3 med fasit/forklaringer som samsvarte. Resultatene er brukeroppgitte. Kildens standard er fortsatt `gemini-2.5-flash`; `gemini-3.5-flash-lite` er prosesslokal override. Full pytest: 83 bestått; diff-check bestod. Sprintens manuelle hovedflyter er rapportert testet; færre spørsmål enn ønsket følger kildegrunningsregelen.


- **Prompt-historikkontroll (2026-11-15):** PROMPT-loggene er sammenlignet skrivebeskyttet mellom originalmappen og Gemini-worktreen. Den aktive Gemini-loggen inneholder PROMPT 001–026 og 028; PROMPT 027 er fortsatt udokumentert. 26 nummererte ID-er har full tekst i tilgjengelige arkiver, mens PROMPT 019 er personvernredigert. Åtte senere ordrette brukerbeskjeder er lagt i unummerert arkiv. Fire grupper av eldre post-028 arbeid mangler fortsatt originalprompter og står som rekonstruerte sammendrag. Ingen unik original PROMPT 028-tekst manglet i Gemini-kopien. Originalmappen ble ikke endret; `.memlog.md` og Secrets ble ikke åpnet. Historikken er komplett bare for tilgjengelige og kontrollerte kilder. Detaljer: `docs/prompts/PROMPT_HISTORY_GAPS.md`.


### MVP Sprint 002 – modellstandard og tilstandsherding (2026-11-16)

- Gemini-adapterens fallback er `gemini-3.5-flash-lite`; `GEMINI_MODEL` og eksplisitt modellargument overstyrer fortsatt standarden. Ingen nøkkel eller Secret er endret eller lest.
- Gemini-notater begrenses til samme 1 000 000 tegn som lokalt PDF-uttrekk. Tomme quizresponser avvises; Streamlit har i tillegg en trygg tom-quizvakt.
- Notat-/PDF- og modusendringer tømmer resultat og quizfeedback og nullstiller Gemini-samtykke. Lengde-, vanskelighets- og antallsendringer tømmer resultat, quizfeedback og svarvalg; ny generering rydder også forrige quiztilstand.
- Lokal modus, PDF-grensene, kildebevisvalidering og personvernadvarselen består. Ingen eksternt kall ble gjort.
- PROMPT 001–026 og 028 er bevart, PROMPT 027 forblir gap, og `PROMPT_HISTORY_GAPS.md` er uendret. DEC-003 er fortsatt uavklart om godkjenning, kostnad, dataflyt og oppbevaring.
- Verifisering: målrettet suite 79 bestått; dokumentasjonstester 5 bestått; full pytest 99 bestått; `git diff --check` bestod.


### DEC-003 – avgrenset prototypegodkjenning (2026-11-16)

- **A. Godkjent prototypebruk:** Valgfri Gemini-bruk bare med syntetiske, offentlige eller anonymiserte notater uten personopplysninger eller konfidensielt innhold. Samtykke og brukerstart kreves; lokal modus skal virke uten Gemini; ingen nøkler/Secrets i Git.
- **B. Ikke godkjent:** Produksjonsbruk med personopplysninger eller konfidensielt innhold.
- **C. Krever ny beslutning:** Produksjonsbruk, kostnadsansvar, dokumentert leverandørdataflyt/lagring/sletting, nye datakategorier og eventuelle emne-/institusjonskrav. Beslutningen er ikke juridisk eller institusjonell godkjenning.
- Gjeldende Google-vilkår og emnekrav må følges; ingen garanti gis om gratis bruk, lagringstid eller sletting uten dokumentasjon. Se `docs/decisions/DECISION_LOG.md`.


### Retrospektiv sluttrevisjon (2026-11-16)

- Arbeidstråden `chore/ibe160-final-quality-audit` er basert på `origin/main` `fef77e85f078b6e5ecdb82f09a903b8a6a1d4fc1`, separat fra tidligere worktrees.
- Tre syntetiske cases er lagt til. Full pytest: 108 bestått; docs tests: 5 bestått; Python 3.12 clean install og Streamlit healthcheck 200 uten API-nøkkel; ingen eksterne Gemini-kall.
- `docs/audit/` oppsummerer kilder, krav, lærerfeedback, testbevis og innleveringsbegrensninger. Den fullstendige oppgaveteksten/sensorveiledningen ble ikke funnet og står NOT VERIFIED.
- PROMPT 027, rekonstruerte eldre aktivitetsgrupper og manglende ordrett PROMPT 029-transkripsjon er ikke fremstilt som fullstendige; se promptarkivets gapregister.
