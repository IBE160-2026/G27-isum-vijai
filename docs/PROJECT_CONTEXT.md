# Prosjektkontekst

Oppdatert: 2026-10-18

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
