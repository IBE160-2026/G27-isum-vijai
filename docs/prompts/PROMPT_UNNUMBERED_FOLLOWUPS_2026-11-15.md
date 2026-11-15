# Unummererte oppfølgingsprompter – Gemini og historikk (2026-11-15)

Disse promptene er ordrette kopier av separate brukerbeskjeder som er tilgjengelige i denne Codex-samtalen. De har ikke fått historiske PROMPT-numre. Arkivet slår dem ikke sammen til én oppgave.

## Statusforespørsel om promptloggen

```text
Gi meg en kort statusrapport fra dokumentasjonskontrollen.

Les PROMPT_HISTORY_GAPS.md og CODEX_PROMPT_LOG.md i Gemini-worktree.

Oppgi:
1. Antall promptoppføringer før og etter kontrollen.
2. Hvilke promptnummer som er dokumentert.
3. Hvilke originale prompttekster som mangler.
4. Hvilke prompter som er rekonstruert.
5. Om tidligere dokumentasjon er bevart.
6. Om dokumentasjonen er komplett for tilgjengelige kilder.

Ikke endre filer, commit, push eller opprett PR.

Ikke les .memlog.md eller Secrets.
```

## Godkjenning av dokumentasjonskontroll og Gemini-oppfølging

```text
Jeg godkjenner dokumentasjonskontrollen med de dokumenterte forbeholdene.

Bevar PROMPT_HISTORY_GAPS.md og all eksisterende prompt-historikk. Ikke fyll inn PROMPT 027 uten dokumentasjon.

Fortsett nå med det tidligere oppdraget om GEMINI-MODEL i Gemini-worktree:

/private/tmp/G27-isum-vijai-mvp-002-gemini

Undersøk hvilken Gemini-modell som faktisk er konfigurert, hvordan modellnavnet kan overstyres, og hvordan vi trygt kan kontrollere modelltilgangen.

Ikke utfør ekte API-kall uten å be om godkjenning først.

Oppdater relevante tester og BMAD-logger med bekreftede funn.

Ikke les Secrets eller .memlog.md. Ikke endre originalarbeidsmappen.

Ikke commit, push, opprett PR eller merge.

Rapporter funnene og anbefalt neste steg før du gjør modellendringer.
```

## Godkjenning av én models.list()-diagnostikk

```text
Ja, jeg godkjenner én ekstern models.list()-diagnostikkforespørsel.

Utfør den kun i:
/private/tmp/G27-isum-vijai-mvp-002-gemini

Bruk:
./.venv/bin/python -m prototype.gemini_diagnostics --list-models --confirm-external-call

Sikkerhetskrav:
- Ikke vis, loggfør eller lagre API-nøkkelen.
- Ikke send forelesningsnotater eller personopplysninger.
- Ikke utfør generate_content-kall.
- Ikke utfør flere eksterne forespørsler uten ny godkjenning.
- Rapporter kun tilgjengelige modell-ID-er, relevant genereringsstøtte og eventuelle ufølsomme feilkoder.
- Ikke endre standardmodellen ennå.
- Ikke rør .memlog.md eller originalarbeidsmappen.
- Ikke commit, push, opprett PR eller merge.

Etter diagnostikken: Anbefal hvilken tilgjengelig modell som passer prosjektets krav til sammendrag, quiz og strukturert JSON-respons.

Dokumenter resultatet i TEST_LOG.md og relevante BMAD-logger uten sensitive opplysninger.

Stopp etter rapporten og vent på godkjenning før modellendringer.
```

## Godkjenning av midlertidig lokal modelloverstyring

```text
Jeg godkjenner en lokal, midlertidig modelloverstyring til gemini-3.5-flash-lite i Gemini-worktree:

/private/tmp/G27-isum-vijai-mvp-002-gemini

Oppgave:

1. Konfigurer GEMINI_MODEL=gemini-3.5-flash-lite kun lokalt for testing.
2. Ikke endre standardmodellen i kildekoden ennå.
3. Kontroller uten å vise hemmeligheter at Streamlit-prosessen faktisk bruker den valgte modellen.
4. Ikke endre eller overskriv GEMINI_API_KEY.
5. Ikke gjennomfør generate_content-kall automatisk. Den manuelle testen skal utføres av brukeren etterpå.
6. Kontroller at lokal modus, PDF-funksjonen og samtykkekravet er bevart.
7. Kjør relevante tester og git diff --check dersom kode eller dokumentasjon endres.
8. Dokumenter modelloverstyringen og at den ennå ikke er verifisert med en vellykket generering.
9. Bevar hele prompt-historikken og PROMPT_HISTORY_GAPS.md.
10. Ikke les .memlog.md, ikke endre originalarbeidsmappen og ikke commit, push, opprett PR eller merge.

Rapporter nøyaktig hvordan jeg starter Streamlit med modelloverstyringen, og hvordan jeg bekrefter at riktig modell brukes.

Stopp etter rapporten.
```

