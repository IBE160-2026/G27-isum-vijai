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
