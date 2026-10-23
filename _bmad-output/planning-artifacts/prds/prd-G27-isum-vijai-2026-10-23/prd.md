---
title: "Foredragsnotater → Sammendrag & Quizgenerator"
status: draft
created: 2026-10-23
updated: 2026-10-23
---

# PRD: Foredragsnotater → Sammendrag & Quizgenerator

## 0. Dokumentformål og kilder

Dette dokumentet beskriver produktkrav for gruppen og for senere BMAD-arbeid med UX, arkitektur, stories og implementasjon. Krav merket **Bekreftet** er hentet fra Product Brief. Lærerens råd og mulige utvidelser er merket **Forslag** inntil gruppen vedtar dem. Uavklarte valg står i §9. Ingen teknologistakk eller eksterne tjenester er vedtatt.

Kilder: [`product-brief.md`](../../../../product-brief.md), [`tilbakemelding-product-brief.md`](../../../../tilbakemelding-product-brief.md), [`docs/PROJECT_CONTEXT.md`](../../../../docs/PROJECT_CONTEXT.md), [`docs/decisions/DECISION_LOG.md`](../../../../docs/decisions/DECISION_LOG.md) og [`docs/bmad/WORKFLOW_STATUS.md`](../../../../docs/bmad/WORKFLOW_STATUS.md). Kildeangivelser i kravene viser til disse dokumentene og deres overskrifter.

## 1. Visjon

Studenter skal kunne gå fra egne forelesningsnotater til strukturert repetisjonsmateriale i én tydelig arbeidsflyt. Produktet tar imot tekst eller PDF, lar studenten angi ønsket sammendragslengde, quizvanskelighetsgrad og antall spørsmål, og viser et sammendrag, sentrale begreper og quiz med fasit.

Produktet skal støtte aktiv repetisjon uten å fremstille KI-generert innhold som garantert korrekt. Studenten skal kunne forstå at materialet er laget fra egne notater og gå tilbake til kilden. Dette følger Product Briefs «The Solution», «What Makes This Different» og «Success Criteria».

## 2. Målgruppe og brukerbehov

### 2.1 Primærbruker

En student med digitale forelesningsnotater som vil repetere stoff raskere og kontrollere egen forståelse. Kilden er Product Brief, «Who This Serves».

### 2.2 Brukerbehov

- Gjøre notater i tekst- eller PDF-format om til læringsressurser.
- Velge lengden på sammendraget, vanskelighetsgraden og antallet quizspørsmål.
- Få en oversiktlig begrepsliste og quiz med fasit.
- Forstå når kildedokumentet ikke kan behandles.
- Kunne se at resultatet bygger på de innsendte notatene og bruke originalmaterialet som referanse.

## 3. Begreper

- **Notater:** Tekst eller PDF med forelesningsmateriale som studenten gir produktet.
- **Sammendrag:** Kortere, strukturert framstilling av hovedinnholdet i notatene.
- **Begrepsliste:** Liste over sentrale begreper fra notatene.
- **Quiz:** Spørsmål laget fra notatene, med tilhørende fasit. Interaktiv besvarelse er ikke bekreftet krav.
- **Genereringsjobb:** Én behandling av studentens input med valgte innstillinger, fra innsending til resultat eller feilmelding.
- **Lesbar PDF:** PDF som kan behandles av den valgte tekstuttrekksløsningen. Om dette begrenses til maskinlesbar tekst eller også omfatter skannede sider er uavklart.
- **Resultat:** Generert sammendrag, begrepsliste, quiz og fasit fra én genereringsjobb.
- **Fasit:** Oppgitte riktige svar til quizspørsmålene.
- **Testmodus:** Foreslått kjøring med lokale eksempelresultater uten ekstern KI-nøkkel; dette er ikke vedtatt.

## 4. Brukerreise

- **UJ-1. Studenten lager repetisjonsmateriale fra forelesningsnotater.** [ASSUMPTION: Dette er en rollebasert reise fra Product Brief; ingen navngitt persona eller brukerundersøkelse er dokumentert.] Studenten velger å lime inn tekst eller laste opp en PDF, oppgir ønsket sammendragslengde, quizvanskelighetsgrad og antall spørsmål, starter genereringen og får vist sammendrag, begrepsliste, quiz og fasit. Hvis dokumentet ikke kan behandles, får studenten en tydelig beskjed og kan prøve igjen med annet materiale.

Reisen gjengir flyten i Product Brief, «The Solution» og «Success Criteria». Konto, lagring, plattform og interaktiv quizzing er ikke forutsatt.

## 5. Funksjoner og funksjonelle krav

### 5.1 Legge inn og behandle notater