## Manuell tekstgenerering og undersøkelse av quizantall

```text
MVP SPRINT 002 – Dokumenter vellykket Gemini-generering og undersøk quiz

Arbeid kun i:
/private/tmp/G27-isum-vijai-mvp-002-gemini

Branch: feature/mvp-002-gemini-ai

BEKREFTET MANUELL TEST

15. november 2026 ble Gemini testet på Streamlit port 8503 med midlertidig GEMINI_MODEL=gemini-3.5-flash-lite.

Brukeren limte inn syntetiske forelesningsnotater om prosjektledelse.

Resultat:
- Gemini genererte et relevant sammendrag.
- Gemini genererte tre sentrale begreper.
- Gemini genererte tre quizspørsmål med fire svaralternativer hver.
- Spørsmålene var relevante for kildeteksten.
- Brukeren ba om fem spørsmål, men fikk tre.
- Quizretting og poengberegning er ennå ikke manuelt verifisert.
- PDF med Gemini er ennå ikke manuelt verifisert.

Dette er en vellykket manuell ende-til-ende-test av tekstbasert Gemini-generering, men ikke en fullstendig godkjenning av Sprint 002.

OPPGAVER

1. Dokumenter testresultatet i docs/testing/TEST_LOG.md.
2. Oppdater BMAD-status, prosjektkontekst, changelog og promptlogg.
3. Undersøk hvorfor fem ønskede spørsmål resulterte i tre.
4. Kontroller quizgeneratorens regler, JSON-validering og eventuelle filtre.
5. Undersøk om gyldige spørsmål forkastes unødvendig.
6. Ikke finn på spørsmål eller fjern kildevalideringen bare for å nå ønsket antall.
7. Legg til relevante regresjonstester dersom du finner en faktisk feil.
8. Kjør full pytest og git diff --check.
9. Bevar all tidligere dokumentasjon og PROMPT_HISTORY_GAPS.md.
10. Ikke les Secrets eller .memlog.md.
11. Ikke endre originalarbeidsmappen.
12. Ikke commit, push, opprett PR eller merge.

Rapporter hvorfor bare tre spørsmål ble generert, hva som eventuelt bør rettes, og hvilke manuelle tester som gjenstår før PR #5.
```

## Sluttkontroll før PR #5

```text
MVP SPRINT 002 – Sluttkontroll før PR #5

Arbeid kun i:
/private/tmp/G27-isum-vijai-mvp-002-gemini

Branch: feature/mvp-002-gemini-ai

Brukeren har nå gjennomført følgende manuelle tester med gemini-3.5-flash-lite på Streamlit port 8503:

TEST 1 – Tekstbasert Gemini:
- Relevant sammendrag generert.
- Sentrale begreper generert.
- Fire quizspørsmål generert av fem ønskede.
- Fire riktige svar ga 4 av 4.
- En tidligere test viste 0 av 4, men de valgte svarene er ikke dokumentert.

TEST 2 – PDF med Gemini:
- PDF: testnotater_informasjonssystemer_databaser.pdf
- PDF-opplasting og tekstuttrekk fungerte.
- Gemini genererte relevant sammendrag.
- Tre sentrale begreper generert.
- Tre quizspørsmål generert av fem ønskede.
- Quizretting viste 1 av 3 riktige, med to feil og ett riktig svar.
- Fasit og forklaringer samsvarte med notatene.

OPPGAVER:

1. Dokumenter begge testene i TEST_LOG.md og relevante BMAD-logger.
2. Oppdater CODEX_PROMPT_LOG.md uten å overskrive tidligere prompt-historikk.
3. Bevar PROMPT_HISTORY_GAPS.md.
4. Kontroller at standardmodellen i kildekoden fortsatt er uendret, og at gemini-3.5-flash-lite bare er en lokal overstyring.
5. Kjør full pytest og git diff --check.
6. Kontroller git status, branch, endrede filer og at Secrets og .memlog.md ikke inngår i endringene.
7. Vurder om Sprint 002 er klar for PR #5.
8. Rapporter eventuelle risikoer eller åpne punkter.

Ikke les, endre eller stage .memlog.md.
Ikke vis API-nøkler.
Ikke endre originalarbeidsmappen.
Ikke utfør flere eksterne Gemini-kall.
Ikke commit, push, opprett PR eller merge.

Stopp etter sluttkontrollen og rapporter resultatet.
```

