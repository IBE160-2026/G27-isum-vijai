# PROMPT 031 – Endelig ferdigstilling av G27-prosjektet

- **Dato:** 2026-11-16.
- **Formål:** Sluttkontrollere PR #7, bevare refleksjonsutkastet, kontrollere promptarkiv og innleveringskrav, og merge PR-en hvis GitHub-kontroller tillater det.
- **Kilde:** Full brukerprompt fra denne Codex-samtalen; originalteksten er nedenfor i en `text`-fence.
- **Branch/worktree:** `chore/ibe160-final-quality-audit`, `/private/tmp/G27-isum-vijai-final-audit`.
- **Resultat/filer/tester/commit/PR:** Oppdateres etter gjennomføring.

## Original prompt

```text
# IBE160 – ENDELIG FERDIGSTILLING AV G27-PROSJEKTET

## HOVEDOPPDRAG

Du skal fullføre den tekniske prosjektleveransen for IBE160, gruppe G27, og klargjøre det som gjenstår før endelig innlevering.

Repository:
IBE160-2026/G27-isum-vijai

Pull Request:
https://github.com/IBE160-2026/G27-isum-vijai/pull/7

Branch:
chore/ibe160-final-quality-audit

Prosjekt:
Foredragsnotater → Sammendrag & Quizgenerator

Arbeid systematisk og gjennomfør alle trygge oppgaver uten å stoppe etter planlegging.

## 1. SIKKERHET

Finn riktig arbeidsmappe med `git worktree list`.

Arbeid bare i den separate PR #7-worktreen.

Ikke endre originalmappen:
~/Downloads/G27-isum-vijai

Ikke endre tidligere Gemini-worktree.

Ikke les eller endre:
- .memlog.md
- .streamlit/secrets.toml
- API-nøkler eller private .env-filer.

Ikke kjør ekte Gemini API-kall.

Ikke bruk force push.

Ikke slett historikk.

Ikke overskriv eksisterende arbeid.

## 2. BEVAR REFLEKSJONSUTKASTET

Eksisterende lokal fil:

/private/tmp/G27-isum-vijai-final-audit/docs/audit/REFLECTION_REPORT_GROUP_DRAFT.md

Denne filen er bevisst ucommittet og holdt utenfor PR #7.

Ikke slett eller overskriv filen.

Ikke legg den til PR #7.

Kontroller at den fortsatt finnes, uten å endre innholdet.

Rapporter filens status.

## 3. KONTROLLER PROMPTARKIVET

Kontroller:

docs/CODEX_PROMPT_LOG.md

docs/prompts/

docs/prompts/PROMPT_HISTORY_GAPS.md

Undersøk spesielt PROMPT 029 og den siste oppfølgingsprompten.

Kontroller om PROMPT 029 faktisk er arkivert ordrett.

Hvis originalteksten ikke er tilgjengelig, marker det tydelig.

Ikke fabriker manglende originaltekster.

Bevar PROMPT 027 og eldre historiske hull som dokumenterte begrensninger.

Loggfør også denne prompten etter prosjektets eksisterende nummerering dersom originalteksten er tilgjengelig.

Ikke påstå fullstendig arkivering uten bevis.

## 4. SLUTTKONTROLL AV PR #7

Kontroller:

- Alle commits.
- Alle endrede filer.
- GitHub-status.
- Mergekonflikter.
- Tester.
- Dokumentasjon.
- README.
- BMAD.
- Promptlogging.
- Sikkerhet.
- Testdata.

Tidligere rapporterte resultater:
108 automatiserte tester og 5 dokumentasjonstester.

Kjør relevante tester på nytt.

Kjør `git diff --check`.

Kontroller at ingen hemmeligheter eller utilsiktede filer blir inkludert.

Hvis konkrete feil finnes, rett dem på PR-branchen, test på nytt og push endringene.

## 5. FULLFØR PR #7

Når følgende er bekreftet:

- PR-en er mergebar.
- Alle nødvendige tester består.
- Ingen kritiske feil er åpne.
- Ingen hemmeligheter er inkludert.
- Promptarkivet er korrekt dokumentert.
- Refleksjonsutkastet er utenfor PR-en.

Da skal du:

1. Bekrefte at PR #7 fortsatt peker mot riktig `main`.
2. Kontrollere GitHub-checks og eventuelle branch protection-regler.
3. Merge PR #7 med vanlig godkjent merge-metode.
4. Ikke bruk force merge eller omgå beskyttelsesregler.
5. Bekreft merge-commit og oppdatert `origin/main`.
6. Kontroller at endringene faktisk finnes på `main`.
7. Kjør relevante tester på en ren checkout av oppdatert `main`.

Hvis GitHub krever manuell godkjenning eller merge ikke er trygt, stopp og rapporter hvorfor.

## 6. REFLEKSJONSRAPPORT – GRUPPE

Den offentlige emnebeskrivelsen for IBE160 høsten 2026 oppgir:

- Prosjektkode, funksjonalitet og KI-/kvalitetssikringsdokumentasjon: 70 %.
- Gruppevis refleksjonsrapport: 30 %.

Refleksjonsrapporten skal omhandle:

- Utviklingsprosessen.
- Utfordringer og løsninger.
- Hvordan KI påvirket arbeidet.
- Etiske og teknologiske implikasjoner.

Undersøk om den fullstendige oppgaveteksten eller rapportinstruksjonene finnes i tilgjengelige prosjektfiler.

Hvis de finnes, bruk dem.

Hvis de ikke finnes, dokumenter at gruppen må hente dem fra emneplattformen.

Ikke gjett rapportens lengde, format eller leveringskanal.

Bruk eksisterende refleksjonsdisposisjon som grunnlag for en forbedret, sammenhengende rapport dersom den inneholder tilstrekkelig dokumentert informasjon.

Rapporten skal være faktabasert og skille mellom:

- Dokumenterte prosjektaktiviteter.
- Dokumenterte beslutninger.
- Gruppens refleksjoner som må bekreftes.
- Manglende informasjon.

Ikke finn på møter, arbeidsfordeling, opplevelser eller læringsutbytte.

Ikke publiser refleksjonsrapporten på GitHub uten gruppens uttrykkelige godkjenning.

Bevar rapporten lokalt og separat fra PR #7.

## 7. SLUTTRAPPORT

Gi en fullstendig rapport på norsk.

Rapporter:

1. Om PR #7 ble merget.
2. Merge-commit.
3. Oppdatert main-commit.
4. Faktiske testresultater etter merge.
5. Status for README.
6. Status for BMAD.
7. Status for promptarkivet.
8. Status for PROMPT 029.
9. Historiske prompt-hull.
10. Status for refleksjonsrapporten.
11. Status for formelle innleveringskrav.
12. Eventuelle gjenstående feil.
13. Hva gruppen må gjøre manuelt.

Svar eksplisitt:

- Er den tekniske MVP-en ferdig?
- Er den tekniske leveransen på main?
- Kan sensor demonstrere appen uten API-nøkkel?
- Er dokumentasjonen konsistent?
- Er refleksjonsrapporten ferdig?
- Er hele IBE160-innleveringen klar?

Ikke marker hele innleveringen som ferdig dersom rapporten eller formelle krav fortsatt mangler.

## START NÅ

Begynn med Git-status, kontroll av PR #7 og bevaring av refleksjonsutkastet.

Gjennomfør alle trygge steg.

Merge PR #7 bare når alle sikkerhets- og kvalitetskontroller er oppfylt.

Deretter kontrollerer du oppdatert main og rapporterer nøyaktig hva som fortsatt gjenstår før innlevering.
```