**Kilde:** Product Brief, «The Solution», «Scope – IN» og «Success Criteria».

#### FR-1: Tekstinput

Studenten kan lime inn forelesningsnotater som tekst for behandling.

**Testbare konsekvenser:**
- Innlimt, ikke-tom tekst kan sendes gjennom genereringsflyten.
- Tom tekst gir en forståelig valideringsmelding og starter ikke generering.

#### FR-2: PDF-input

Studenten kan laste opp forelesningsnotater i PDF-format for behandling.

**Testbare konsekvenser:**
- En lesbar PDF kan sendes gjennom genereringsflyten.
- En fil som ikke kan leses eller behandles gir en tydelig feilmelding.

**Åpent:** OCR for skannede PDF-er er ikke spesifisert i briefen og inngår ikke som krav her.

### 5.2 Velge genereringsinnstillinger

**Kilde:** Product Brief, «The Solution», «Scope – IN» og «Success Criteria».

#### FR-3: Sammendragslengde

Studenten kan velge ønsket lengde på sammendraget før generering.

**Testbare konsekvenser:**
- Valgt lengde brukes som innstilling i samme genereringsjobb.
- Grensesnittet viser hvilke valg som er tilgjengelige. Selve valgalternativene må bestemmes i UX/arkitektur.

#### FR-4: Quizinnstillinger

Studenten kan velge quizens vanskelighetsgrad og ønsket antall spørsmål før generering.

**Testbare konsekvenser:**
- Valgt vanskelighetsgrad og antall sendes med genereringsjobben.
- Resultatet inneholder det valgte antallet spørsmål når innholdet kan genereres. Grenseverdier for tillatt antall må fastsettes før implementasjon.

### 5.3 Generere og vise læringsressurser

**Kilde:** Product Brief, «The Solution», «Scope – IN», «What Makes This Different» og «Success Criteria».

#### FR-5: Sammendrag og begrepsliste

Produktet genererer et sammendrag og en liste over sentrale begreper fra studentens notater.

**Testbare konsekvenser:**
- Et vellykket resultat har separate, identifiserbare sammendrags- og begrepslistedeler.
- Innholdet vises sammen med eller i samme resultatvisning som de øvrige genererte ressursene.

#### FR-6: Quiz og fasit

Produktet genererer quizspørsmål fra notatene og gir studenten tilgang til fasit.

**Testbare konsekvenser:**
- Hvert generert spørsmål vises som et avgrenset spørsmål.
- Fasit er tilgjengelig for spørsmålene.
- Briefen fastsetter ikke quizformat, så flervalg eller fritekst er et åpent valg.

#### FR-7: Oversiktlig resultatvisning

Produktet presenterer sammendrag, begrepsliste, quiz og fasit på en oversiktlig måte.

**Testbare konsekvenser:**
- En testbruker kan finne alle fire resultatdelene etter fullført generering uten hjelp, i tråd med briefens suksesskriterium.
- Resultatet gjør det tydelig at ressursene er generert fra studentens notater og ikke er garantert feilfrie.

### 5.4 Feil og gjenoppretting

**Kilde:** Product Brief, «Success Criteria»; lærerens tilbakemelding, «Plan for språkmodellen» og testbarhetsråd.

#### FR-8: Forståelige feilbeskjeder

Produktet gir studenten en tydelig beskjed når et dokument ikke kan behandles eller en generering ikke lykkes.

**Testbare konsekvenser:**
- Ugyldige eller uleselige dokumenter og tom input kan testes og gir synlig, forståelig tilbakemelding.
- Teknisk feil viser ikke hemmeligheter, API-nøkler eller intern feildetalj til brukeren.

### 5.5 Forslag som krever gruppevedtak

Forslag til utvidelser og deres status står samlet i §7.2. Ingen av dem er krav fra gjeldende Product Brief.

## 6. Ikke-funksjonelle krav og guardrails

### 6.1 Kvalitet og kildebinding

- **NFR-1:** Generert innhold skal være basert på notatene som er gitt produktet (Product Brief, «Success Criteria»). Briefen fastsetter ikke en målemetode. Lærerens eksempel «ingen quizspørsmål om noe som ikke står i notatene» er et forslag som må godkjennes og konkretiseres i testkriterier.
- **NFR-2:** Produktet skal ikke love at KI-generert innhold alltid er korrekt (Product Brief, «What Makes This Different»).
- **NFR-3:** Full arbeidsflyt skal kunne gjennomføres av en testbruker uten hjelp (Product Brief, «Success Criteria»). Hvilket testoppsett som brukes, er åpent.

### 6.2 Personvern og sikkerhet