## Klargjøring og opprettelse av PR #5

```text
MVP SPRINT 002 – Klargjør og opprett Pull Request

Arbeid kun i:
/private/tmp/G27-isum-vijai-mvp-002-gemini

Branch: feature/mvp-002-gemini-ai

Jeg godkjenner at du klargjør Sprint 002 for GitHub Pull Request mot main.

Før Git-operasjoner:

1. Bekreft riktig worktree, branch og oppdatert origin/main.
2. Kontroller alle endrede og nye filer.
3. Kontroller at .memlog.md, .streamlit/secrets.toml, API-nøkler, .venv og andre lokale filer ikke blir staged eller committed.
4. Kontroller at all eksisterende prompt-historikk er bevart, inkludert PROMPT_HISTORY_GAPS.md.
5. Bevar alle tidligere commits og dokumenterte BMAD-beslutninger.
6. Kjør full pytest og git diff --check.
7. Kontroller staged diff før commit.

Deretter:

8. Commit kun relevante kode-, test- og dokumentasjonsendringer på feature/mvp-002-gemini-ai.
9. Push feature-branchen til origin.
10. Opprett én Pull Request mot main med en tydelig beskrivelse av:
   - Gemini-integrasjonen
   - Tekst- og PDF-generering
   - Samtykke og personvern
   - Quizgenerering og retting
   - Automatiserte og manuelle tester
   - Modellkonfigurasjon og gjenværende forbehold

VIKTIG:
- Standardmodellen i kildekoden er fortsatt gemini-2.5-flash.
- Vellykkede manuelle tester brukte midlertidig GEMINI_MODEL=gemini-3.5-flash-lite.
- Ikke presenter standardmodellen som manuelt verifisert.
- Ikke endre standardmodell uten ny godkjenning.
- Ikke les, endre, stage eller commit .memlog.md.
- Ikke les eller vis API-nøkler.
- Ikke endre originalarbeidsmappen.
- Ikke utfør nye Gemini API-kall.
- Ikke merge PR-en.

Hvis GitHub-autentisering eller Git-operasjoner feiler, stopp og rapporter problemet. Ikke bruk force push.

Rapporter commit-SHA, push-status, PR-nummer, PR-lenke og testresultater når du er ferdig.
```

## Fortsettelse av dokumentasjonsoppdraget etter avkortet melding

```text
Fortsett dokumentasjonsoppdraget i Gemini-worktreet:

/private/tmp/G27-isum-vijai-mvp-002-gemini

Den forrige prompten ble avkuttet. Her er godkjenningen og resten av oppgaven.

1. Sammenlign begge CODEX_PROMPT_LOG.md-filene grundig.
2. Bevar alle eksisterende oppføringer i Gemini-loggen.
3. Finn eventuelle unike originaltekster i originalmappen og legg dem til i Gemini-loggen uten å endre originalmappen.
4. Kontroller at PROMPT 001–026 og 028 er bevart.
5. Ikke opprett PROMPT 027 uten dokumentasjon.
6. Samle alle tilgjengelige senere Codex-prompttekster for PDF, Gemini, feilsøking, modelltilgang, testing og PR-forberedelser.
7. Skill tydelig mellom ordrette originalprompter, dokumenterte sammendrag og manglende originaltekster.
8. Oppdater PROMPT_HISTORY_GAPS.md med alle hull som fortsatt ikke kan dokumenteres.
9. Oppdater relevante BMAD- og testlogger uten å slette historikk.
10. Kjør dokumentasjonstester og git diff --check.

Ikke finn på manglende prompttekster.

Ikke les eller endre .memlog.md eller Secrets.
Ikke endre originalmappen.
Ikke utfør Gemini API-kall.
Ikke commit, push, opprett PR eller merge.

Rapporter antall verifiserte originalprompter, rekonstruerte oppføringer og gjenværende hull.

Oppgi også nøyaktig hvilken CODEX_PROMPT_LOG.md som nå er mest komplett.

Stopp etter rapporten.
```
