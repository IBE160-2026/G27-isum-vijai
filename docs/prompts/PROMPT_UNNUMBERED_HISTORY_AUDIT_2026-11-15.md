# Unummerert brukeroppdrag – kontroll av Codex-prompt-historikk (2026-11-15)

Originalprompten nedenfor er kopiert ordrett fra brukermeldingen i denne Codex-samtalen. Den har ikke fått et historisk PROMPT-nummer.

---

# KRITISK DOKUMENTASJONSKONTROLL – GJENOPPRETT KOMPLETT CODEX-PROMPT-HISTORIKK

## Arbeidsområde

Arbeid kun i:

/private/tmp/G27-isum-vijai-mvp-002-gemini

Branch:
feature/mvp-002-gemini-ai

## PROBLEM

Vi har oppdaget at docs/CODEX_PROMPT_LOG.md ikke inneholder alle Codex-promptene vi tidligere har brukt i IBE160-prosjektet.

Dette er et dokumentasjonsavvik som må undersøkes og rettes før Sprint 002 kan ferdigstilles.

Målet er å bevare en fullstendig, kronologisk og etterprøvbar prompt-historikk, uten tap av tidligere dokumentasjon.

## FASE 1 – SIKKERHET OG STATUS

1. Kontroller aktiv worktree og branch.
2. Kjør git status --short.
3. Undersøk eksisterende dokumentasjon uten å endre noe først.
4. Ikke overskriv eller nullstill eksisterende filer.
5. Ikke endre originalarbeidsmappen eller andre worktrees.
6. Ikke rør .memlog.md – ikke les, rediger, stage, slett eller commit den.
7. Ikke les eller loggfør API-nøkler eller Secrets.
8. Ikke push, merge eller opprett PR.

## FASE 2 – UNDERSØK HELE PROMPT-HISTORIKKEN

Undersøk relevante, tilgjengelige kilder:

- docs/CODEX_PROMPT_LOG.md
- docs/prompts/
- docs/CHANGELOG_PROCESS.md
- docs/PROJECT_CONTEXT.md
- docs/testing/TEST_LOG.md
- docs/testing/TEST_PLAN.md
- docs/bmad/
- docs/decisions/
- _bmad-output/implementation-artifacts/
- Git-historikk for relevante dokumentasjonsfiler
- Tidligere commits og mergehistorikk
- Tilgjengelige Codex-sessionlogger, dersom de kan undersøkes uten å lese .memlog.md eller hemmeligheter

Kontroller også dokumentasjon som er tilgjengelig gjennom Git-historikken fra tidligere integrerte branches.

Ikke anta at en prompt mangler bare fordi den ikke finnes i den nyeste versjonen av én fil.

Ikke bruk originalarbeidsmappen som skriveområde.

## FASE 3 – KONTROLLER PROMPT 001–028

Gjennomgå eksisterende promptnummerering.

For hvert nummer:

- Finnes prompten?
- Er originalteksten bevart?
- Er dato og formål dokumentert?
- Finnes tilhørende beslutninger eller endringer?
- Finnes commit eller PR som dokumenterer arbeidet?
- Er det hull, duplikater eller motstridende opplysninger?

PROMPT 028 skal kontrolleres spesielt mot:

docs/prompts/PROMPT_028_ANALYSIS.md
docs/prompts/PROMPT_028_APPROVAL.md

Bevar eksisterende originaltekst og tidligere historikk.

## FASE 4 – KONTROLLER SENERE PROMPTER

Undersøk alle tilgjengelige prompter etter PROMPT 028.

Inkluder spesielt:

