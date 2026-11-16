# PROMPT 032 – Sluttkontroll og forbedring av README.md (IBE160)

- **Dato:** 2026-11-16.
- **Formål:** Kontrollere README mot implementasjonen og sensorens kjørbarhetsbehov; forbedre setup-, brukerveilednings-, test-, prosjektstruktur- og feilsøkingsdokumentasjon uten kodeendringer.
- **Kilde:** Full brukerprompt fra denne Codex-samtalen; originalteksten er nedenfor i en `text`-fence.
- **Branch/worktree:** `docs/readme-sensor-setup-audit`, `/private/tmp/G27-isum-vijai-readme-audit`.
- **Resultat/filer/tester/commit/PR:** Oppdateres etter gjennomgang. Ingen commit eller push før brukerens godkjenning.

## Original prompt

```text
# G27 – Sluttkontroll og forbedring av README.md (IBE160)

Du arbeider i GitHub-repositoryet:

https://github.com/IBE160-2026/G27-isum-vijai

## Mål

Kontroller og forbedre `README.md` slik at prosjektet oppfyller sensorveiledningen for IBE160 høsten 2026, særlig kriterium 6: **README og kjørbarhet (10 %)**.

Sensor skal kunne klone prosjektet og starte applikasjonen på en ren maskin ved å følge README, uten muntlige forklaringer eller hjelp fra gruppen.

Ikke skriv en generell README. Undersøk den faktiske koden, prosjektstrukturen, avhengighetene og testene før du gjør endringer.

## 1. Undersøk prosjektet først

Les og kontroller:

- Eksisterende `README.md`.
- `requirements.txt` og eventuelle andre avhengighetsfiler.
- Streamlit-applikasjonens faktiske startfil.
- Python-versjon og nødvendige pakker.
- Gemini-integrasjon og miljøvariabler.
- Lokal demonstrasjonsmodus uten API-nøkkel.
- PDF-opplasting og begrensninger.
- Quizfunksjonalitet.
- Testfiler og dokumenterte testkommandoer.
- Relevante BMAD-dokumenter, beslutningslogger og promptlogger.
- Git-status, branches og Pull Requests.

Ikke anta at tidligere dokumentasjon er korrekt. Kontroller påstandene mot den faktiske implementasjonen.

## 2. README skal inneholde

### A. Prosjektbeskrivelse

Forklar kort:

- Hva applikasjonen gjør.
- Hvem den er laget for.
- Hvilket problem den forsøker å løse.
- At prosjektet er en prototype utviklet i IBE160.
- Hvilke funksjoner som fungerer lokalt, og hvilke som krever Gemini.

### B. Teknologistakk

Dokumenter de teknologiene som faktisk brukes, for eksempel Python, Streamlit, pypdf, Gemini og testverktøy.

Ikke oppgi teknologier som ikke brukes i prosjektet.

### C. Installasjon på en ren maskin

Gi eksakte kommandoer som kan kopieres.

README skal forklare:

1. Hvordan repositoryet klones.
2. Hvordan brukeren går inn i prosjektmappen.
3. Hvilken Python-versjon som kreves eller er testet.
4. Hvordan et virtuelt miljø opprettes.
5. Hvordan miljøet aktiveres på Windows, macOS og Linux.
6. Hvordan avhengighetene installeres.
7. Hvordan Streamlit startes.
8. Hvilken lokal adresse brukeren åpner.

Kontroller riktig startkommando fra repositoryet. Ikke gjett filnavnet.

### D. Oppstart uten Gemini API-nøkkel

Dette er spesielt viktig.

Sensor skal kunne demonstrere applikasjonen uten å opprette en API-nøkkel.

Forklar tydelig:

- Hvordan lokal modus velges.
- Hvilke funksjoner som fungerer uten nøkkel.
- Hvilke begrensninger lokal modus har.
- At lokal quiz bruker faste demonstrasjonsdata dersom dette fortsatt stemmer med implementasjonen.

Ikke påstå at lokal quiz genereres dynamisk fra brukerens notater.

### E. Valgfri Gemini-modus

Forklar:

- Hvordan Gemini aktiveres.
- Hvilken miljøvariabel som brukes for API-nøkkel.
- Hvordan modellnavnet konfigureres med `GEMINI_MODEL`, dersom dette fortsatt gjelder.
- Hvordan konfigurasjon håndteres uten at hemmeligheter legges i GitHub.
- At eksterne API-kall kan medføre kostnader og kreve nettverkstilgang.
- At Gemini-modus er valgfri.

Ikke kjør ekte Gemini-forespørsler eller bruk en virkelig API-nøkkel under denne kontrollen.

### F. Brukerveiledning

Beskriv trinnvis hvordan brukeren:

1. Starter applikasjonen.
2. Skriver inn forelesningsnotater eller laster opp en PDF.
3. Velger tilgjengelig modus.
4. Får sammendrag og sentrale begreper.
5. Bruker quizfunksjonen.
6. Får tilbakemelding og poengsum.

Beskriv bare funksjoner som faktisk finnes.

### G. Begrensninger

Dokumenter tydelig:

- At løsningen er en prototype.
- At PDF-støtten gjelder maskinlesbar tekst.
- At OCR ikke støttes, dersom dette fortsatt gjelder.
- At lokal demonstrasjonsmodus har begrenset funksjonalitet.
- At KI-genererte svar kan inneholde feil.
- At sitatkontroll ikke garanterer semantisk korrekthet.
- At Gemini ikke skal brukes med personopplysninger eller konfidensielle notater i denne prototypen, i tråd med DEC-003.

### H. Testing

Dokumenter nøyaktig hvordan sensor kjører testene.

Kontroller hvilke kommandoer som fungerer i det aktuelle repositoryet.

Forklar forskjellen mellom:

- Automatiserte tester.
- Tester med mockede Gemini-svar.
- Manuelle tester.
- Eventuell testing som krever ekstern tjeneste.

Ikke oppgi historiske testtall som nåværende resultater uten å kjøre testene på nytt.

### I. Prosjektstruktur

Lag en kort og korrekt oversikt over sentrale mapper og filer.

Inkluder relevante lenker til:

- Product brief.
- BMAD-dokumentasjon.
- Beslutningslogg.
- Testplan og testlogg.
- Promptarkiv.
- Dokumentasjon av kjente begrensninger.

Kontroller at alle relative lenker fungerer.

### J. Feilsøking

Lag en kort feilsøkingsseksjon for vanlige problemer, basert på faktiske avhengigheter og feiltilstander:

- Python-versjon.
- Manglende pakker.
- Problemer med virtuelt miljø.
- Streamlit starter ikke.
- PDF kan ikke leses.
- Gemini-nøkkel mangler.
- Gemini-tjenesten er utilgjengelig.

Ikke finn på feilmeldinger eller løsninger som ikke er kontrollert.

## 3. Gjennomfør en ren installasjonstest

Bruk et isolert miljø.

Test så langt miljøet tillater:

1. Installasjon med README-instruksjonene.
2. Oppstart uten Gemini API-nøkkel.
3. At Streamlit-serveren svarer.
4. Lokal demonstrasjonsmodus.
5. Tekstinput og PDF-behandling.
6. Quizflyt.
7. Feilhåndtering ved ugyldig input.
8. Dokumenterte automatiserte tester.

Dersom grafisk testing ikke er tilgjengelig, skal dette oppgis eksplisitt. Ikke påstå at hele brukergrensesnittet er visuelt testet bare fordi HTTP-endepunktet svarer.

Rapporter hva som faktisk ble testet, og hva som ikke kunne testes.

## 4. Kontroller sensorveiledningens øvrige krav

Gjør også en begrenset gjennomgang av følgende kriterier, uten å endre applikasjonskoden:

- Prosess og KI-styring (30 %).
- Funksjonalitet og omfang (20 %).
- Kvalitetssikring og testing (15 %).
- Design og brukeropplevelse (10 %).
- Kodekvalitet og arkitektur (10 %).
- Ryddighet i repositoryet (5 %).

Gi en kort status for hvert kriterium med konkrete filreferanser og eventuelle mangler.

Ikke tildel en sikker karakter uten tilstrekkelig dokumentasjon.

## 5. Viktige sikkerhetsregler

- Ikke endre applikasjonskoden.
- Ikke endre eller les private filer som `.memlog.md` eller `.streamlit/secrets.toml`.
- Ikke legg til API-nøkler, tokens eller passord.
- Ikke slett filer eller overskriv andres arbeid.
- Ikke rekonstruer manglende historiske prompts.
- Ikke endre gruppens godkjente refleksjonsrapport.
- Ikke opprett unødvendige filer.
- Ikke gjør endringer direkte på `main`.
- Ikke merge Pull Requests automatisk.
- Ikke påstå at en kontroll er gjennomført dersom den ikke faktisk ble utført.

## 6. Git og levering

Før endringer:

1. Kontroller arbeidsområdet og Git-status.
2. Undersøk om det finnes ucommittede endringer.
3. Kontroller siste `origin/main`.
4. Opprett en egen branch fra oppdatert `main`, uten å overskrive lokalt arbeid.

Gjennomfør deretter bare nødvendige README-forbedringer.

Kjør `git diff --check` og kontroller at alle dokumentasjonslenker fungerer.

Vis endringene og testresultatene før commit.

**Ikke push eller opprett Pull Request før jeg har godkjent endringene.**

## 7. Sluttrapport til meg

Svar med:

1. Hva som var feil eller manglet i README.
2. Hva du har forbedret.
3. Eksakte kommandoer sensor skal bruke.
4. Resultater fra ren installasjon.
5. Resultater fra automatiserte tester.
6. Eventuelle feil eller begrensninger.
7. Status opp mot alle sju vurderingskriteriene.
8. Hvilke filer som er endret.
9. Om prosjektet er klart for sensors gjennomgang.

Vær presis og kritisk. Ikke skriv at alt er perfekt dersom du finner mangler.

**Viktigste mål: Sensor skal kunne følge README og få G27-applikasjonen til å kjøre uten hjelp fra gruppen.**
```
