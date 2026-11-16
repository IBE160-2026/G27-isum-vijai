# PROMPT 030 – Endelig ferdigstilling av PR #7 og innleveringsforberedelser

- **Dato:** 2026-11-16.
- **Formål:** Ferdigstille PR #7, sikre promptarkivet, kontrollere innleveringskrav og forberede refleksjonsrapport uten å merge.
- **Branch:** `chore/ibe160-final-quality-audit`.
- **Kilde/verifikasjon:** Brukerens fulle melding i Codex-økten er originalkilden. Denne filen inneholder en transkripsjon nedenfor.
- **Resultat/filer/tester/commit/PR:** Oppdateres etter gjennomføring.

## Original prompt

```text
# IBE160 – ENDELIG FERDIGSTILLING AV PR #7 OG INNLEVERINGSFORBEREDELSER

## OPPDRAG

Du skal fullføre de gjenværende oppgavene etter sluttrevisjonen av IBE160-prosjektet G27-isum-vijai.

Repository:
IBE160-2026/G27-isum-vijai

Eksisterende Pull Request:
https://github.com/IBE160-2026/G27-isum-vijai/pull/7

Arbeidsbranch:
chore/ibe160-final-quality-audit

Målet er å ferdigstille PR #7, sikre korrekt promptarkiv, kontrollere innleveringskravene og klargjøre eventuell refleksjonsrapport.

Dette er en gjennomføringsoppgave. Gjennomfør alle trygge, verifiserbare steg.

## 1. SIKKERHET OG GIT

Arbeid bare i den eksisterende, separate worktreen for PR #7.

Finn riktig worktree gjennom `git worktree list`.

Ikke endre:

- ~/Downloads/G27-isum-vijai
- /private/tmp/G27-isum-vijai-mvp-002-gemini

Ikke les eller endre:

- .memlog.md
- .streamlit/secrets.toml
- API-nøkler
- private .env-filer

Ikke utfør ekte Gemini API-kall.

Ikke bruk force push.

Ikke merge PR #7 automatisk.

Kontroller at worktreen peker på riktig branch og at den ikke inneholder uventede endringer før du starter.

## 2. ARKIVER PROMPT 029 ORDRETT

Dette er den viktigste dokumentasjonsrettelsen.

Eksisterende fil:

docs/prompts/PROMPT_029_FINAL_AUDIT.md

Inneholder ifølge sluttrevisjonen bare en henvisning til originalprompten, ikke hele teksten.

Du skal:

1. Undersøke eksisterende arkivformat.
2. Finne originalteksten til PROMPT 029 i tilgjengelig Codex-samtale.
3. Arkivere hele teksten ordrett.
4. Bevare linjeskift, overskrifter, instruksjoner og rekkefølge.
5. Ikke forkorte, omskrive eller rekonstruere teksten.
6. Dokumentere kilde og verifikasjonsmetode.
7. Oppdatere docs/CODEX_PROMPT_LOG.md.
8. Oppdatere docs/prompts/PROMPT_HISTORY_GAPS.md.
9. Oppdatere sluttrevisjonens sjekkliste.

VIKTIG:

Dersom du ikke har tilgang til hele originalteksten, skal du ikke late som om den er arkivert.

Be om at originalprompten limes inn.

PROMPT 027 og andre historiske hull skal fortsatt dokumenteres korrekt.

## 3. LOGGFØR DENNE NYE PROMPTEN

Arkiver også denne oppfølgingsprompten etter prosjektets eksisterende nummereringssystem.

Finn neste tilgjengelige nummer.

Ikke overskriv eksisterende promptfiler.

Registrer:

- Originaltekst.
- Dato.
- Formål.
- Arbeidsbranch.
- Gjennomførte handlinger.
- Endrede filer.
- Testresultater.
- Commit.
- PR.

Dersom hele originalteksten ikke er tilgjengelig, dokumenter dette eksplisitt.

## 4. KONTROLLER PR #7

Undersøk:

- Alle endrede filer.
- Nye testdata.
- Nye tester.
- README-endringer.
- Auditdokumentasjon.
- BMAD-sporbarhet.
- GitHub-status.
- Eventuelle mergekonflikter.

Kontroller at de tre syntetiske testcasene er korrekte og faktisk brukes i tester.

Kontroller at README beskriver lokal demo uten API-nøkkel.

Kontroller at lokal quiz beskrives som demo, ikke som KI-generert quiz.

Kontroller at dokumentasjonen samsvarer med faktisk implementasjon.

Rett konkrete feil.

## 5. KJØR SLUTTTESTENE PÅ NYTT

Kjør:

- Full pytest-suite.
- Dokumentasjonstester.
- Relevante Streamlit AppTests.
- Tester for PDF-behandling.
- Tester for quiz og poengsum.
- Mock-baserte Gemini-tester.
- git diff --check.

Tidligere rapporterte resultater:

108 automatiserte tester.
5 dokumentasjonstester.

Ikke anta at disse resultatene fortsatt gjelder.

Rapporter de nye faktiske resultatene.

Ikke fjern tester for å oppnå grønn status.

## 6. UNDERSØK FULLSTENDIGE INNLEVERINGSKRAV

Den tidligere revisjonen fant følgende offisielle emnebeskrivelse:

https://www.himolde.no/studier/emner/log/2026/host/ibe160.html

Tidligere rapportert vurderingsfordeling:

- Prosjektkode/funksjonalitet og KI-dokumentasjon: 70 %.
- Refleksjonsrapport: 30 %.

Verifiser opplysningene mot tilgjengelig emnebeskrivelse.

Skill mellom:

A. Offisiell emnebeskrivelse.
B. Gruppens konkrete oppgavetekst.
C. Faglærerens product brief-tilbakemelding.
D. Eventuell detaljert sensorveiledning.

Ikke anta at den offentlige emnebeskrivelsen inneholder alle innleveringskrav.

Undersøk om full oppgavetekst finnes i repository eller tilgjengelige prosjektfiler.

Hvis den ikke finnes, dokumenter at gruppen må hente den fra emneplattformen.

## 7. FORBERED REFLEKSJONSRAPPORTEN

Undersøk først om refleksjonsrapporten skal leveres individuelt eller som gruppe, hvilket format den skal ha, eventuelt omfang og hvilke vurderingskriterier som gjelder.

Ikke anta dette.

Hvis tilstrekkelige krav og dokumenterte prosjektfakta finnes, opprett et tydelig merket utkast på riktig sted.

Rapporten skal bygge på faktisk dokumentasjon:

- Product brief.
- BMAD-arbeid.
- Arkitekturvalg.
- Utviklingsprompts.
- Bruk av Codex.
- Gemini-integrasjon.
- Testing.
- Feil og forbedringer.
- DEC-003.
- Personvern.
- Iterasjoner.
- Begrensninger.

Ikke finn på gruppemedlemmers personlige erfaringer, innsats eller refleksjoner.

Hvis rapporten krever individuelle refleksjoner, opprett heller en strukturert disposisjon med spørsmål hver student må besvare selv.

Ikke presenter et slikt utkast som en ferdig, personlig refleksjonsrapport.

Ikke legg refleksjonsrapporten i PR #7 dersom det er uklart om den er individuell, privat eller skal leveres separat.

## 8. OPPDATER SLUTTDOKUMENTASJONEN

Kontroller og oppdater ved behov:

docs/audit/FINAL_AUDIT_REPORT.md

docs/audit/FINAL_TEST_REPORT.md

docs/audit/FINAL_SUBMISSION_CHECKLIST.md

docs/audit/REQUIREMENTS_TRACEABILITY.md

docs/audit/TEACHER_FEEDBACK_RESOLUTION.md

README.md

docs/CODEX_PROMPT_LOG.md

docs/prompts/PROMPT_HISTORY_GAPS.md

Bevar alle dokumenterte begrensninger.

Ikke endre PARTIAL eller NOT VERIFIED til PASS uten nye bevis.

## 9. GJENNOMFØR ENDELIG GIT-KONTROLL

Når endringene er ferdige:

1. Kontroller git diff.
2. Kontroller at ingen hemmeligheter er inkludert.
3. Kontroller at .memlog.md er urørt.
4. Kontroller promptarkivet.
5. Kjør tester.
6. Kjør git diff --check.
7. Commit relevante endringer.
8. Push til eksisterende PR #7-branch.
9. Kontroller GitHub-status.

Ikke opprett en ny PR dersom PR #7 fortsatt er riktig.

Ikke merge.

## 10. SLUTTRAPPORT

Svar på norsk med:

1. Hva som ble rettet.
2. Hvor PROMPT 029 er arkivert.
3. Om PROMPT 029 er arkivert ordrett eller fortsatt mangler originaltekst.
4. Hvilket nummer denne oppfølgingsprompten fikk.
5. Hvilke tidligere prompt-hull som fortsatt finnes.
6. Hvilke tester som ble kjørt.
7. Faktiske testresultater.
8. Status for PR #7.
9. Status for refleksjonsrapporten.
10. Hvilke innleveringskrav som er verifisert.
11. Hvilke innleveringskrav som fortsatt mangler.
12. Om PR #7 er klar for merge.
13. Hva gruppen må gjøre før endelig innlevering.

Vær konkret.

Ikke hev at prosjektet er ferdig med hele innleveringen dersom refleksjonsrapport eller formelle krav fortsatt mangler.

## START

Begynn med å finne riktig PR #7-worktree, kontrollere Git-status og undersøke promptarkivet.

Gjennomfør alle trygge steg selvstendig.

Stopp bare når et steg krever manglende originaltekst, personlige refleksjoner, tilgang til emneplattformen eller en beslutning fra gruppen.

Fullfør alle øvrige oppgaver og oppdater PR #7 uten å merge.
```