- Dokumentasjonsarbeidet før PR #3.
- PDF MVP Sprint 001.
- PDF-testing og integrasjonsarbeid.
- Konfliktløsning ved PDF-merge.
- Gemini MVP Sprint 002.
- Implementering av Gemini SDK.
- API-nøkkel og Streamlit Secrets.
- Gemini-feil ved første manuelle generering.
- Forbedring av feilhåndtering.
- Isolering av tester fra lokale Secrets.
- Rotårsaksanalyse og diagnostikkoder.
- GEMINI-MODEL-feilen.
- Undersøkelse av modelltilgang.
- Denne dokumentasjonskontrollen.

Ta også med andre tilgjengelige prompter som ikke er nevnt her.

## FASE 5 – GJENOPPRETT DOKUMENTASJONEN

Oppdater docs/CODEX_PROMPT_LOG.md uten å miste eksisterende innhold.

For hver dokumentert prompt skal følgende registreres der informasjonen finnes:

1. Prompt-ID eller nummer.
2. Dato.
3. Formål.
4. Original prompttekst, eller en tydelig referanse til en bevart original.
5. Resultat.
6. Endrede filer.
7. Tester og verifisering.
8. Tilhørende commit/PR.
9. BMAD-status.
10. Kilde og verifiseringsstatus.

Dersom original prompttekst ikke kan gjenfinnes, skriv tydelig:

"Original prompttekst ikke gjenfunnet – rekonstruert sammendrag."

Ikke presenter rekonstruert tekst som et ordrett originalsitert prompt.

Ikke finn på datoer, commit-SHA-er, promptnummer eller testresultater.

Dersom tidligere prompter mangler, opprett en egen oversikt over manglende eller uverifiserte prompter.

Ikke renummerer historiske prompter uten å dokumentere og begrunne endringen.

## FASE 6 – GIT OG PR-HISTORIKK

Kontroller kjente milepæler mot tilgjengelig Git-historikk:

PR #3 – PROMPT 028-dokumentasjon.
PR #4 – PDF MVP Sprint 001.
Sprint 002 – Gemini, ennå ikke merget.

Kontroller relevante commit-SHA-er mot Git før de registreres.

Skill mellom:
- Lokalt utført arbeid.
- Lokalt committet arbeid.
- Pushet arbeid.
- Opprettet PR.
- Merget PR.

Ikke registrer en PR som merget uten verifisering.

## FASE 7 – BMAD OG DOKUMENTASJON

Oppdater ved behov:

docs/CODEX_PROMPT_LOG.md
docs/CHANGELOG_PROCESS.md
docs/PROJECT_CONTEXT.md
docs/testing/TEST_LOG.md
docs/bmad/WORKFLOW_STATUS.md

Registrer dokumentasjonsavviket, undersøkelsen, hva som ble gjenfunnet, og eventuelle gjenværende hull.

Bevar tidligere BMAD-arbeid og historikk.

## FASE 8 – VERIFISERING

Kontroller at:

- Eksisterende promptoppføringer ikke er slettet.
- PROMPT 001–028 er kontrollert.
- Senere tilgjengelige prompter er kontrollert.
- Kronologien er forståelig.
- Referanser til filer og commits er korrekte.
- Ingen API-nøkler eller Secrets er inkludert.
- Ingen duplikater er introdusert.
- Manglende originaltekster er tydelig merket.

Kjør relevante dokumentasjonstester og git diff --check.

## FASE 9 – SLUTTRAPPORT

Rapporter:

1. Hvor mange promptoppføringer som fantes før.
2. Hvor mange som finnes etter.
3. Hvilke prompter som ble gjenfunnet.
4. Hvilke prompter som fortsatt mangler.
5. Om PROMPT 001–028 er fullstendig dokumentert.
6. Om alle Sprint 001- og Sprint 002-prompter er registrert.
7. Hvilke dokumentasjonsfiler som ble endret.
8. Testresultater.
9. Eventuelle historiske avvik.
10. Om promptloggen nå kan regnes som komplett, eller bare komplett for tilgjengelige kilder.

IKKE COMMIT, PUSH, OPPRETT PR ELLER MERGE.

Vent på brukerens godkjenning etter sluttrapporten.
