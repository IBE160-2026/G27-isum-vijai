# Beslutningslogg

Registrer beslutninger først etter at gruppen har tatt dem. Forslag i produktbrief eller tilbakemelding er ikke automatisk vedtak.

## Mal

### [DEC-XXX] Kort tittel

- **Problemstilling:**
- **Alternativer:**
- **Beslutning:** Ikke besluttet
- **Begrunnelse:**
- **Konsekvenser:**
- **Dato:** Ikke besluttet
- **Status:** Uavklart

## Åpne beslutninger

### [DEC-001] Interaktiv quiz

- **Problemstilling:** Skal studenten kunne svare på quiz i appen, få tilbakemelding og poengsum?
- **Alternativer:** Kun vise spørsmål og fasit; interaktiv quiz med poengsum; annet valg fra gruppen.
- **Beslutning:** Ikke besluttet.
- **Begrunnelse:** Tilbakemeldingen foreslår interaktiv quiz; briefen krever quiz med fasit, men fastsetter ikke interaksjon.
- **Konsekvenser:** Avhenger av valgt løsning.
- **Dato:** Ikke besluttet.
- **Status:** Uavklart.

### [DEC-002] Lagring per emne

- **Problemstilling:** Skal sammendrag og quiz lagres per emne eller forelesning?
- **Alternativer:** Ingen varig lagring; enkel lagring per emne/forelesning; annet valg fra gruppen.
- **Beslutning:** Ikke besluttet.
- **Begrunnelse:** Tilbakemeldingen foreslår lagring. Briefen ønsker å begrense lagring i v1.
- **Konsekvenser:** Avhenger av valgt løsning, inkludert behov for innlogging og personvernvalg.
- **Dato:** Ikke besluttet.
- **Status:** Uavklart.

### [DEC-003] KI-tjeneste

- **Problemstilling:** Hvilken KI-tjeneste/modell skal brukes, og hvordan håndteres nøkkel og kostnad?
- **Alternativer vurdert:** Ingen ekstern KI i prototypen; valgfri Gemini-prototypebruk med strenge databegrensninger; eventuell senere produksjonsbruk etter ny vurdering.
- **Beslutning (2026-11-16):**
  - **A. Godkjent prototypebruk:** Gemini godkjennes som et valgfritt prototypevalg bare for syntetiske, offentlig tilgjengelige eller anonymiserte notater som ikke inneholder personopplysninger eller konfidensielt innhold. Før hvert eksternt kall skal brukeren ha synlig informasjon og aktivt samtykke, og selv starte genereringen. Lokal modus skal fungere uten Gemini. API-nøkler og Secrets skal ikke lagres i Git.
  - **B. Ikke-godkjent produksjonsbruk:** Produksjonsbruk med personopplysninger er ikke godkjent. Beslutningen gir heller ikke generell godkjenning for konfidensielt, sensitivt eller annet ikke-offentlig kursmateriale.
  - **C. Krever ny beslutning:** Produksjonsbruk, personopplysninger, behandling av konfidensielt innhold, datalagring/sletting, kostnadsansvar, leverandørvilkår, emne-/institusjonskrav og eventuelle endringer av datagrensene må vurderes særskilt før slik bruk.
- **Begrunnelse:** Prototypen kan prøves med lavrisiko-notater når brukeren vet at innholdet sendes til Google, godkjenner behandlingen og starter handlingen. Avgrensningen gir ikke grunnlag for å hevde juridisk, institusjonell eller formell gruppe-/emnegodkjenning.
- **Konsekvenser:** Gemini forblir valgfritt; lokal modus er tilgjengelig uten tjenesten. Brukere skal få tydelig beskjed om ekstern behandling og begrenset databruk. Det loves ikke gratis bruk, lagringstid eller sletting uten dokumentasjon som støtter det. Gjeldende leverandørvilkår og eventuelle emnekrav må følges. Ingen produksjonsgodkjenning følger av denne beslutningen.
- **Dato:** 2026-11-16.
- **Status:** Avgrenset prototypebruk godkjent etter brukerens uttrykkelige beslutning; produksjonsbruk og forholdene i punkt C er ikke godkjent og krever ny beslutning.

### [DEC-004] Testmodus

- **Problemstilling:** Hvordan skal sensor kunne kjøre kjerneflyten uten gruppens API-nøkkel?
- **Alternativer:** Ferdige eksempelsvar/mock; lokal testimplementasjon; annet valg fra gruppen.
- **Beslutning:** Ikke besluttet.
- **Begrunnelse:** Tilbakemeldingen anbefaler testmodus med ferdige eksempelsvar, men ingen løsning er vedtatt.
- **Konsekvenser:** Uavklart.
- **Dato:** Ikke besluttet.
- **Status:** Uavklart.

### [DEC-005] Teknologistakk

