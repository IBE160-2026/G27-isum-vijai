# Tilbakemelding på PRD

| | |
|---|---|
| **Gruppe** | G27 – G27-isum-vijai |
| **PRD vurdert** | `_bmad-output/planning-artifacts/prds/prd-G27-isum-vijai-2026-10-23/prd.md` (status: draft, sist endret 2026-10-23, commit 6a247e2) |
| **Dato** | 2026-11-12 |
| **Type** | Formativ tilbakemelding, ikke karakter |

## 1. Samlet inntrykk

PRD-en er ryddig og ærlig. Kravene har testbare konsekvenser, kildene er oppgitt, og dere påstår ikke at ting er vedtatt når de ikke er det. Risikoen er at nesten alle viktige valg (utvidelse av MVP, KI-tjeneste, testmodus, quizformat, grenser) står som åpne spørsmål. Da kan UX, arkitektur og stories ikke bygge på dokumentet ennå, og kjerneomfanget er fortsatt det briefen ble kalt «for lite» for.

## 2. Dette fungerer godt

1. **Ærlig skille mellom bekreftet og forslag.** §0 og §7.1/§7.2 skiller «Bekreftet» fra «Forslag». Det gjør at ingen utvidelse kan snike seg inn som krav.
2. **FR-ene har «Testbare konsekvenser».** FR-1: «Tom tekst gir en forståelig valideringsmelding og starter ikke generering.» Dette kan bli testtilfeller direkte, og AC-1–AC-7 i §8 kobler kriterier til FR/NFR.
3. **KI-ansvar og guardrails er nevnt.** NFR-2 («skal ikke love at KI-generert innhold alltid er korrekt») og FR-8 («Teknisk feil viser ikke hemmeligheter, API-nøkler…») viser at dere har tenkt på KI-risiko. Tillegget holder teknologivalg utenfor kravene.

## 3. Oversikt per dimensjon

| Dimensjon | Vurdering | Kort begrunnelse |
|---|---|---|
| Beslutningsklarhet | svak | Åtte åpne spørsmål (§9), og de som avgjør omfanget (DEC-001–005) er ikke tatt. |
| Substans | god | Lite pynt og ingen oppblåste personas, men NFR-5/6/7 er mer forbehold enn krav. |
| Strategisk sammenheng | svak | Tesen («aktiv repetisjon fra egne notater») er tydelig, men utvidelsen som gir funksjonene tyngde er ikke valgt. |
| Testbarhet | god | Gode konsekvenser for input og feil, men KI-kvalitet (NFR-1) og grenseverdier mangler. |
| Scope og avgrensning | svak | §7.3 har tydelig «utenfor v1», men MVP-kjernen er uten utvidelse og testmodus er ikke bestemt. |
| Brukbarhet for neste fase | god | Kontinuerlige ID-er og kilder, men bare én brukerreise og mange åpne punkter å bygge rundt. |
| Formtilpasning | god | Passer et lite verktøy for én bruker. Mangler suksessmål (SM) og motmål. |

## 4. Viktigste forbedringer

### 4.1 Velg utvidelsen og gjør den til FR-er
- **Alvorlighet:** høy
- **Hvor:** §7.2 «Dette PRD-et velger ikke mellom alternativene»; §9 punkt 1–2
- **Problem og hvorfor det betyr noe:** Uten valg har dere åtte FR-er som i praksis er «ett skjema og ett kall til en språkmodell». Epics og stories får lite å dele opp, og UX vet ikke om quizen skal besvares i appen. Nesten alt i §9 henger sammen med dette valget.
- **Forslag:** Ta beslutningen nå og før den i DECISION_LOG. Velger dere interaktiv quiz, kan det bli:
  > **FR-9: Besvare quiz.** Studenten kan velge ett svar per spørsmål og få rett/galt umiddelbart.
  > - Etter siste spørsmål vises poengsum som «x av n».
  > - Et spørsmål uten valgt svar teller som feil og markeres.
  > - Fasit vises først etter at studenten har svart.

### 4.2 Krav til KI-ens usikre og ugyldige svar, og til testmodus
- **Alvorlighet:** høy
- **Hvor:** §3 «Testmodus: Foreslått…»; AC-8/AC-9 «foreslått»; NFR-1 «Briefen fastsetter ikke en målemetode»
- **Problem og hvorfor det betyr noe:** Kjernen i appen er et språkmodellkall, men PRD-en sier ingenting om hva som skjer når modellen svarer i feil format, gir færre spørsmål enn bedt om, tar for lang tid eller finner på innhold. Testmodus er det som gjør at automatiske tester og sensor kan kjøre appen uten nøkkel, og er i dag bare et forslag. NFR-1 kan ikke testes slik den står.
- **Forslag:** Gjør testmodus til et FR og legg til et feilkrav, for eksempel:
  > **FR-9a: Ugyldig modellsvar.** Hvis KI-svaret mangler sammendrag, begrepsliste eller quiz, eller har færre spørsmål enn valgt, viser produktet en feilmelding og tilbyr «Prøv igjen». Delvise resultater vises ikke som fullstendige.
  >
  > **FR-10: Testmodus.** Når `TEST_MODE=true`, returneres lagrede eksempelresultater for de tre testnotatene uten KI-kall. Produktet viser tydelig at resultatet er eksempeldata.

  Gjør NFR-1 målbar: «For hvert av de tre testnotatene skal minst 80 % av forventede begreper være med, og ingen quizspørsmål krever kunnskap utenfor notatet (manuell sjekk).» Tallene er et utgangspunkt dere må ta stilling til.