- **NFR-4:** Ikke legg API-nøkler eller andre hemmeligheter i klienten eller versjonskontroll. Lærerens tilbakemelding anbefaler nøkkel i `.env` utenfor Git; den konkrete implementasjonen må bestemmes i arkitektur.
- **NFR-5:** Begrens lagring av notater til det som er nødvendig for arbeidsflyten, i tråd med Product Brief, «Scope».
- **NFR-6:** Hvis kursbeskyttet materiale lagres eller knyttes til en bruker, må innlogging og hensiktsmessig håndtering av materialet inngå. Det er en betingelse i briefen, ikke et krav om innlogging i en løsning uten slik lagring.
- **NFR-7:** Det er ikke bestemt om notater sendes til en ekstern KI-tjeneste, hvilken tjeneste som i så fall brukes, eller hvor lenge data oppbevares. Dette må avklares før produksjonsbruk.

## 7. MVP-omfang

### 7.1 Bekreftet minimum fra Product Brief

- Ta imot notater som tekst eller PDF.
- La studenten velge sammendragslengde, quizvanskelighetsgrad og antall spørsmål.
- Generere sammendrag, sentrale begreper og quiz med fasit fra notatene.
- Vise resultatene oversiktlig.
- Gi forståelig tilbakemelding dersom et dokument ikke kan behandles.
- Begrense lagring til det som er nødvendig for arbeidsflyten.

### 7.2 Forslag til utvidet MVP – krever godkjenning

Lærerens tilbakemelding mener kjerneomfanget alene er lite, og anbefaler minst én utvidelse. Gruppen må velge om utvidet MVP skal inkludere interaktiv quiz med poengsum, kildehenvisning per spørsmål eller lagring per emne/forelesning. Dette PRD-et velger ikke mellom alternativene. Lagring har personvern- og innloggingskonsekvenser.

**Foreslått utvalgskriterium, ikke vedtatt:** Velg den utvidelsen gruppen kan demonstrere og teste med godkjente testnotater innen tilgjengelig tid, og vurder samtidig personvern- og lagringskonsekvensene. Gruppen må dokumentere valg og begrunnelse i beslutningsloggen før utvidelsen blir implementeringskrav.

Testmodus uten API-nøkkel og faste testnotater anbefales i tilbakemeldingen for kjørbarhet og kvalitetssikring, men krever også en konkret gruppebeslutning.

### 7.3 Utenfor v1 ifølge Product Brief

- Automatisk vurdering/karaktersetting av studenten.
- Integrasjon med Canvas eller andre læringsplattformer.
- Samarbeid og deling mellom studenter.
- Langvarig analyse av studentprestasjoner.
- Automatisk innhenting av forelesningsmateriale fra eksterne systemer.
- Betaling eller kjøp/salg i appen.

### 7.4 Implementeringsklarhet

Dette PRD-et er en kildebasert kravbaseline, ikke et vedtak om full scope eller teknologistakk. FR-1–FR-8 kan brukes til å planlegge videre UX og arkitektur, men implementeringsstories som avhenger av åpne valg skal ikke behandle dem som avgjort. Før kode for berørte deler starter, må gruppen avklare teknologistakk, KI-tjeneste/nøkkelhåndtering/dataflyt, quizformat og valggrenser, PDF-støtte/OCR, testmodus og eventuell MVP-utvidelse. Målbar vurdering av kildebinding krever også godkjente testnotater og fasit. Derfor står dokumentstatus som `draft`.

## 8. Akseptansekriterier og verifisering

Kriteriene under er testbare mot funksjonskravene. Kvalitetskriterier som krever fasit eller valg av testmodus må ferdigstilles når gruppen har tatt beslutningene i §9.

