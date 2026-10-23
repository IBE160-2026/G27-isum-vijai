# BMAD-status

Kontrollert 2026-10-18. Den første kontrollen nedenfor dokumenterer funnene før installasjon; PROMPT 007-oppdateringen dokumenterer den senere installasjonen.

## Før installasjon

- **Bekreftet:** Ingen BMAD-runtime, agentdefinisjoner eller arbeidsflytressurser ble funnet i repoet.
- **Bekreftet:** Codex-miljøet hadde eldre BMAD-relaterte promptfiler i `~/.codex/prompts/`, men ikke prosjektets BMAD-runtime.
- **Bekreftet:** Repoet hadde ikke PRD, arkitektur eller epics ifølge faglærerens tilbakemelding.

## PROMPT 007 – installasjon og verifisering

- **Bekreftet:** BMad Method v6.12.4 er installert. Manifestet [manifest.yaml](../../_bmad/_config/manifest.yaml) viser `core` og `bmm` på 6.12.4 og `codex` som konfigurert IDE.
- **Bekreftet:** Codex-ferdighetene ligger i `../../.agents/skills/`. Codex CLI 0.163.0 oppdaget og lastet `bmad-help`; en ny skrivebeskyttet Codex-kjøring bekreftet 29 skills i prosjektmanifestet.
- **Bekreftet:** BMad sin `resolve_config.py` resolver kjørte og returnerte konfigurasjon samt BMM-agentdefinisjoner.
- **Bekreftet:** Agentene er Analyst, Architect, Dev, PM og UX Designer.
- **Bekreftet:** BMM-plan-/arbeidsflytskills inkluderer Product Brief, PRD, Architecture, UX, Spec, Epics and Stories, Sprint Planning, Build, Code Review, Correct Course, QA E2E, Retrospective, Walkthrough, PRFAQ og Project Context. Core inneholder blant annet Help, Brainstorming, Party Mode, Review og Customize.
- **Uavklart:** Eldre globale promptfiler i `~/.codex/prompts/` er fortsatt til stede. Installereren varslet at de kan gi dupliserte kommandoer og anbefalte manuell fjerning; de ble ikke endret i denne oppgaven.

## Neste aktuelle fase

**Foreslått:** Avklar v1-scope og åpne beslutninger i [beslutningsloggen](../decisions/DECISION_LOG.md), oppdater produktbriefen når gruppen har vedtatt endringer, og bruk deretter BMM-planleggingsskills som PRD og Architecture. Ingen PRD, arkitektur eller epics er opprettet gjennom installasjonen.

## PROMPT 021 – PRD

- **Dato:** 2026-10-23.
- **BMAD-arbeidsflyt:** Prosjektets `bmad-prd`-skill (BMM PRD). Konfigurasjonen løser PRD-utdata til `_bmad-output/planning-artifacts/prds/prd-G27-isum-vijai-2026-10-23/`.
- **BMAD-agentrolle:** PM (John, Product Manager) for krav- og PRD-arbeidet. Arkitektur- og teknologivalg er ikke gjort.
- **Status:** BMM PRD-forfatting og kvalitetsgjennomgang er gjennomført; PRD-en står som `draft` fordi nødvendige produkt- og teknologivalg fortsatt mangler gruppevedtak. BMAD-rubrikken vurderte den som adekvat, men ikke implementeringsklar før åpne grenser og akseptansekriterier er avklart. PRD-en skiller mellom krav fra Product Brief, lærerens forslag og gruppens uavklarte valg.
- **Artefakter:** `prd.md`, `addendum.md` (ikke-bindende teknologistakkvurdering), `.memlog.md` og `review-rubric.md` i PRD-mappen. Ingen PRD, arkitektur eller epics fantes før denne arbeidsøkten.
- **Uavklart før implementasjon:** Quizinteraksjon, lagring, KI-tjeneste/nøkkel/kostnad, testmodus, teknologistakk, quizformat og -grenser, målbare kriterier for kildebinding og eventuell OCR. Se PRD §9 og [beslutningsloggen](../decisions/DECISION_LOG.md).

## PROMPT 022 – Første prototype