### 4.3 Fyll ut grenser og gjør NFR-ene til krav
- **Alvorlighet:** medium
- **Hvor:** FR-3 «Selve valgalternativene må bestemmes i UX/arkitektur»; FR-4 «Grenseverdier… må fastsettes»; NFR-5 «Begrens lagring…»; NFR-7
- **Problem og hvorfor det betyr noe:** AC-5 kan ikke testes uten en øvre/nedre grense, og «begrens» og «hensiktsmessig håndtering» gir utvikler ingen terskel. NFR-7 er et åpent spørsmål, ikke et krav. Mangler også maks størrelse på input og tid for generering.
- **Forslag:** Sett verdier og merk dem `[ASSUMPTION]` til de er bekreftet, for eksempel: sammendragslengde «kort / middels / lang»; vanskelighetsgrad «lett / middels / vanskelig»; antall spørsmål 3–20; maks 20 000 tegn eller 10 MB PDF; melding hvis generering tar over 60 sekunder. Flytt NFR-7 til §9. Skriv NFR-5 som: «Notattekst lagres ikke etter at økten er avsluttet» (hvis det er valget).

### 4.4 Gjør brukerreisen konkret
- **Alvorlighet:** medium
- **Hvor:** §4 UJ-1 «ingen navngitt persona eller brukerundersøkelse er dokumentert»; §2.1
- **Problem og hvorfor det betyr noe:** Briefen-tilbakemeldingen ba om en konkret student. Med én generell reise får UX ingen skjermer og kanttilfeller å tegne, og FR-ene viser ikke til UJ-er.
- **Forslag:** Gjør UJ-1 konkret (navngitt student, emne, lysbildenotater i PDF, eksamen om to uker), og legg til UJ-2: «PDF-en er skannet og kan ikke leses». La FR-1–FR-8 vise til UJ-ene («realiserer UJ-1»).

### 4.5 Legg til målbare suksessmål og motmål
- **Alvorlighet:** lav
- **Hvor:** §8 (AC-er) og manglende suksessmål
- **Problem og hvorfor det betyr noe:** AC-ene tester funksjonene, men ikke om tesen holder (at materialet er bygget på notatene og er nyttig).
- **Forslag:** Legg til SM-1 («Mot tre testnotater er minst 80 % av forventede begreper med»), SM-2 (en testbruker fullfører flyten uten hjelp, jf. AC-6) og et motmål, for eksempel kostnad per generering som ikke økes for å få flere spørsmål.

## 5. Mekaniske funn

- **ID-er:** FR-1–FR-8, NFR-1–NFR-7, AC-1–AC-9 og UJ-1 er sammenhengende, og krysshenvisningene løser seg. Ingen SM-ID-er.
- **Glossar:** «notater», «dokument» og «fil» brukes om det samme (FR-2, FR-8). «Innstillinger» og «valg» veksler. Sjekk også at «Fasit» og «Resultat» brukes likt overalt.
- **[ASSUMPTION]:** Bare én inline (UJ-1). A-2 i §10 står ikke inline i teksten. §0 viser til merkelappen «Bekreftet», men den er ikke brukt på selve kravene.
- **Teknologi:** Tillegget (`addendum.md`) holder stakken utenfor kravene, som det skal.

## 6. Før dere går videre

**Må avklares før UX, arkitektur og epics:**
- Quizinteraksjon og lagring (DEC-001, DEC-002), fordi de avgjør omfang og skjermer.
- KI-tjeneste, kostnad og nøkkel (DEC-003) og testmodus (DEC-004), fordi de avgjør arkitektur og kjørbarhet.
- Quizformat og grenseverdier, PDF-støtte (maskinlesbar eller også OCR).

**Kan vente:** konkret teknologistakk (DEC-005, tillegget har et rimelig utkast), detaljer om testnotater og fasit så lenge dere bestemmer at de skal lages.

**Oppfølging av briefen-tilbakemeldingen: delvis.** Dere har skrevet inn rådene og gjort dem til forslag (utvidelse, testnotater, testmodus, nøkkel i `.env`), men ingen er vedtatt. Suksesskriteriene er ikke gjort målbare ennå (AC-8 er «foreslått»), og det konkrete studenteksemplet mangler.

## 7. Refleksjonsspørsmål

1. §7.2 beskriver tre mulige utvidelser, men velger ingen. Hva trengte dere for å kunne bestemme dere, og hvordan kan dere bruke KI til å teste konsekvensene av hvert alternativ (stories, tester, personvern) før dere velger?
2. Hvordan vil dere kontrollere at et KI-generert quizspørsmål faktisk står i notatene? Hva i PRD-en hindrer at dere godtar et feil svar fra modellen uten å oppdage det?

_Vurdert mot kvalitetsrubrikken i bmad-prd. Dette er veiledning, ikke sensur._
