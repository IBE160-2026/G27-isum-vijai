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
- **Alternativer:** Ikke kartlagt; gruppen må vurdere aktuelle alternativer.
- **Beslutning:** Ikke besluttet.
- **Begrunnelse:** Brief og tilbakemelding oppgir ingen valgt tjeneste.
- **Konsekvenser:** Uavklart.
- **Dato:** Ikke besluttet.
- **Status:** Uavklart.

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
- **Dato:** Ikke besluttet.
- **Status:** Uavklart.

## Prosessbeslutning – PROMPT 024/025-avgrenset review (2026-10-25)

- **Problemstilling:** Den installerte Build Step 04-reviewen ber om alle aktive lag, og Blind Hunter-instruksen har en beregnet funnkvote. For F-07/F-10-diffen fant Blind Hunter ett reelt lavprioritetsforslag, men kunne ikke dokumentere flere uten spekulasjon.
- **Prosessvalg:** Brukeren godkjente en separat, avgrenset gjennomgang med installert `bmad-review`-arbeidsflyt og relevante lag, uten å konstruere funn. Verification Gap ble kjørt som valgt `bmad-review`-linse; Acceptance Auditor ble kjørt separat fra den installerte `bmad-code-review`-konfigurasjonen.
- **Begrunnelse:** Beholde faktiske, etterprøvbare funn og la de relevante kontrollene vurdere akseptansekriteriene.
- **Resultat:** Verification Gap fant ingen gap; Acceptance Auditor fant ingen avvik. F-07 og F-10 er lukket. Dette endrer ikke produktbeslutningene DEC-001–DEC-005, som fortsatt er `Uavklart`.
- **Begrensning:** Dette er ikke en fullføring av Build Step 04. Den ber fortsatt om alle aktive reviewlag, og den installerte Build-ruten tilbyr ikke valg av delmengde. Den første Build-reviewens Blind Hunter-kvote ble ikke oppfylt. Prosessbeslutningen om å kjøre separat avgrenset review er godkjent; et unntak som lar den erstatte Build Step 04 for å sette storyen til `done`, er ikke vedtatt. Storyen forblir `in-progress`.
- **Dato:** 2026-10-25.