- **Problemstilling:** Hvilke språk, rammeverk, lagring og PDF-verktøy skal brukes?
- **Alternativer:** Ikke kartlagt; velges etter gruppens behov og kompetanse.
- **Beslutning:** Ikke besluttet.
- **Begrunnelse:** Tilbakemeldingen bekrefter at briefen ikke har teknologivalg.
- **Konsekvenser:** Uavklart.
- **Dato for øvrige valg:** Ikke besluttet.
- **Avgrenset delbeslutning (2026-11-15):** Gruppen har godkjent `pypdf` som PDF-verktøy for lokalt tekstuttrekk fra maskinlesbare PDF-er i MVP-ens eksisterende Streamlit-app. Ingen OCR eller ekstern PDF-behandlingstjeneste inngår i denne funksjonen. **Kilde:** Brukerens eksplisitte opplysning og godkjenning i MVP SPRINT 001-instruksjonen 2026-11-15. Ingen møtereferat, deltakere eller tidligere godkjenningstidspunkt er oppgitt.
- **Status:** Delbeslutningen om PDF-verktøy er godkjent; DEC-005 som helhet forblir `Uavklart` for øvrige språk-, rammeverk- og teknologistakkvalg.

## Foreløpige implementeringsvalg – MVP SPRINT 002 (2026-11-15)

Brukeren oppga følgende valg for implementeringen i denne sprinten. Kilden er brukerens instruksjon 2026-11-15; dette dokumenterer ikke et formelt gruppevedtak eller møtereferat:

- Gemini Developer API med `google-genai`; modell konfigurerbar. Dette er et foreløpig teknologivalg, og ikke en avslutning av DEC-003. Kostnadsansvar og tillatt dataflyt må avklares før produksjonsbruk.
- Sammendragslengde kort/middels/lang; quizantall 1–10 med standard 5; vanskelighetsgrad lett/middels/vanskelig med standard middels.
- Quizformat i implementeringsprototypen: flervalg med nøyaktig fire alternativer, ett riktig svar, fasit og kort forklaring. Spørsmål, svar og forklaringer skal være forankret i notatene; ved utilstrekkelig grunnlag skal appen varsle i stedet for å finne på innhold.
- Eksterne Gemini-kall krever synlig personverninformasjon og aktiv bekreftelse; automatiserte tester bruker mocks og ingen ekte studentnotater. Resultatets sammendrag, begreper, spørsmål, svar og forklaringer må inkludere tekstlige sitater fra notatene som valideres før visning.

**Status:** Foreløpige valg for implementering, ikke formelt gruppevedtak. DEC-001–DEC-005 beholder eksisterende status; DEC-003 forblir uavklart om leverandørgodkjenning, kostnad, dataflyt og oppbevaring. PRD forblir `draft`.

**Implementeringsspor (2026-11-15):** Prototypen bruker Gemini Developer API gjennom Googles offisielle `google-genai` SDK. SDK-bruk og strukturert JSON-utdata følger [Google Gen AI SDK-dokumentasjonen](https://googleapis.github.io/python-genai/) og [Gemini structured output-dokumentasjonen](https://ai.google.dev/gemini-api/docs/structured-output). Dette er implementasjon av det foreløpige brukeroppgitte valget, ikke gruppevedtak. Modellnavn kan settes med `GEMINI_MODEL`; nøkkel leses fra `GEMINI_API_KEY` eller Streamlit Secrets. DEC-003 forblir åpen om produksjonsgodkjenning, kostnadsansvar og dataflyt.

**Statusoppdatering (2026-11-16):** Den uttrykkelige, avgrensede prototypebeslutningen ovenfor erstatter eldre formuleringer om at Gemini-bruk overhodet ikke var besluttet. Den utvider ikke godkjenningen til produksjon, personopplysninger eller konfidensielt innhold.

## Prosessbeslutning – PROMPT 024/025-avgrenset review (2026-10-25)

- **Problemstilling:** Den installerte Build Step 04-reviewen ber om alle aktive lag, og Blind Hunter-instruksen har en beregnet funnkvote. For F-07/F-10-diffen fant Blind Hunter ett reelt lavprioritetsforslag, men kunne ikke dokumentere flere uten spekulasjon.
- **Prosessvalg:** Brukeren godkjente en separat, avgrenset gjennomgang med installert `bmad-review`-arbeidsflyt og relevante lag, uten å konstruere funn. Verification Gap ble kjørt som valgt `bmad-review`-linse; Acceptance Auditor ble kjørt separat fra den installerte `bmad-code-review`-konfigurasjonen.
- **Begrunnelse:** Beholde faktiske, etterprøvbare funn og la de relevante kontrollene vurdere akseptansekriteriene.
- **Resultat:** Verification Gap fant ingen gap; Acceptance Auditor fant ingen avvik. F-07 og F-10 er lukket. Dette endrer ikke produktbeslutningene DEC-001–DEC-005, som fortsatt er `Uavklart`.
- **Begrensning:** Dette er ikke en fullføring av Build Step 04. Den ber fortsatt om alle aktive reviewlag, og den installerte Build-ruten tilbyr ikke valg av delmengde. Den første Build-reviewens Blind Hunter-kvote ble ikke oppfylt. Prosessbeslutningen om å kjøre separat avgrenset review er godkjent; et unntak som lar den erstatte Build Step 04 for å sette storyen til `done`, er ikke vedtatt. Storyen forblir `in-progress`.
- **Dato:** 2026-10-25.
