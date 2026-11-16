# Unummererte Codex-oppfølginger – 16. november 2026

Disse oppføringene bevarer brukerens ordrette prompt uten å tildele historisk promptnummer.

## MVP Sprint 002 – Godkjent modellendring og kvalitetssikring

```text
# MVP Sprint 002 – Godkjent modellendring og kvalitetssikring

Arbeid kun i:
/private/tmp/G27-isum-vijai-mvp-002-gemini

Branch: feature/mvp-002-gemini-ai

Jeg godkjenner at standardmodellen endres fra gemini-2.5-flash til gemini-3.5-flash-lite.

Behold GEMINI_MODEL som miljøvariabel for overstyring.

## 1. Modellendring

- Endre standardmodellen til gemini-3.5-flash-lite.
- Oppdater relevante tester og dokumentasjon.
- Bevar lokal modus.
- Ikke endre API-nøkkel eller Secrets.
- Ikke utfør eksterne Gemini-kall.

## 2. Gjennomgå kvalitetsfunnene

Undersøk følgende:
- Gjenbruk av samtykke etter endring av notater.
- Gamle quizresultater ved ny generering.
- Lange notater og tekstgrenser.
- Tom quiz med null spørsmål.
- Personvernbeslutningen DEC-003.
- Dokumentasjonstestenes dekning av prompt-historikken.

For hvert funn:
1. Forklar hvordan problemet kan oppstå.
2. Vurder konsekvensen.
3. Rett konkrete feil som kan løses trygt innenfor Sprint 002.
4. Legg til regresjonstester.
5. Ikke endre produktbeslutninger eller personvernregler uten å rapportere behovet for godkjenning.

## 3. BMAD-dokumentasjon

Oppdater relevante:
- CODEX_PROMPT_LOG.md
- CHANGELOG_PROCESS.md
- PROJECT_CONTEXT.md
- TEST_LOG.md
- WORKFLOW_STATUS.md
- Sprint 002-spesifikasjonen

Bevar PROMPT_HISTORY_GAPS.md og all tidligere prompt-historikk.

## 4. Verifisering

Kjør:
- Full pytest
- Dokumentasjonstester
- git diff --check

Kontroller at ingen sensitive filer inngår i endringene.

## 5. Git-begrensninger

- Ikke les, endre eller stage .memlog.md.
- Ikke les eller vis Secrets eller API-nøkler.
- Ikke endre originalarbeidsmappen.
- Ikke utfør eksterne Gemini-kall.
- Ikke commit.
- Ikke push.
- Ikke merge PR #5.

## 6. Rapport

Rapporter:
- Hvilke konkrete feil som ble funnet og rettet.
- Hvilke funn som fortsatt er åpne.
- Om standardmodellen er endret.
- Testresultater.
- Endrede filer.
- Om PR #5 er klar for en ny gjennomgang.

Stopp etter rapporten og vent på godkjenning før Git-operasjoner.
```

## IBE160 – Fullfør Sprint 002, DEC-003 og PR #5

```text
# IBE160 – Fullfør Sprint 002, DEC-003 og PR #5

Arbeid kun i:
/private/tmp/G27-isum-vijai-mvp-002-gemini

Branch:
feature/mvp-002-gemini-ai

PR:
https://github.com/IBE160-2026/G27-isum-vijai/pull/5

Jeg ønsker å ferdigstille MVP Sprint 002.

## 1. Avklar DEC-003

Dokumenter følgende prosjektbeslutning:

Gemini godkjennes for valgfri bruk i prosjektets prototype, begrenset til syntetiske, offentlige eller anonymiserte notater som ikke inneholder personopplysninger eller konfidensielt innhold.

Forutsetninger:
- Aktivt samtykke før ekstern behandling.
- Brukeren må selv starte generering.
- Lokal modus skal fungere uten Gemini.
- Ingen API-nøkler eller Secrets i Git.
- Tydelig informasjon om at notatinnhold sendes til Google.
- Ingen garanti om gratis bruk, datalagring eller sletting uten dokumentasjon.
- Gjeldende leverandørvilkår og eventuelle emnekrav må respekteres.
- Produksjonsbruk med personopplysninger er ikke godkjent.

Skill tydelig mellom:
A. Godkjent prototypebruk.
B. Ikke-godkjent produksjonsbruk.
C. Forhold som krever ny beslutning.

Ikke påstå at det foreligger juridisk eller institusjonell godkjenning.

## 2. Sluttkontroll av Sprint 002

Kontroller:
- Standardmodell gemini-3.5-flash-lite.
- GEMINI_MODEL-overstyring.
- Samtykke og tilbakestilling ved endring av innhold.
- Lokal modus.
- Tekst og PDF.
- Quiz, fasit og poengberegning.
- Håndtering av tomme resultater og lange notater.
- Kildevalidering.
- Feilhåndtering.
- Ingen eksponering av API-nøkler.

Ikke utfør eksterne Gemini API-kall.

## 3. Dokumentasjon

Oppdater relevante BMAD-dokumenter, beslutningslogg, README, TEST_LOG, WORKFLOW_STATUS og CODEX_PROMPT_LOG.

Bevar hele eksisterende prompt-historikken og dokumenterte hull.

Registrer DEC-003 med dato, beslutning, begrunnelse, begrensninger og konsekvenser.

## 4. Tester

Kjør:
- Full pytest.
- Dokumentasjonstester.
- git diff --check.

Kontroller at alle relevante filer er inkludert.

## 5. Git

Hvis alle tester består og ingen kritiske feil gjenstår:

- Stage kun relevante Sprint 002-filer.
- Kontroller staged diff og filnavn.
- Commit med melding:
  docs: approve restricted Gemini prototype use in DEC-003
- Push til eksisterende feature-branch.
- Bekreft at PR #5 er oppdatert og fortsatt MERGEABLE/CLEAN.

Ikke bruk force push.
Ikke opprett ny PR.
Ikke merge ennå.

## 6. Sikkerhet

Ikke les, endre eller stage .memlog.md.
Ikke les eller vis Secrets eller API-nøkler.
Ikke inkluder .venv.
Ikke endre originalarbeidsmappen.
Ikke utfør eksterne Gemini-kall.

## 7. Sluttrapport

Oppgi:
- Status for DEC-003.
- Eventuelle gjenstående begrensninger.
- Testresultater.
- Commit-SHA.
- Push-status.
- PR #5-status.
- Om PR-en er klar for merge.

Stopp etter rapporten. Ikke merge uten en egen bekreftelse.
```