- **Dato:** 2026-10-23.
- **Arbeidsflyt:** BMM Build (`bmad-build`), one-shot for en liten, avgrenset prototype.
- **Prototypvalg:** Python og Streamlit for UI, lokal deterministisk mock for resultatene, pytest-kompatible tester. Dette følger den uttrykkelige prototypetillatelsen i PROMPT 022; det er ikke et endelig produksjonsarkitekturvedtak og endrer ikke DEC-005.
- **Omfang:** Tekstinput, feilhåndtering, mock-sammendrag/begreper/quiz og lokal quizbesvarelse. Ingen PDF-uttrekk, ekstern KI, API-nøkkel eller lagring.
- **Verifisering:** Python 3.12 ble brukt i et isolert `.venv`. Etter godkjent installasjon av `requirements.txt` bestod pytest med 6 tester, og unittest-kjøringen bestod med 6 tester. `compileall` bestod. Streamlit startet kun på `127.0.0.1:8765`, og helsesjekken på `/_stcore/health` returnerte `ok`; lokal HTTP-server ble stoppet etter kontroll. Ingen ekstern KI eller API-nøkkel er brukt. Eksisterende PRD-`.memlog.md` ble ikke endret.
- **Avgrensninger:** PDF-uttrekk, ekstern KI, lagring og produksjonsarkitektur er ikke implementert. Denne prototypen avgjør ikke de åpne gruppespørsmålene i DEC-001–DEC-005.

## PROMPT 023 – Lokal tekstbehandling

- **Dato:** 2026-10-23.
- **Arbeidsområde:** Separat worktree `/private/tmp/G27-isum-vijai-prompt023`, branch `feature/023-local-text-processing`, basert på `444135e946b5635c812a24d44037c80fbf815e45`. Opprinnelig prosjektmappe og dens `.memlog.md` ble ikke endret.
- **Brukt BMAD-agent/arbeidsflyt:** BMM Build (`bmad-build`) one-shot via faktisk renderet skillflyt; utviklerrollen Amelia (`bmad-agent-dev`) ble aktivert og konfigurasjonen løst. BMM Code Review (`bmad-code-review`) ble kjørt i `full`-modus mot implementeringsdiffen og den nye story-spesifikasjonen.
- **Brukerhistorie:** Studenten får et enkelt lokalt utdragssammendrag og hyppige begreper fra innlimte forelesningsnotater. Quiz beholdes som tydelig merket demonstrasjonsdata.
- **Akseptansekriterier:** Resultatsammendraget består av setninger fra notatene; begreper velges fra kildeord med stabil rangering; tom/ugyldig input gir kontrollert valideringsfeil; UI skiller lokal behandling fra KI og demoquiz; eksisterende interaktiv quiz fungerer.
- **Review-lag:** Blind Hunter, Verification Gap Reviewer og Acceptance Auditor fullførte. Edge Case Hunter returnerte tomt resultat og ble registrert som mislykket lag etter Code Review-regelen for tomme svar. I post-fix-pass fant Blind Hunter, Verification Gap Reviewer og Edge Case Hunter nye patchpunkter; Acceptance Auditor bekreftet utsatt quizgap. Reviewens obligatoriske valgpunkt for patcher er nådd, og storystatus er `in-progress` mens funnene avventer brukerens valg.
- **Reviewfunn:** Funn om setningsrangering, norske fyllord og manglende UI-regresjonstester ble rettet og testet. To Blind Hunter-funn ble avkreftet. PRD-kravet om quiz fra notatene er ikke implementert, i tråd med brukerens avgrensning; det er registrert som utsatt arbeid.
- **Tester:** `pytest -q -p no:cacheprovider`: 14 bestått. `compileall` og `git diff --check` bestod. Streamlit AppTest kontrollerte faktiske resultater, etiketter, demoquiz, tom begrepsliste og tom input.
- **Status etter godkjent review-oppfølging:** Funn 1 og 2 ble rettet med AppTest-dekning for kildebasert sammendrag og quizinnsending/tilbakemelding. Funn 3–7 er ført som utsatte forbedringer i spesifikasjonen og `deferred-work.md`, uten kodeendring. Hele pytest-pakken består med 15 tester. Storyen er `done` for godkjent omfang; reviewbegrensningen med Edge Case Hunter som ga tomt svar i første pass står fortsatt. PRD-kravet om notatbasert quiz er utsatt. Ingen commit, push eller overføring til opprinnelig prosjektmappe.
