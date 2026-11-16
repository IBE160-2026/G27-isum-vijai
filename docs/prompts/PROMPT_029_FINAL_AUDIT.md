# PROMPT 029 – Komplett sluttrevisjon, ferdigstilling og innleveringskontroll

- **Dato:** 2026-11-16 (sesjonsdato).
- **Formål:** Gjennomføre evidensbasert sluttkontroll av IBE160-prosjektet i en isolert worktree, oppdatere sporbarhet, tester og innleveringsdokumentasjon, rette forsvarlige mangler og klargjøre én PR uten å merge.
- **Branch/worktree:** `chore/ibe160-final-quality-audit`, `/private/tmp/G27-isum-vijai-final-audit`.
- **Kilde:** Den foregående brukerbeskjeden i Codex-økten, med tittelen «IBE160 – KOMPLETT SLUTTREVISJON, FERDIGSTILLING OG INNLEVERINGSKONTROLL».
- **Verifiseringsstatus for originaltekst:** Fulltekst kopiert ordrett fra tilgjengelig samtalemelding og nedenfor omsluttet av `text`-fence. Metadata over er arkivmetadata, ikke del av prompten.
- **Planlagte aktiviteter:** Kartlegge tilgjengelige krav og faglærerfeedback; kontrollere kode, tester, README, BMAD, beslutninger og promptspor; legge til tre faste syntetiske testcaser; dokumentere sporbarhet, testing, innleveringsklarhet og kjente hull; kjøre full verifikasjon; committe og pushe avgrensede endringer og opprette PR uten merge.
- **Gjennomføring og resultater:** Oppdateres etter sluttkontroll.
- **Filer/tester/commit/PR:** Oppdateres etter sluttkontroll.

## Original prompt (ordrett)