| ID | Akseptansekriterium | Verifiserer |
|---|---|---|
| AC-1 | Studenten kan lime inn ikke-tom tekst og starte en genereringsjobb. Tom tekst stoppes med en synlig forklaring. | FR-1 |
| AC-2 | Studenten kan velge en PDF som kan leses; en ugyldig eller uleselig PDF gir synlig feilmelding uten at appen viser tekniske hemmeligheter. | FR-2, FR-8, NFR-4 |
| AC-3 | Valgene for sammendragslengde, quizvanskelighetsgrad og antall spørsmål følger genereringsjobben og kan kontrolleres i en test eller mock. | FR-3, FR-4 |
| AC-4 | Et vellykket resultat inneholder et sammendrag, en begrepsliste, quizspørsmål og tilgjengelig fasit. | FR-5, FR-6 |
| AC-5 | Quizresultatet inneholder det antallet spørsmål studenten ba om, innenfor grensene som gruppen fastsetter før implementasjon. | FR-4, FR-6 |
| AC-6 | I en veiledningsfri test får testbrukeren oppgaven å lage repetisjonsmateriale fra godkjente testnotater. Bestått når personen kan sende inn notater, velge innstillinger, starte generering og peke ut sammendrag, begrepsliste, quiz og fasit uten hint. | FR-7, NFR-3 |
| AC-7 | Når generering feiler, får studenten en forståelig feilmelding; hemmeligheter og rå intern feildetalj eksponeres ikke. | FR-8, NFR-4 |
| AC-8 (foreslått) | Mot godkjente faste testnotater skal quizspørsmål kunne kontrolleres mot fasit, og ingen spørsmål skal kreve kunnskap som ikke finnes i notatene. | NFR-1; lærerens anbefaling, ikke vedtatt |
| AC-9 (foreslått) | Appens kjerneflyt kan demonstreres uten ekstern API-nøkkel ved bruk av testmodus med eksempelresultater. | Testmodus; lærerens anbefaling, ikke vedtatt |

**Foreslått testnivå, ikke implementert:** enhetstester for inputvalidering, PDF-feil, innstillingsgrenser og resultatform; integrasjonstester med KI-klient mock; ende-til-ende-test for AC-1–AC-7; manuell kvalitetskontroll på godkjente faste testnotater hvis gruppen vedtar AC-8. Ingen testresultater påstås i dette PRD-et.

## 9. Åpne spørsmål og beslutninger

Alle punktene nedenfor står som uavklart i [`docs/decisions/DECISION_LOG.md`](../../../../docs/decisions/DECISION_LOG.md). Avklar dem før relevant implementasjon.

1. **Quizinteraksjon (DEC-001):** Skal første versjon bare vise spørsmål og fasit, eller også la studenten svare og få tilbakemelding/poengsum? Eier: gruppen. Revider før quiz-UI implementeres.
2. **Lagring (DEC-002):** Skal resultater lagres per emne/forelesning eller bare finnes for den aktuelle arbeidsflyten? Eier: gruppen. Revider før datalagring eller innlogging planlegges.
3. **KI-tjeneste, nøkkel og kostnad (DEC-003):** Hvilken tjeneste, hvem dekker eventuell kostnad, og hvordan håndteres notatdata og nøkler? Eier: gruppen. Revider før ekstern KI-integrasjon.
4. **Testmodus (DEC-004):** Skal appen ha ferdige eksempelresultater/mock slik at sensor kan kjøre den uten API-nøkkel? Eier: gruppen. Revider før README og testoppsett ferdigstilles.
5. **Teknologier (DEC-005):** Hvilket språk, UI-rammeverk, PDF-verktøy og testverktøy skal brukes? Eier: gruppen. Revider før prosjektstruktur og avhengigheter velges.
6. **Quizformat og grenser:** Flervalg, fritekst eller begge deler? Hvilke verdier kan velges for antall spørsmål og sammendragslengde? Eier: gruppen. Revider i UX/arkitektur før skjemaet implementeres.
7. **Målbar relevans:** Hvilke godkjente testnotater, forventede begreper og fasit skal brukes for å måle om resultatene er basert på kilden? Eier: gruppen. Revider før kvalitetskravet erklæres verifisert.
8. **PDF-støtte:** Skal skannede PDF-er med OCR støttes, eller bare PDF-er med maskinlesbar tekst? Eier: gruppen. Revider før PDF-løsning velges.

## 10. Antakelsesregister

- **A-1:** §4 UJ-1 beskriver én student som behandler egne notater i én økt. Dette er en rollebasert organisering av briefens kjerneflyt, ikke en dokumentert persona; konto, lagring og plattform er ikke forutsatt.
- **A-2:** Akseptansekriteriene tester strukturen og brukerflyten uavhengig av leverandør/modell. Konkret kvalitetsmåling av generert innhold avventer gruppens testnotater og godkjente regler.

## 11. Kilder

- `product-brief.md`: «Executive Summary», «The Solution», «What Makes This Different», «Who This Serves», «Success Criteria» og «Scope».
- `tilbakemelding-product-brief.md`: «Samlet vurdering», «De viktigste endringene», «Kvalitetssikring og testing», «README og kjørbarhet» og «Neste steg for gruppen».
- `docs/PROJECT_CONTEXT.md`: «Krav og mulige utvidelser», «Uavklart» og «Gjeldende utviklingsstatus».
- `docs/decisions/DECISION_LOG.md`: DEC-001 til DEC-005 er uavklart.
- `docs/bmad/WORKFLOW_STATUS.md`: installert BMad Method og tilgjengelige planleggingsarbeidsflyter.
