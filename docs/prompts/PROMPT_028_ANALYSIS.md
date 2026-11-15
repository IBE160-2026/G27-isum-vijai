# PROMPT 028 – Product Brief alignment, post-merge verification og dokumentasjon

Ordrett originalprompt fra brukerens analyseforespørsel. Den senere godkjenningen av dokumentasjonsutførelsen står i [PROMPT_028_APPROVAL.md](PROMPT_028_APPROVAL.md).

```text
PROMPT 028 – PRODUCT BRIEF ALIGNMENT, POST-MERGE VERIFICATION OG FULLSTENDIG DOKUMENTASJON

Vi skal nå videreutvikle IBE160-prosjektet etter at PR #1 og PR #2 er merget.

Produktet heter:

Foredragsnotater → Sammendrag & Quizgenerator

Bruk installert BMAD Method v6.12.4 og prosjektets etablerte arbeidsflyter.

1. PROSJEKTINFORMASJON

Repository:
IBE160-2026/G27-isum-vijai

Lokal prosjektmappe:
~/Downloads/G27-isum-vijai

Vi ønsker at alle nye endringer skjer på en egen branch.

Foreslått branch:
docs/028-product-brief-alignment

Ikke opprett branchen før Git-statusen er kontrollert.

Ikke commit, push, merge eller opprett PR uten eksplisitt godkjenning.

2. PRODUKTETS OPPRINNELIGE MÅL

Product Brief-en beskriver følgende produkt:

En student skal kunne laste opp eller lime inn forelesningsnotater som tekst eller PDF.

Studenten skal kunne velge:

* Lengde på sammendraget.
* Vanskelighetsgrad på quiz.
* Antall quiz-spørsmål.

Applikasjonen skal produsere:

* Sammendrag basert på studentens notater.
* Liste over sentrale begreper.
* Quiz-spørsmål basert på notatene.
* Fasit til quiz-spørsmålene.

Produktet skal støtte en sammenhengende arbeidsflyt fra forelesningsnotater til aktiv repetisjon.

Studenten skal få tydelig tilbakemelding dersom dokumenter ikke kan behandles.

Generert innhold skal ikke fremstilles som garantert korrekt.

Brukeren skal kunne sammenligne resultatet med originalmaterialet.

Første versjon skal være enkel og fokusert på denne arbeidsflyten.

Funksjoner utenfor første versjon omfatter blant annet automatisk karaktersetting, Canvas-integrasjon, samarbeid mellom studenter, langtidsanalyse og betaling.

Disse målene skal bevares med mindre gruppen uttrykkelig godkjenner endringer.

3. FASE A – VERIFISER GIT OG OPPDATERT MAIN

Start med skrivebeskyttet kontroll:

1. Kontroller aktiv branch.
2. Kontroller Git-status og lokale endringer.
3. Kontroller alle eksisterende worktrees.
4. Kontroller at PR #1 og PR #2 faktisk er merget på GitHub.
5. Registrer merge-commit-SHA for begge PR-ene.
6. Kontroller origin/main.
7. Kontroller lokal main.
8. Kontroller eventuelle forskjeller mellom lokal og ekstern main.

Dersom det er trygt, kan lokal main oppdateres med fast-forward-only.

Ikke bruk reset, force eller rebase.

Ikke overskriv lokale endringer.

Ikke rør .memlog.md.

Hvis oppdateringen ikke kan gjennomføres trygt, stopp og rapporter problemet.

4. FASE B – FINN EKSISTERENDE PRODUCT BRIEF

Undersøk prosjektets BMAD-artefakter og dokumentasjon.

Finn den eksisterende Product Brief-en.

Kontroller:

1. Filsti og dokumentstatus.
2. Om dokumentet samsvarer med Product Brief-teksten jeg har gitt.
3. Om det finnes senere godkjente endringer.
4. Om PRD-en bygger på samme produktmål.
5. Om viktige krav mangler i PRD-en.
6. Om dokumentasjonen beskriver planlagte funksjoner som allerede implementerte.

Bruk teksten jeg har gitt som grunnlag for sammenligningen.

Ikke overskriv tidligere dokumentasjon uten å bevare historikk og sporbarhet.

5. FASE C – KARTLEGG IMPLEMENTERT FUNKSJONALITET

Undersøk faktisk kode på oppdatert main.

Lag en krav-til-implementasjon-matrise for:

R-01: Brukeren kan lime inn forelesningsnotater.

R-02: Brukeren kan laste opp tekstfiler.

R-03: Brukeren kan laste opp PDF-filer.

R-04: Applikasjonen genererer sammendrag basert på brukerens notater.

R-05: Applikasjonen trekker ut sentrale begreper fra notatene.

R-06: Applikasjonen genererer quiz-spørsmål fra notatene.

R-07: Quizen inneholder fasit.

R-08: Brukeren kan velge sammendragslengde.

R-09: Brukeren kan velge quiz-vanskelighetsgrad.

R-10: Brukeren kan velge antall quiz-spørsmål.

R-11: Applikasjonen håndterer tomme eller ugyldige dokumenter.

R-12: Brukeren kan gjennomføre hele arbeidsflyten uten hjelp.

R-13: Applikasjonen skiller mellom demonstrasjonsinnhold og faktisk generert innhold.

R-14: Brukeren får tydelig informasjon om begrensninger og mulig feil i generert innhold.

R-15: Løsningen håndterer brukerens materiale i samsvar med avklart lagrings- og personvernmodell.

Disse R-numrene er foreløpige kartleggingsidentifikatorer, ikke automatisk godkjente PRD-krav.

For hvert punkt skal du dokumentere:

* Krav.
* Kilde i Product Brief eller PRD.
* Implementert, delvis implementert eller ikke implementert.
* Relevant kode.
* Eksisterende tester.
* Manglende tester.
* Eventuelle avhengigheter eller åpne beslutninger.

Ikke anta at en funksjon er implementert bare fordi den finnes i grensesnittet.

Skill tydelig mellom:

* Faktisk AI-generering.
* Lokal regelbasert tekstbehandling.
* Hardkodet demo.
* Planlagt funksjonalitet.

6. FASE D – LOKAL TESTING ETTER MERGE

Undersøk hvordan prosjektet skal kjøres.

Kjør relevante automatiske tester på oppdatert main.

Registrer:

* Faktisk kommando.
* Dato og tidspunkt.
* Testet commit-SHA.
* Antall beståtte tester.
* Antall feilede tester.
* Eventuelle warnings.
* Eventuelle begrensninger.

Kontroller også hvordan Streamlit-applikasjonen startes.

Hvis mulig, gjennomfør en lokal funksjonstest.

Test med egne forelesningsnotater.

Kontroller spesielt at sammendrag og begreper endres når notatene endres.

Kontroller om quizen faktisk bygger på brukerens notater, eller fortsatt er demo.

Hvis nettlesertesting ikke er mulig, oppgi nøyaktige manuelle teststeg.

Ikke rapporter manuelle tester som gjennomført dersom de ikke faktisk er utført.

Ikke rett kode automatisk i denne fasen.

7. FASE E – PRODUCT BRIEF OG PRD

Basert på kartleggingen skal du foreslå nødvendige oppdateringer i Product Brief og PRD.

Product Brief skal fortsatt beskrive:

* Problemet.
* Målgruppen.
* Produktvisjonen.
* Løsningen.
* Suksesskriteriene.
* Omfanget for første versjon.
* Funksjoner utenfor første versjon.

Ikke fjern krav fordi de ennå ikke er implementert.

Hvis et krav er uklart, dokumenter spørsmålet som en åpen beslutning.

Ikke endre opprinnelige produktmål uten godkjenning.

Vurder om dokumentene trenger:

1. Tydeligere skille mellom produktmål og implementasjonsstatus.
2. Mer presise og testbare suksesskriterier.
3. Avklaring av AI-bruk.
4. Avklaring av PDF-støtte.
5. Avklaring av datalagring og personvern.
6. Presisering av quiz-generering.
7. Presisering av hvordan originalmaterialet skal kunne kontrolleres.
8. Oppdaterte kryssreferanser til PRD og BMAD-storyer.

Ikke marker åpne beslutninger som vedtatt.

8. FASE F – BMAD METHOD

Bruk de faktisk installerte BMAD-arbeidsflytene.

Undersøk hvilke BMAD-artefakter som allerede finnes.

Foreslå riktig arbeidsflyt for:

* Product Brief Alignment.
* PRD Alignment.
* Integrasjonstesting.
* Neste utviklingsstory.

Ikke opprett en ny story som dupliserer eksisterende arbeid.

Hvis BMAD krever spesifikasjonsgodkjenning før implementasjon, skal du stoppe og be om godkjenning.

Ikke marker ufullførte arbeidsflyter som done.

9. FASE G – FULLSTENDIG LOGGFØRING

Dette er svært viktig.

Vi ønsker fullstendig og etterprøvbar dokumentasjon av hele utviklingsprosessen.

Kontroller alle relevante dokumenter:

docs/CODEX_PROMPT_LOG.md

docs/CHANGELOG_PROCESS.md

docs/testing/TEST_PLAN.md

docs/testing/TEST_LOG.md

docs/testing/TEST_LOG_TEMPLATE.md

docs/PROJECT_CONTEXT.md

docs/bmad/WORKFLOW_STATUS.md

docs/decisions/DECISION_LOG.md

Eksisterende Product Brief.

Eksisterende PRD.

Relevante BMAD-spesifikasjoner.

Relevante implementasjonsartefakter.

README.md

Eventuelle andre eksisterende logger som er relevante.

Kontroller at dokumentasjonen viser:

1. Hvorfor prosjektet ble opprettet.
2. Hvilke produktmål som ble definert.
3. Hvilke beslutninger som er tatt.
4. Hvilke beslutninger som fortsatt er åpne.
5. Hvilke BMAD-arbeidsflyter som er gjennomført.
6. Hvilke funksjoner som er implementert.
7. Hvilke tester som faktisk er kjørt.
8. Hvilke reviewfunn som er lukket.
9. Hvilke funn som er utsatt.
10. Hvilke commits som dokumenterer arbeidet.
11. Hvilke Pull Requests som er opprettet.
12. Hvilke Pull Requests som er merget.
13. Hvilken commit som er gjeldende main.
14. Hva som fortsatt mangler før produktet oppfyller Product Brief.
15. Hva neste utviklingssteg bør være.

VIKTIG:

Ikke slett eller skriv om historiske logger.

Ikke rekonstruer utilgjengelige prompttekster.

Ikke finn på beslutninger, tester eller godkjenninger.

Ikke endre DEC-001–DEC-005 uten dokumentert gruppebeslutning.

Ikke oppdater alle filer mekanisk. Oppdater bare filer der det finnes et reelt behov.

Hvis en teknisk beslutning allerede er loggført, bruk en kryssreferanse i stedet for å lage duplikater.

10. FASE H – PLAN FOR VIDERE UTVIKLING

Etter analysen skal du foreslå en prioritert utviklingsplan.

Planen skal bygge på:

* Product Brief.
* PRD.
* Faktisk implementasjon.
* Testresultater.
* Åpne beslutninger.
* Avhengigheter mellom funksjonene.

Vurder spesielt:

* PDF-opplasting.
* AI-basert generering.
* Quiz basert på notatene.
* Sammendragslengde.
* Quiz-vanskelighetsgrad.
* Antall spørsmål.
* Feilhåndtering.
* Brukervennlighet.
* Personvern og datalagring.

Ikke start implementasjon av nye produktfunksjoner ennå.

11. FASE I – RAPPORT OG GODKJENNING

Presenter en samlet rapport med:

1. Verifisert Git-status etter merge.
2. Oppdatert main-SHA.
3. Resultat fra automatiske tester.
4. Resultat fra eventuell lokal Streamlit-test.
5. Hvor Product Brief ligger.
6. Forskjeller mellom Product Brief og PRD.
7. Krav som allerede er implementert.
8. Krav som mangler.
9. Hvilke Product Brief-endringer som anbefales.
10. Hvilke PRD-endringer som anbefales.
11. Hvilke logger som trenger oppdatering.
12. Hvilke BMAD-artefakter som trenger oppdatering.
13. Forslag til neste utviklingsstory.
14. Forslag til ny branch.
15. Eventuelle beslutninger gruppen må ta.

STOPP ETTER RAPPORTEN.

Ikke implementer nye funksjoner.

Ikke rediger Product Brief eller PRD uten godkjenning.

Ikke rediger prosjektlogger uten godkjenning.

Ikke commit eller push.

Ikke opprett Pull Request.

Ikke merge eller rebase.

Ikke endre Git-identitet.

Ikke rør .memlog.md.

Målet er at Product Brief, PRD, implementasjon, tester, BMAD og alle prosjektlogger skal være konsistente, korrekte og etterprøvbare.
```

## Senere verifisering – 2026-11-15

Promptteksten over er bevart ordrett som historisk instruks; den er ikke bevis for at PR #2 var merget på tidspunktet den ble skrevet. Senere `git fetch origin` viste at `origin/main` peker på mergecommit `1227fb443e52815f831b3f5720b4f41844f72ad0`, med PR #2-head `a5778f25991d9b88fa4c3c186d5b2d2536c36212` som andre forelder. Commit-tiden er `2026-11-14 21:49:15 +01:00`. PR-spesifikk `merged_at` ble ikke hentet fordi GitHub API var utilgjengelig fra Codex-miljøet. Se [post-merge-status og kravmatrise](../../_bmad-output/implementation-artifacts/prompt-028-product-brief-alignment.md).