```text
# IBE160 – KOMPLETT SLUTTREVISJON, FERDIGSTILLING OG INNLEVERINGSKONTROLL

## ROLLE OG OPPDRAG

Du er senior fullstack-utvikler, QA-ansvarlig, programvarearkitekt, BMAD-prosessansvarlig og dokumentasjonsansvarlig for IBE160-prosjektet G27-isum-vijai.

Du skal gjennomføre en komplett, strukturert og evidensbasert sluttrevisjon av prosjektet.

Dette er en gjennomføringsoppgave, ikke bare en analyse.

Du skal undersøke hele prosjektet, identifisere mangler, rette dem der det er forsvarlig, forbedre dokumentasjonen, kjøre relevante tester og levere en ferdig kvalitetssikret Pull Request.

Målet er at prosjektet skal være så klart som mulig for innlevering og demonstrasjon.

Ikke overdriv prosjektets kvalitet eller påstå at krav er oppfylt uten konkrete bevis.

Ikke bygg unødvendige funksjoner eller gjør store arkitekturendringer bare for å øke kompleksiteten.

---

# 1. PROSJEKTINFORMASJON

Repository:
IBE160-2026/G27-isum-vijai

Prosjekt:
Foredragsnotater → Sammendrag & Quizgenerator

Teknologi:
Python, Streamlit, pypdf og Google Gemini.

Sist bekreftede main-commit:
fef77e85f078b6e5ecdb82f09a903b8a6a1d4fc1

Tidligere Pull Requests:

- PR #5: Gemini MVP – MERGED.
- PR #6: DEC-003 og dokumentasjon – MERGED.

Tidligere rapporterte testresultater:

- 99 automatiserte tester bestått.
- 5 dokumentasjonstester bestått.
- git diff --check bestått.

Standardmodell:
gemini-3.5-flash-lite

Miljøvariabelen GEMINI_MODEL skal fortsatt kunne overstyre standardmodellen.

Dette er tidligere rapportert status, ikke en erstatning for ny kontroll.

---

# 2. SIKKER GIT-ARBEIDSMETODE

Arbeid kun i en ny, separat Git-worktree basert på oppdatert origin/main.

Eksisterende arbeidsmapper skal ikke endres:

~/Downloads/G27-isum-vijai

/private/tmp/G27-isum-vijai-mvp-002-gemini

Anbefalt branch:

chore/ibe160-final-quality-audit

Anbefalt worktree:

/private/tmp/G27-isum-vijai-final-audit

Før oppstart:

1. Kontroller faktisk repository og Git-status.
2. Kjør git fetch origin.
3. Bekreft oppdatert origin/main.
4. Kontroller om en tilsvarende branch eller PR allerede eksisterer.
5. Opprett separat worktree og branch dersom dette kan gjøres trygt.
6. Kontroller at den nye worktreen er ren.

Ikke bruk force push.

Ikke skriv om eksisterende Git-historikk.

Ikke merge automatisk.

Ikke slett eksisterende branches eller worktrees.

Ikke endre originalarbeidsmappen.

Hvis opprettelse av worktree ikke kan gjøres sikkert, stopp før du endrer filer og rapporter hvorfor.

---

# 3. ABSOLUTTE SIKKERHETSREGLER

Følgende regler gjelder under hele arbeidet:

- Ikke les, endre, stage, slett eller commit .memlog.md.
- Ikke les eller skriv ut .streamlit/secrets.toml.
- Ikke les eller skriv ut API-nøkler.
- Ikke les eller skriv ut innholdet i .env-filer med hemmeligheter.
- Ikke commit .venv.
- Ikke send ekte studentnotater eller personopplysninger til Gemini.
- Ikke utfør eksterne Gemini API-kall.
- Ikke loggfør hemmeligheter eller private brukerdata.
- Ikke endre produksjonskonfigurasjon uten nødvendig grunn.
- Ikke omgå GitHub branch protection.
- Ikke utfør destruktive Git-operasjoner.

Bruk syntetiske testdata, mocks og lokale tester.

Sikkerhet går foran fullføring.

---

# 4. OBLIGATORISK PROMPTLOGGING – START FØR ANDRE ENDRINGER

Dette er et absolutt krav.

Før du begynner å endre applikasjonen eller dokumentasjonen, skal du undersøke prosjektets eksisterende promptlogg.

Relevante steder:

docs/CODEX_PROMPT_LOG.md

docs/prompts/

docs/prompts/PROMPT_HISTORY_GAPS.md

Undersøk eksisterende nummerering, arkivformat og rutiner.

## 4.1 Loggfør denne hovedprompten

Arkiver hele denne hovedprompten ordrett dersom den komplette originalteksten er tilgjengelig i Codex-økten.

Bruk neste ledige promptnummer etter eksisterende dokumentert historikk.

Ikke gjenbruk PROMPT 027 bare for å fylle et historisk hull.

Hvis hovedpromptens eksakte tekst ikke er tilgjengelig for arkivering, dokumenter dette eksplisitt og be om originalteksten i stedet for å finne på en rekonstruksjon.

Registrer:

- Promptnummer eller etablert arkiv-ID.
- Dato.
- Formål.
- Arbeidsbranch.
- Kilde og om teksten er ordrett.
- Planlagte aktiviteter.
- Faktisk gjennomføring.
- Endrede filer.
- Testresultater.
- Commit-ID.
- PR-nummer når dette finnes.

Arkiver hovedprompten før øvrige prosjektendringer, men oppdater resultatmetadata ved slutten av arbeidet.

## 4.2 Tidligere prompts

Kontroller at tidligere arkiverte utviklingsprompts er bevart.

Undersøk:

- PROMPT 001–026.
- Status for PROMPT 027.
- PROMPT 028.
- Senere nummererte prompts.
- Unummererte oppfølgingsprompts.
- Dokumenterte historiske hull.

Ikke anta at listen over er fullstendig.

Undersøk faktisk arkivstruktur.

Ikke endre historiske originaltekster.

Ikke fabriker manglende prompts.

Ikke påstå at arkivet er 100 % komplett dersom originaltekster mangler.

Bevar og oppdater PROMPT_HISTORY_GAPS.md ved behov.

## 4.3 Nye prompts under revisjonen

Alle tilgjengelige nye brukerprompts i denne arbeidsøkten skal loggføres.

For hver prompt registreres:

- Originaltekst når tilgjengelig.
- Tidspunkt eller dato når kjent.
- Formål.
- Handlinger.
- Filer.
- Tester.
- Resultat.
- Commit eller PR.

Ikke registrer Codex' egne interne resonnementer som brukerprompts.

Hvis Codex ikke automatisk har tilgang til tidligere samtalemeldinger, skal den dokumentere begrensningen og ikke påstå at de er arkivert.

## 4.4 Gemini-prompts

Skill mellom:

1. Utviklingsprompts til Codex.
2. Promptmaler i applikasjonens kildekode.
3. Faktiske API-forespørsler.
4. Modellresultater.

Kontroller at promptmalene brukt til sammendrag, begreper og quiz er sporbare og dokumenterte.

Dokumenter hvordan promptene forsøker å begrense innholdet til brukerens notater.

Ikke lagre sensitive API-payloads.

Ikke utfør eksterne Gemini-kall.

---

# 5. KILDEGRUNNLAG OG VURDERINGSKRITERIER

Bruk faglærerens dokument:

«Tilbakemelding på product brief»

Gruppe:
G27 – G27-isum-vijai

Dato:
2026-10-06

Dokumentet gjelder product-brief.md ved commit dc2a630.

VIKTIG:

Dette er tilbakemelding på en tidlig product brief, ikke nødvendigvis hele den endelige oppgaveteksten.

Søk etter tilgjengelig:

- Fullstendig IBE160-oppgavetekst.
- Sensorveiledning.
- Vurderingskriterier.
- Product brief.
- PRD.
- Arkitektur.
- Epics.
- Stories.
- BMAD-artefakter.
- README.
- Testplaner.
- Testlogger.
- Beslutningslogger.
- Promptarkiv.

Ikke finn på krav som ikke finnes i kildene.

Hvis full oppgavetekst eller sensorveiledning ikke er tilgjengelig, marker dette som NOT VERIFIED.

Opprett:

docs/audit/REQUIREMENTS_TRACEABILITY.md

Hvert krav skal ha:

- Krav-ID.
- Kilde.
- Vurderingsområde.
- Forventet resultat.
- Relevant implementasjon.
- Relevant dokumentasjon.
- Relevant test.
- Faktisk resultat.
- Status.
- Eventuell mangel.
- Tiltak.

Bruk statusene:

PASS
PARTIAL
FAIL
NOT VERIFIED
NOT APPLICABLE

Ikke marker PASS uten konkret bevis.

---

# 6. FAGLÆRERENS SYV VURDERINGSOMRÅDER

Gjennomfør kontroll etter følgende områder og vekter fra faglærerens tilbakemelding om del 1.

## 6.1 PROSESS OG KI-STYRING – 30 %

Kontroller:

- Product brief.
- PRD.
- Arkitektur.
- Epics og stories.
- BMAD-arbeidsflyt.
- Endringshistorikk.
- Promptlogging.
- Dokumenterte beslutninger.
- Sporbarhet fra krav til kode.
- Hvordan KI-generert kode er kontrollert.
- Hvordan feil er oppdaget og rettet.
- Hvordan gruppen har arbeidet iterativt.

Undersøk spesielt om den tidlige product briefen faktisk er oppdatert etter faglærerens tilbakemelding.

Kontroller at plan, kode og dokumentasjon beskriver samme løsning.

Ikke lag retrospektive dokumenter som feilaktig fremstilles som om de ble skrevet før implementasjonen.

Manglende dokumentasjon kan opprettes nå, men skal merkes som retrospektiv der det er relevant.

Rett inkonsistenser.

Dokumenter eventuelle historiske hull.

## 6.2 FUNKSJONALITET OG OMFANG – 20 %

Kontroller hele brukerflyten:

1. Åpne applikasjonen.
2. Legge inn tekst.
3. Laste opp PDF.
4. Velge sammendragslengde.
5. Velge vanskelighetsgrad.
6. Velge antall quizspørsmål.
7. Generere sammendrag.
8. Generere begrepsliste.
9. Generere quiz.
10. Svare på spørsmål.
11. Få riktig/feil.
12. Se forklaring.
13. Se poengsum.
14. Starte en ny quiz.
15. Bytte notater.
16. Bruke lokal modus.
17. Bruke valgfri Gemini-modus.

Undersøk hva som faktisk er implementert.

Ikke anta at alle funksjoner finnes.

Faglæreren ønsket en utvidelse utover ett skjema og ett språkmodellkall.

Kontroller at den interaktive quizen faktisk gir reell egenlogikk og testbar funksjonalitet.

Kontroller også:

- Tom input.
- Ugyldig PDF.
- PDF uten lesbar tekst.
- Store notater.
- Endring av input etter generering.
- Endring av innstillinger.
- Gjentatt generering.
- Manglende API-nøkkel.
- Feil fra språkmodellen.
- Manglende eller ufullstendige modellresultater.
- Ugyldig quizformat.
- Færre spørsmål enn forespurt.

Rett konkrete feil.

Ikke legg til database, innlogging eller lagring bare for å gjøre prosjektet større dersom dette ikke er nødvendig eller besluttet.

## 6.3 KVALITETSSIKRING OG TESTING – 15 %

Kontroller eksisterende testdekning.

Kjør full pytest.

Undersøk hvilke funksjoner som faktisk testes.

Lag eller forbedre faste syntetiske testnotater med fasit.

Faglæreren anbefalte to–tre faste testnotater.

Opprett minst tre forskjellige syntetiske testcaser dersom slike ikke allerede finnes.

Eksempler:

A. Informasjonssystemer og databaser.
B. Programmering og algoritmer.
C. Prosjektarbeid og systemutvikling.

For hvert testnotat dokumenteres:

- Forventede begreper.
- Relevante fakta.
- Mulige quizspørsmål.
- Forventede svar.
- Informasjon som ikke finnes i notatet.
- Forventet oppførsel ved manglende informasjon.

Bruk disse til deterministiske tester der det er mulig.

Bruk mocks for Gemini.

Kontroller:

- Korrekt svar gir riktig poeng.
- Feil svar gir ikke poeng.
- Poengsummen beregnes riktig.
- Ny quiz nullstiller nødvendig tilstand.
- Bytte av notater gir ikke gamle resultater.
- Feilmeldinger er forståelige.
- Quizspørsmål er knyttet til kildematerialet.
- Ubegrunnede påstander håndteres.
- Applikasjonen krasjer ikke ved vanlige feil.

Ikke påstå at automatisk kildevalidering garanterer at alle KI-svar er faktuelt riktige.

Dokumenter begrensningene.

Oppdater testloggen med faktiske testresultater.

## 6.4 DESIGN OG BRUKEROPPLEVELSE – 10 %

Gjennomgå Streamlit-grensesnittet.

Kontroller:

- Oversiktlig startside.
- Tydelig arbeidsflyt.
- Forståelige felt og valg.
- Lesbart sammendrag.
- Oversiktlig begrepsliste.
- Forståelig quiz.
- Tydelig riktig/feil.
- Tydelig poengsum.
- Gode feilmeldinger.
- Informasjon om KI-begrensninger.
- Informasjon om personvern.
- Tydelig forskjell mellom lokal modus og Gemini-modus.

Kontroller at brukeren forstår når data kan sendes til en ekstern tjeneste.

Lag en enkel dokumentert brukerflyt dersom dette mangler.

Hvis skjermbilder eller visuell testing ikke er mulig, marker dette som NOT VERIFIED.

Ikke hev at en manuell UI-test er utført dersom bare kildekoden er undersøkt.

Rett konkrete UX-problemer uten å bygge om hele applikasjonen.

## 6.5 KODEKVALITET OG ARKITEKTUR – 10 %

Kontroller:

- Modulstruktur.
- Funksjonsansvar.
- Duplisert kode.
- Navngivning.
- Feilhåndtering.
- Testbarhet.
- Avhengigheter.
- Python-versjon.
- Streamlit-tilstand.
- PDF-behandling.
- Gemini-klient.
- Konfigurasjon.
- Sikkerhet.
- Logging.
- Datavalidering.

Kontroller at Gemini-kall ikke skjer ukontrollert.

Kontroller at brukerinput behandles som data, ikke som autoritative instruksjoner.

Undersøk risiko for prompt injection og ubegrunnede KI-svar.

Kontroller at API-nøkler ikke ligger hardkodet i kildekoden.

Ikke les hemmelige filer for å undersøke dette.

Undersøk bare trygge, versjonerte kildefiler og konfigurasjonsmaler.

Rett konkrete kvalitetsproblemer.

Unngå store refaktoreringer uten tydelig nytte.

## 6.6 README OG KJØRBARHET – 10 %

Dette er spesielt viktig.

Sensor skal kunne forstå prosjektet og prøve løsningen uten gruppens private API-nøkkel.

Kontroller README fra perspektivet til en person som aldri har sett prosjektet.

README bør forklare:

- Hva prosjektet gjør.
- Hvem løsningen er laget for.
- Hvilke funksjoner som finnes.
- Hvilke begrensninger som finnes.
- Teknologistakk.
- Python-versjon.
- Installasjon.
- Opprettelse av virtuelt miljø.
- Installasjon av avhengigheter.
- Oppstart av Streamlit.
- Hvordan lokal modus fungerer.
- Hvordan Gemini-modus aktiveres.
- At Gemini-modus er valgfri.
- Hvordan sensor kan teste uten API-nøkkel.
- Hvordan tester kjøres.
- Hvor BMAD-dokumentasjonen ligger.
- Hvor promptarkivet ligger.
- Hvordan syntetiske testnotater brukes.
- Personvern og sikkerhetsbegrensninger.

Gjennomfør en reell oppstartstest uten API-nøkkel dersom miljøet tillater det.

Bruk en ren, isolert testinstallasjon.

Ikke skriv ut eller inspiser eksisterende hemmeligheter.

Ikke hev at oppstart er testet dersom miljøet ikke tillater det.

Hvis README er feil, rett den.

## 6.7 RYDDIGHET I REPOSITORY – 5 %

Kontroller:

- Logisk mappestruktur.
- README i roten.
- Relevante dokumentasjonsmapper.
- Tester.
- Testdata.
- .gitignore.
- Fravær av utilsiktede genererte filer.
- Fravær av virtuelle miljøer i Git.
- Fravær av hemmeligheter i versjonerte filer.
- Ryddige filnavn.
- Konsistent dokumentasjon.
- Sporbar Git-historikk.

Ikke slett gamle filer uten å undersøke hvorfor de finnes.

Ikke fjern historisk dokumentasjon bare fordi den virker overflødig.

---

# 7. SPESIELL KONTROLL AV PRODUCT BRIEF

Faglæreren identifiserte følgende forbedringspunkter:

1. For lite funksjonelt omfang.
2. For lite målbare suksesskriterier.
3. Manglende konkret plan for språkmodell.
4. Uklar plan for kostnader og nøkkel.
5. Risiko for at sensor ikke kan kjøre løsningen.
6. Behov for testnotater og fasit.
7. Behov for tydeligere brukergruppe.
8. Behov for sporbar BMAD-prosess.

Sammenlign den opprinnelige briefen med dagens versjon.

Kontroller om hvert punkt er løst.

Hvis briefen ikke gjenspeiler dagens løsning, oppdater den.

Bevar opprinnelig historikk.

Ikke skriv om gamle beslutninger som om de ble tatt på et annet tidspunkt.

Lag en tabell med:

- Faglærerens opprinnelige kommentar.
- Hva gruppen gjorde.
- Relevant fil.
- Relevant test.
- Status.
- Eventuelt gjenstående arbeid.

---

# 8. BMAD – KOMPLETT PROSESSKONTROLL

Undersøk alle tilgjengelige BMAD-artefakter.

Kontroller særlig:

- Product brief.
- PRD.
- Arkitektur.
- Epics.
- Stories.
- Implementasjonsspesifikasjoner.
- Sprint-status.
- Beslutningslogg.
- Testplan.
- Testlogg.
- Endringslogg.

Ikke anta at alle dokumenttypene må finnes dersom den faktiske oppgaven ikke krever dem.

Sammenlign eksisterende dokumentasjon med faktisk kode.

Identifiser:

- Krav uten implementasjon.
- Implementasjon uten dokumentert krav.
- Tester uten tydelig krav.
- Krav uten tester.
- Utdaterte beslutninger.
- Motstridende beskrivelser.

Opprett eller oppdater nødvendige dokumenter.

Merk retrospektiv dokumentasjon korrekt.

Ikke fabrikker historiske sprintaktiviteter, møter eller beslutninger.

---

# 9. GEMINI, PERSONVERN OG DEC-003

Kontroller at DEC-003 fortsatt er korrekt.

Gjeldende beslutning:

Gemini er kun godkjent som valgfri prototypefunksjon for syntetiske, offentlige eller anonymiserte notater uten personopplysninger eller konfidensielt innhold.

Brukeren skal få tydelig informasjon og aktivt velge Gemini-funksjonen.

Brukeren skal selv starte genereringen.

Lokal modus skal være tilgjengelig.

Produksjonsbruk med personopplysninger er ikke godkjent.

DEC-003 er ikke en juridisk eller institusjonell godkjenning.

Kontroller:

- Samtykkemekanisme.
- Tilbakestilling av samtykke når nødvendig.
- Tydelig informasjon.
- Separasjon mellom lokal modus og Gemini.
- At Gemini ikke kalles uten brukerhandling.
- At feil håndteres.
- At modellnavn kan konfigureres.
- At standardmodellen er gemini-3.5-flash-lite.
- At ingen API-nøkkel er nødvendig i lokal modus.
- At ingen sensitive data loggføres.

Kontroller at dokumentasjonen ikke lover noe som ikke er bekreftet om:

- Kostnader.
- Leverandørens databehandling.
- Lagring.
- Sletting.
- Databehandleravtaler.
- Juridisk godkjenning.

Ikke utfør Gemini API-kall.

---

# 10. KILDEFORANKRING OG KVALITET PÅ KI-SVAR

Undersøk hvordan appen sikrer at sammendrag og quiz bygger på notatene.

Kontroller:

- Promptinstruksjoner.
- Strukturert respons.
- Parsing.
- Validering.
- Feilhåndtering.
- Kildehenvisninger dersom implementert.
- Håndtering av ukjente svar.
- Håndtering av ufullstendige quizresultater.

Test med syntetiske notater.

Kontroller at appen ikke ukritisk godtar ugyldige quizobjekter.

Undersøk om det finnes en risiko for at quizspørsmål inneholder informasjon uten støtte i notatene.

Skill mellom:

- Automatisk strukturvalidering.
- Heuristisk kildevalidering.
- Faktisk faglig korrekthet.

Ikke hev at en av disse automatisk garanterer de andre.

---

# 11. FULL TESTSTRATEGI

Kjør relevante tester i følgende rekkefølge:

A. Eksisterende pytest-suite.

B. Dokumentasjonstester.

C. Nye tester for identifiserte mangler.

D. Tester for lokal modus.

E. Mock-baserte Gemini-tester.

F. Tester for PDF-behandling.

G. Tester for quiztilstand og poengberegning.

H. Tester for samtykke og personvern.

I. Tester for feiltilstander.

J. README-installasjon og oppstart uten API-nøkkel, dersom praktisk mulig.

K. git diff --check.

Ved testfeil:

1. Undersøk årsaken.
2. Dokumenter feilen.
3. Rett den dersom det er forsvarlig.
4. Legg til regresjonstest.
5. Kjør relevante tester igjen.
6. Kjør hele testsuiten på nytt.

Ikke skjul feil ved å fjerne eller deaktivere tester.

Ikke endre forventede testresultater bare for å få grønn status.

Dokumenter nøyaktige testkommandoer og resultater.

---

# 12. GJENNOMFØR NØDVENDIGE RETTELSER

Etter revisjonen skal du ikke stoppe ved å liste opp mangler.

Rett alle trygge og klart avgrensede mangler som ligger innenfor prosjektets eksisterende omfang.

Prioriter:

P0 – Sikkerhet, datalekkasjer, kritiske feil.

P1 – Brutt kjernefunksjonalitet eller viktige innleveringskrav.

P2 – Manglende tester, dokumentasjon eller sporbarhet.

P3 – Mindre forbedringer og kosmetiske forhold.

For hver rettelse:

- Beskriv problemet.
- Identifiser årsaken.
- Utfør minimal forsvarlig endring.
- Legg til eller oppdater test.
- Kontroller at eksisterende funksjonalitet fortsatt virker.
- Oppdater dokumentasjon ved behov.

Ikke introduser nye store funksjoner uten eksplisitt behov.

Ikke endre arkitekturen unødvendig.

Ikke gjennomfør risikable endringer bare for å oppnå en kunstig «100 % ferdig»-status.

Hvis et problem krever en beslutning fra gruppen, dokumenter det og stopp akkurat den endringen.

Fortsett med uavhengige oppgaver.

---

# 13. DOKUMENTASJON SOM SKAL LEVERES

Bruk eksisterende dokumentasjonsstruktur når det er hensiktsmessig.

Opprett eller oppdater følgende:

docs/audit/FINAL_AUDIT_PLAN.md

Beskriver metode, omfang og kilder.

docs/audit/REQUIREMENTS_TRACEABILITY.md

Knytter krav til implementasjon, dokumentasjon og tester.

docs/audit/TEACHER_FEEDBACK_RESOLUTION.md

Viser hvordan faglærerens tilbakemeldinger er håndtert.

docs/audit/FINAL_TEST_REPORT.md

Dokumenterer testkommandoer, resultater og begrensninger.

docs/audit/FINAL_SUBMISSION_CHECKLIST.md

Inneholder sjekkliste for innlevering.

docs/audit/FINAL_AUDIT_REPORT.md

Inneholder samlet sluttvurdering.

Oppdater ved behov:

README.md

product-brief.md

docs/PROJECT_CONTEXT.md

docs/testing/TEST_LOG.md

docs/CHANGELOG_PROCESS.md

docs/CODEX_PROMPT_LOG.md

docs/prompts/PROMPT_HISTORY_GAPS.md

docs/bmad/WORKFLOW_STATUS.md

Eksisterende BMAD-artefakter.

Ikke opprett duplikatdokumenter dersom tilsvarende dokumentasjon allerede finnes.

Alle rapporter skal inneholde konkrete filreferanser og bevis.

---

# 14. INNLEVERINGSSJEKKLISTE

Opprett en sjekkliste med minst følgende kontrollpunkter:

[ ] Product brief er oppdatert.

[ ] PRD er kontrollert eller manglende krav er dokumentert.

[ ] Arkitektur er kontrollert.

[ ] BMAD-prosess er dokumentert.

[ ] Stories og implementasjon er sporbare.

[ ] Kjernefunksjoner fungerer.

[ ] Interaktiv quiz fungerer.

[ ] Poengberegning fungerer.

[ ] Tekstinput fungerer.

[ ] PDF-input fungerer.

[ ] Lokal modus fungerer.

[ ] Gemini-modus er dokumentert.

[ ] Gemini-personvern er dokumentert.

[ ] DEC-003 er korrekt.

[ ] Faste syntetiske testnotater finnes.

[ ] Testene består.

[ ] README er kontrollert.

[ ] Appen er testet uten API-nøkkel.

[ ] Promptarkivet er kontrollert.

[ ] Denne hovedprompten er loggført.

[ ] Alle tilgjengelige oppfølgingsprompts er loggført.

[ ] Historiske prompt-hull er dokumentert.

[ ] GitHub-repository er ryddig.

[ ] Ingen hemmeligheter er committet.

[ ] Faglærerens kommentarer er vurdert.

[ ] Kjente begrensninger er dokumentert.

[ ] Full oppgavetekst er kontrollert dersom tilgjengelig.

[ ] Endelige innleveringskrav er kontrollert dersom tilgjengelig.

[ ] Sluttrapport er ferdig.

[ ] Alle relevante endringer er testet.

[ ] Pull Request er opprettet.

Marker bare punkter som fullført når det finnes bevis.

---

# 15. GIT-COMMITS OG PULL REQUEST

Når revisjon, rettelser og dokumentasjon er ferdig:

1. Kontroller git status.
2. Undersøk alle endringer.
3. Kontroller at ingen hemmeligheter eller uønskede filer er inkludert.
4. Kontroller at .memlog.md er helt urørt.
5. Kontroller promptarkivet.
6. Kjør full testsuite.
7. Kjør dokumentasjonstester.
8. Kjør git diff --check.
9. Stage kun relevante, gjennomgåtte filer.
10. Lag logiske commits.

Foreslått commitstruktur:

- docs: audit IBE160 requirements and teacher feedback
- test: strengthen synthetic fixtures and regression coverage
- fix: resolve final MVP quality issues
- docs: finalize README BMAD and submission evidence
- docs: archive Codex final audit prompt and results

Bruk bare commits som faktisk er nødvendige.

Push branchen til origin.

Opprett én Pull Request mot main.

Foreslått PR-tittel:

chore: complete IBE160 final quality audit and submission readiness

PR-beskrivelsen skal inkludere:

- Formål.
- Oppsummering av funn.
- Implementerte rettelser.
- Dokumentasjonsendringer.
- Testresultater.
- Faglærerkrav.
- Promptlogging.
- Sikkerhetskontroller.
- Kjente begrensninger.
- Gjenstående manuelle oppgaver.

Ikke merge PR-en.

Jeg skal selv ta beslutningen om merge etter gjennomgang.

---

# 16. SLUTTRAPPORT TIL MEG

Når arbeidet er gjennomført, skal du gi en tydelig rapport på norsk.

Rapporten skal inneholde:

## A. GitHub-status

- Branch.
- Commit-ID-er.
- PR-lenke.
- Mergeability.
- Om branchen er ren.

## B. Funksjonalitet

- Hva som fungerer.
- Hva som ble rettet.
- Hva som fortsatt mangler.

## C. Tester

- Antall beståtte tester.
- Antall feilede tester.
- Dokumentasjonstester.
- Nye tester.
- Eventuelle tester som ikke kunne kjøres.

## D. BMAD og dokumentasjon

- Status for product brief.
- Status for PRD.
- Status for arkitektur.
- Status for epics og stories.
- Status for beslutningslogger.
- Status for sporbarhet.

## E. Prompt-historikk

- Hvor denne hovedprompten er arkivert.
- Hvilket nummer den fikk.
- Om originalteksten er bevart ordrett.
- Status for tidligere prompts.
- Status for PROMPT 027.
- Status for PROMPT_HISTORY_GAPS.md.
- Status for Gemini-promptmalene.
- Eventuelle manglende originaltekster.

## F. Faglærerens vurderingskriterier

Rapporter status for:

1. Prosess og KI-styring – 30 %.
2. Funksjonalitet og omfang – 20 %.
3. Kvalitetssikring og testing – 15 %.
4. Design og brukeropplevelse – 10 %.
5. Kodekvalitet og arkitektur – 10 %.
6. README og kjørbarhet – 10 %.
7. Ryddighet i repository – 5 %.

Bruk PASS, PARTIAL, FAIL eller NOT VERIFIED.

## G. Innleveringsklarhet

Svar eksplisitt:

1. Er MVP teknisk ferdig?
2. Er alle tilgjengelige faglærerkommentarer håndtert?
3. Er dokumentasjonen konsistent med koden?
4. Kan sensor kjøre appen uten API-nøkkel?
5. Er promptarkivet så komplett som tilgjengelige kilder tillater?
6. Er det uløste kritiske feil?
7. Er prosjektet klart til å demonstreres?
8. Er prosjektet klart til innlevering ut fra de kravene som faktisk er tilgjengelige?
9. Hvilke krav kan ikke verifiseres?
10. Hva må gruppen eventuelt gjøre manuelt?

Ikke bruk prosenttall for prosjektets ferdigstillelse uten en dokumentert beregningsmetode.

---

# 17. DEFINISJON AV FERDIG

Arbeidet er ferdig når:

- Alle tilgjengelige krav er kartlagt.
- Faglærerens tilbakemelding er gjennomgått.
- Alle forsvarlig rettbare, relevante mangler er håndtert.
- Alle testresultater er dokumentert.
- README er verifisert så langt miljøet tillater.
- BMAD-dokumentasjonen er konsistent med koden.
- Promptarkivet er kontrollert.
- Denne hovedprompten er arkivert når originalteksten er tilgjengelig.
- Kjente historiske hull er bevart og synlige.
- Sikkerhetskontrollene er gjennomført.
- En fullstendig sluttrapport finnes.
- Endringene er committet og pushet.
- Én Pull Request er opprettet mot main.
- PR-en er ikke merget.

Dersom noe ikke kan fullføres, skal du dokumentere nøyaktig hva som hindrer det.

Ikke skjul mangler.

Ikke fabriker tester eller dokumentasjon.

Ikke hev at prosjektet er formelt godkjent av faglærer.

Ikke hev at Gemini er godkjent for produksjonsbruk.

## START NÅ

Start med å:

1. Verifisere repository og origin/main.
2. Opprette en trygg, separat worktree.
3. Undersøke eksisterende promptarkiv.
4. Arkivere denne hovedprompten ordrett dersom tilgjengelig.
5. Kartlegge krav og eksisterende dokumentasjon.
6. Gjennomføre revisjonen systematisk.
7. Rette konkrete mangler.
8. Kjøre full sluttverifisering.
9. Oppdatere promptlogg og sluttrapport.
10. Opprette Pull Request uten å merge.

Arbeid selvstendig og systematisk gjennom alle trygge steg.

Ikke stopp etter planlegging eller første funn.

Lever et faktisk kvalitetssikret resultat med spor
```