## IBE160 – Fullfør Sprint 002, DEC-003 og PR #5

```text
# IBE160 – Fullfør Sprint 002, DEC-003 og PR #5

Arbeid kun i:
/private/tmp/G27-isum-vijai-mvp-002-gemini

Branch:
feature/mvp-002-gemini-ai

PR:
https://github.com/IBE160-2026/G27-isum-vijai/pull/5

Jeg ønsker å ferdigstille MVP Sprint 002.

## 1. Avklar DEC-003

Dokumenter følgende prosjektbeslutning:

Gemini godkjennes for valgfri bruk i prosjektets prototype, begrenset til syntetiske, offentlige eller anonymiserte notater som ikke inneholder personopplysninger eller konfidensielt innhold.

Forutsetninger:
- Aktivt samtykke før ekstern behandling.
- Brukeren må selv starte generering.
- Lokal modus skal fungere uten Gemini.
- Ingen API-nøkler eller Secrets i Git.
- Tydelig informasjon om at notatinnhold sendes til Google.
- Ingen garanti om gratis bruk, datalagring eller sletting uten dokumentasjon.
- Gjeldende leverandørvilkår og eventuelle emnekrav må respekteres.
- Produksjonsbruk med personopplysninger er ikke godkjent.

Skill tydelig mellom:
A. Godkjent prototypebruk.
B. Ikke-godkjent produksjonsbruk.
C. Forhold som krever ny beslutning.

Ikke påstå at det foreligger juridisk eller institusjonell godkjenning.

## 2. Sluttkontroll av Sprint 002

Kontroller:
- Standardmodell gemini-3.5-flash-lite.
- GEMINI_MODEL-overstyring.
- Samtykke og tilbakestilling ved endring av innhold.
- Lokal modus.
- Tekst og PDF.
- Quiz, fasit og poengberegning.
- Håndtering av tomme resultater og lange notater.
- Kildevalidering.
- Feilhåndtering.
- Ingen eksponering av API-nøkler.

Ikke utfør eksterne Gemini API-kall.

## 3. Dokumentasjon

Oppdater relevante BMAD-dokumenter, beslutningslogg, README, TEST_LOG, WORKFLOW_STATUS og CODEX_PROMPT_LOG.

Bevar hele eksisterende prompt-historikken og dokumenterte hull.

Registrer DEC-003 med dato, beslutning, begrunnelse, begrensninger og konsekvenser.

## 4. Tester

Kjør:
- Full pytest.
- Dokumentasjonstester.
- git diff --check.

Kontroller at alle relevante filer er inkludert.

## 5. Git

Hvis alle tester består og ingen kritiske feil gjenstår:

- Stage kun relevante Sprint 002-filer.
- Kontroller staged diff og filnavn.
- Commit med melding:
  docs: approve restricted Gemini prototype use in DEC-003
- Push til eksisterende feature-branch.
- Bekreft at PR #5 er oppdatert og fortsatt MERGEABLE/CLEAN.

Ikke bruk force push.
Ikke opprett ny PR.
Ikke merge ennå.

## 6. Sikkerhet

Ikke les, endre eller stage .memlog.md.
Ikke les eller vis Secrets eller API-nøkler.
Ikke inkluder .venv.
Ikke endre originalarbeidsmappen.
Ikke utfør eksterne Gemini-kall.

## 7. Sluttrapport

Oppgi:
- Status for DEC-003.
- Eventuelle gjenstående begrensninger.
- Testresultater.
- Commit-SHA.
- Push-status.
- PR #5-status.
- Om PR-en er klar for merge.

Stopp etter rapporten. Ikke merge uten en egen bekreftelse.
```
