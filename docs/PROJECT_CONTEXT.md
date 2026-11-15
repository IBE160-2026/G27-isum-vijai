# Prosjektkontekst

## Gjeldende status – PROMPT 028 publisert i PR #3 (2026-11-15)

- **Publisert arbeid:** PROMPT 028-integreringen etter PR #2 er committet som `ec19c95a63e169ab90174abb2299bbdaba1ed357` på `docs/028-product-brief-alignment-post-pr2` og publisert i [PR #3](https://github.com/IBE160-2026/G27-isum-vijai/pull/3). Dokumentasjonsarbeidet er gjennomført, men PR #3 er ikke merget.
- **Sist verifiserte PR-status:** 2026-11-15 kl. 10:09:30 UTC: `OPEN`, base `main`, head `ec19c95a63e169ab90174abb2299bbdaba1ed357`, `MERGEABLE`. Ingen automatiske CI-checks var rapportert (`statusCheckRollup: []`). Statusen er fra før denne loggoppdateringen og skal ikke leses som en etterfølgende live-kontroll.
- **Avventer:** Gruppens gjennomgang og godkjenning før eventuell merge. PR #2 er merget i `1227fb443e52815f831b3f5720b4f41844f72ad0`; PR #3 er fortsatt åpen.
- **Produkt/BMAD:** Product Brief Validate er ikke fullført. PRD er fortsatt `draft`, og DEC-001–DEC-005 er fortsatt åpne. Bare den lokale PROMPT 028-integreringsoppgaven er fullført; PR-gjennomgang og merge gjenstår.

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
