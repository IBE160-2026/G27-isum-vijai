# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G27 – G27-isum-vijai |
| **Product brief** | `product-brief.md` (commit `dc2a630`) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

Vurdert fil: `product-brief.md` i repoets rot, som er den eneste briefen. Det finnes ennå ikke PRD, arkitektur eller epics.

## Samlet vurdering

- **Godt utgangspunkt med justeringer.** Gruppen kan gå videre og innarbeide punktene under.

**Det som er bra:**

1. Briefen er ryddig, følger malen og har en tydelig kjerneflyt: last opp notater, velg sammendragslengde, vanskelighetsgrad og antall spørsmål, og få sammendrag, begrepsliste og quiz med fasit.
2. Dere er ærlige om at KI-generert innhold ikke alltid er riktig, og at brukeren bør kunne gå tilbake til originalmaterialet. Scope har også en god OUT-liste (Canvas, deling, prestasjonsanalyse og betaling er utelatt).

**De viktigste endringene:**

1. Omfanget er lite. Slik briefen står, er appen i praksis ett skjema og ett kall til en språkmodell. Det kan bli ferdig svært raskt og gir lite å vise i funksjonalitet og testing. Legg til minst én utvidelse i v1, for eksempel at studenten kan svare på quizen i appen og få poengsum, at sammendrag og quiz lagres per emne, eller at hvert quizspørsmål viser hvilket avsnitt i notatene svaret kommer fra.
2. Gjør suksesskriteriene målbare. «Det genererte innholdet er basert på materialet brukeren har gitt applikasjonen» er viktig, men hvordan skal dere sjekke det? Lag for eksempel tre faste testnotater med en fasit over hvilke begreper som skal være med, og et krav om at ingen quizspørsmål handler om noe som ikke står i notatene.
3. Legg en plan for språkmodellen. Briefen sier ikke hvilken KI-tjeneste dere vil bruke, hvem som betaler, eller hvordan sensor kan kjøre appen uten deres nøkkel. Beskriv en testmodus med ferdige eksempelsvar.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Enkel**

**Sammenlignbart med:** 8) Foredragsnotater → Sammendrag & Quizgenerator (enkel). Briefen er i praksis dette forslaget, uten egne utvidelser.

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Lav | Få egne regler. Det meste av «logikken» ligger i prompten til språkmodellen. |
| Datamodell – antall entiteter og relasjoner mellom dem | Lav | Notat, sammendrag, begrep og quizspørsmål. Lite, spesielt hvis ingenting lagres. |
| Brukere, roller og innlogging | Lav | Én studentbruker. Innlogging nevnes bare hvis materiale lagres. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Middels | Kjernen i appen. Krever gode prompts, strukturert svar (for eksempel JSON for quizen) og håndtering av feil eller oppdiktet innhold. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Lav til middels | Bare språkmodell-API, men den er nødvendig for at appen virker. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Ingen. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Middels | PDF-lesing er med i v1. Tekst fra PDF kan bli rotete (kolonner, lysbilder, tabeller). |
| Sikkerhet og personvern | Lav til middels | Kursmateriale sendes til en ekstern KI-tjeneste. Bruk egne eller fritt tilgjengelige testnotater i repoet. |

**Hva vanskelighetsgraden betyr for dere:**

- _Enkel:_ Et enkelt prosjekt gir stor sjanse for å bli ferdig. Vanskelighetsgraden inngår likevel i vurderingen, så for å nå helt opp må dere vise mer i gjennomføringen. Det betyr særlig et gjennomarbeidet design, grundig testing, en tydelig dokumentert prosess og en README som virker.

### Gjennomførbarhet med BMAD og Claude Code

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | OK | Ja, med god margin. Risikoen er heller at det blir for lite, ikke for mye. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Kjerneflyten er klar, men det blir få stories. Avklar lagring, quizformat (flervalg eller fritekst) og om quizen kan besvares i appen. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | Webapp med filopplasting og ett API-kall er godt egnet. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | Risiko | Koden er lett å kontrollere, men kvaliteten på sammendrag og quiz er vanskeligere. Bruk testnotater dere kjenner godt, slik at dere kan vurdere om svarene er riktige. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | Risiko | Opplasting, valg og feilmeldinger kan testes. Selve KI-svarene trenger faste testnotater og sjekklister, og et mock-svar for automatiske tester. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | Uten plan for nøkkel eller testmodus kan ikke sensor prøve kjernefunksjonen. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | Krever språkmodell-API, og det finnes ingen plan for kostnad eller testmodus ennå. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart som beskrevet.**

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Utvid kjerneflyten med en interaktiv quiz: studenten svarer i appen, får rett/galt per spørsmål med forklaring og henvisning til notatet, og ser poengsum til slutt.
2. Legg til enkel lagring per emne eller forelesning, slik at studenten kan komme tilbake til tidligere sammendrag og quizer. Det gir mer funksjonalitet å teste og vise frem.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | Klart hva appen gjør og hvorfor. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | Juster | Problemet er forståelig, men generelt. Gi et konkret eksempel, for eksempel et emne dere selv tar, hvor mye notater det gjelder, og hvordan dere repeterer i dag. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | OK | Beskriver hva studenten gjør og får. Avklar om quizen bare vises, eller om den kan besvares i appen. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Ærlig: alternativet er et generelt KI-verktøy, og fordelen er en fast arbeidsflyt. Tenk gjennom hva som gjør appen bedre enn å lime notatene inn i en chatbot. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Juster | «En student med digitale notater» er bredt. Beskriv gjerne en konkret student, for eksempel en førsteårsstudent foran eksamen med lysbildenotater i PDF. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Juster | Flere kan sjekkes, men «basert på materialet» og «relevant» må gjøres målbart med testnotater og fasit. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | OK | Tydelig IN/OUT. Avklar om noe lagres, siden avsnittet om innlogging er betinget. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | OK | Henger sammen med kjerneverdien og er tydelig lagt etter v1. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Juster | Grei start, men repoet har bare én commit med innhold. Bruk BMAD videre (PRD, arkitektur, stories) og lagre promptene, også promptene appen selv sender til språkmodellen. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Endre | Kjerneflyten er tydelig, men for liten alene. Legg til en eller to utvidelser i v1, se forslagene over. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Juster | Lag faste testnotater med forventede begreper og bruk mock-svar i automatiske tester. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Flyten er enkel å se for seg (opplasting → valg → resultat). Skisser hvordan sammendrag, begreper og quiz vises, og hvordan studenten finner tilbake til kilden. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | Juster | Ingen teknologivalg ennå. Det er greit i briefen, men bestem i arkitekturen hvordan PDF leses og hvor KI-kallet gjøres (på serveren, ikke i nettleseren). |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Endre | Kjernefunksjonen krever en språkmodell. Planlegg testmodus eller tydelig nøkkeloppsett i README, slik at sensor kan kjøre appen. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Bestem at API-nøkkelen ligger i `.env` utenfor Git, og at testnotatene ligger i en egen mappe. |

## 3. Neste steg for gruppen

1. Utvid v1 med interaktiv quiz med poengsum og/eller lagring per emne, og oppdater Scope.
2. Lag to–tre testnotater med fasit (forventede begreper og typiske spørsmål), og skriv om suksesskriteriene slik at de kan sjekkes mot disse.
3. Bestem KI-tjeneste og skriv en plan for nøkkel, kostnad og testmodus før dere går videre til PRD og arkitektur.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
