# Prosjektkontekst

Oppdatert: 2026-10-18

## Prosjekt

- **Bekreftet:** Prosjektnavnet i produktbriefen er «Foredragsnotater → Sammendrag & Quizgenerator».
- **Bekreftet:** Gruppen er G27 – G27-isum-vijai. README oppgir medlemmene Thor E Isum, Akshayah Vijai og Abena Vijai.
- **Bekreftet:** Dette er et gruppeprosjekt i IBE160 Programmering med KI ved Høgskolen i Molde, høsten 2026.

## Formål og gjeldende produktbrief

- **Bekreftet:** Produktet skal hjelpe studenter med å gjøre forelesningsnotater i tekst- eller PDF-format om til sammendrag, sentrale begreper og quiz med fasit. Briefen beskriver valg av sammendragslengde, quizvanskelighetsgrad og antall spørsmål.
- **Kilde:** [`../product-brief.md`](../product-brief.md) er gjeldende brief i repoet. Tilbakemeldingen omtaler den som repoets eneste brief.
- **Bekreftet:** Briefens v1-scope utelukker automatisk karaktersetting, Canvas-integrasjon, deling, langvarig prestasjonsanalyse, ekstern innhenting av materiale og betaling.

## Faglærerens tilbakemelding, 6. oktober 2026

- **Bekreftet:** [`../tilbakemelding-product-brief.md`](../tilbakemelding-product-brief.md) er datert 2026-10-06 og vurderer briefen som et godt utgangspunkt med justeringer.
- **Bekreftet:** Tilbakemeldingen peker på behov for større v1-omfang, målbare suksesskriterier og en plan for KI-tjeneste, kostnader/nøkkel og testmodus.
- **Bekreftet:** Den foreslår blant annet interaktiv quiz, lagring per emne/forelesning og kildehenvisning per spørsmål. Dette er forslag fra tilbakemeldingen, ikke vedtatte krav.
- **Bekreftet:** Den anbefaler faste testnotater med fasit, mock-svar for automatiske tester og at sensor skal kunne kjøre løsningen uten gruppens API-nøkkel.

## Krav og mulige utvidelser

### Bekreftet i gjeldende brief

- Notater skal kunne lastes opp eller limes inn som tekst/PDF.
- Applikasjonen skal generere sammendrag, begrepsliste og quiz med fasit.
- Brukeren skal kunne velge sammendragslengde, vanskelighetsgrad og antall spørsmål.
- Resultatet skal presenteres oversiktlig, og dokumentfeil skal gi tydelig tilbakemelding.

### Foreslått, ikke vedtatt

- Interaktiv quiz med svar, forklaring og poengsum.
- Lagring per emne eller forelesning.
- Kilde/avsnittshenvisning for quizspørsmål.
- Faste testnotater med forventede begreper og mock-svar.
- Testmodus med ferdige eksempelsvar slik at appen kan kjøres uten API-nøkkel.

### Uavklart

- Om interaktiv quiz, lagring og kildehenvisninger skal inngå i v1.
- Om quizen skal være flervalg, fritekst eller begge deler.
- Hvilken KI-tjeneste som skal brukes, hvordan nøkkel håndteres og hvem som dekker eventuell kostnad.
- Hvordan testmodus skal fungere.
- Teknologistakk, lagringsmodell og PDF-behandling.
- Konkrete målbare kriterier for kvalitet og kildebinding.

## Gjeldende utviklingsstatus

- **Bekreftet:** Repoet inneholder README, produktbrief og tilbakemelding. Ved opprettelsen av denne dokumentasjonen finnes det ingen applikasjonskode, PRD, arkitektur eller epics i repoet.
- **Bekreftet:** Git-historikken inneholder commits for initialisering, README, produktbrief og tilbakemelding. Promptene bak disse arbeidsøktene er ikke arkivert her.
- **Bekreftet (etter PROMPT 007):** BMAD BMM/Core v6.12.4 er installert i prosjektet og konfigurert for Codex CLI. Se [BMAD-status](bmad/WORKFLOW_STATUS.md).
- **Bekreftet:** Ingen applikasjonskode, PRD, arkitektur eller epics er lagt til som del av BMAD-installasjonen.

## Neste anbefalte steg

1. Gruppen avklarer hvilke foreslåtte utvidelser som skal inn i v1, quizformat, KI-tjeneste, testmodus og teknologistakk.
2. Oppdater produktbriefen med vedtatte valg og målbare suksesskriterier.
3. Bruk den installerte BMAD-konfigurasjonen til å utarbeide PRD/arkitektur og planlegge stories når gruppen er klar.
4. Legg til testnotater først når gruppen har laget og godkjent dem; ikke bruk kursbeskyttet materiale uten avklaring.
