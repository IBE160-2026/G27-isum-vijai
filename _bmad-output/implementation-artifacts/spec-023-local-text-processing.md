---
title: '023 – Lokalt sammendrag og begreper fra forelesningsnotater'
type: 'feature'
created: '2026-10-23'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Prototypens sammendrag og begreper er faste demo-data og påvirkes ikke av studentens notater. Studenten trenger et resultat som faktisk hentes fra teksten.

**Approach:** Lag et enkelt, deterministisk utdragssammendrag av inntil tre innholdsrike setninger og trekk ut inntil fem hyppige innholdsord lokalt. Vis disse som lokal tekstbehandling, ikke KI. Behold quizspørsmålene som tydelig merkede demonstrasjonsdata.

### Akseptansekriterier

- Gitt notater med flere setninger, når resultatet lages, skal sammendraget bestå av setninger hentet fra de innsendte notatene.
- Gitt notater med gjentatte innholdsord, når begreper trekkes ut, skal resultatet inneholde ord fra notatene, rangert etter forekomst med stabil rekkefølge ved lik frekvens.
- Gitt tom eller blank input, når resultatet lages, skal eksisterende valideringsfeil vises og ingen resultatdata returneres.
- Gitt et ferdig resultat, skal sammendrag og begreper merkes som lokalt behandlet, quiz som demo-data, og grensesnittet skal ikke hevde at lokal behandling er KI.
- Gitt gyldig input, skal den eksisterende interaktive demonstrasjonsquizen fortsatt kunne besvares og gi tilbakemelding.

### Tekniske oppgaver

- `prototype/generator.py` — legg til standardbibliotek-basert setningsuttrekk og begrepsuttrekk; behold eksisterende input- og quizvalidering.
- `app.py` — vis lokale resultatdeler og quiz med tydelig separat kilde-/demo-merking.
- `tests/test_generator.py` — legg til pytest-kompatible tester for kildegrunnlag, determinisme, tom input og demoquizens struktur/proveniens.
- `README.md` — forklar lokal uttrekksmetode og at den ikke er KI-generering.

### Definition of Done

- Akseptansekriteriene er dekket av automatiserte tester.
- Hele pytest-suiten består, og eksisterende quizflyt er manuelt kontrollert.
- Relevant BMAD Code Review er gjennomført og eventuelle funn triagert.
- Implementeringsspesifikasjon, BMAD-status og `docs/CODEX_PROMPT_LOG.md` er oppdatert.
- Ingen commit eller push er utført.

</frozen-after-approval>

## Implementation Notes

- Implementert standardbibliotek-basert utdragssammendrag: velg opptil tre setninger med høyest gjennomsnittlig setningsbasert frekvens for innholdsord, og behold kilderekkefølgen. Begreper er de fem hyppigste ordformene etter enkel norsk stoppliste, med stabil førsteforekomst ved lik frekvens.
- Sammendrag og begreper kommer fra notatene og merkes med `sources` som `local`; quiz kommer fortsatt fra uendret demonstrasjonsfixture og merkes `demo`. Ingen KI-tjeneste, API-nøkkel eller ny avhengighet ble lagt til.
- Endret `prototype/generator.py`, `app.py`, `README.md`, `tests/test_generator.py`; lagt til `tests/test_app.py` for Streamlit UI-regresjonstester.
- Verifisering: 14 pytest-tester bestod; `compileall` og `git diff --check` bestod. Streamlit AppTest viste notatbasert sammendrag/begreper, lokal/ikke-KI-merking, demoquiz, quizkontroller og feilmelding for tom input.

## Review Triage Log

- **patch (low), rettet:** Gjentakelser i én setning kunne overvekte sammendragsscoren. Frekvens telles nå maksimalt én gang per setning; regresjonstest dekker at rangeringen ikke endres av gjentatte ord i samme setning.
- **patch (low), rettet:** Vanlige norske fyllord kunne vises som begreper. Utvidet stopplisten med vanlige bindeord og lagt til test.
- **patch (medium), rettet:** Kilde- og demo-merking var ikke automatisert verifisert i Streamlit-visningen. Lagt til UI-tester for kildemerking, quizdisclaimer, tom begrepsliste og tom input.
- **false:** Blind Hunter hevdet at en test sammenlignet punktuerte ord med konsepter uten punktum. Begge konseptene forekom også uten punktum i testnotatet; testen ble i tillegg styrket til å tokenisere ord før sammenligning.
- **false:** Blind Hunter mente mockens sammendrag/begreper ikke burde valideres. Den injiserte `generator`-funksjonen har fortsatt kontrakten om å returnere et fullstendig resultat, og ugyldig struktur skal avvises før quizspørsmål konsumeres.
- **defer:** Acceptance Auditor påpekte at PRD FR-6/AC-4/NFR-1 forventer quiz fra notatene. Denne historien og brukerens instruks beholder quiz som demo; kildebundet quiz må planlegges som egen historie. Registrert i `deferred-work.md`.
- **patch (low), fullført ved avslutning:** BMAD-status og promptlogg manglet i review-diffen fordi de oppdateres etter gjennomført review. Begge er nå oppdatert med faktisk status og verifisering.
- **Review-begrensning:** Edge Case Hunter-laget returnerte tomt resultat. BMAD Code Review klassifiserte derfor laget som mislykket; øvrige tre lag fullførte.

### Review Findings (post-fix review)

- [x] [Review][Patch] Submit quiz answers in the Streamlit test and assert score and per-question feedback [tests/test_app.py]
- [x] [Review][Patch] Assert that the rendered summary contains only exact sentences from the submitted notes [tests/test_app.py]
- [x] [Review][Defer] Handle terminal punctuation followed by a closing quote or parenthesis when splitting sentences [prototype/generator.py] — deferred: uncommon sentence-boundary edge case; can be handled in a later text-processing story.
- [x] [Review][Defer] Avoid splitting sentences at ordinary line wraps [prototype/generator.py] — deferred: robust document line-wrap normalization is outside this story's current input handling.
- [x] [Review][Defer] Add common Norwegian filler words that currently surface as concepts [prototype/generator.py] — deferred: stopword tuning is an optional quality improvement to the simple heuristic.
- [x] [Review][Defer] Validate only the demo quiz fields consumed by the local result builder [prototype/generator.py] — deferred: current fixed demo provider satisfies the full result contract; revisit if provider injection is expanded.
- [x] [Review][Defer] Render provenance labels from result source metadata [app.py] — deferred: current fixed labels match the sole supported local/demo sources; revisit with additional providers.

Rejected findings:
- Blind Hunter's claim that the summary/concept output is unused was rejected: `app.py` renders those generated fields.
- Blind Hunter's short-input sentence selection suggestion was rejected as low impact: inputs of three or fewer sentences already satisfy the explicit acceptance criterion that the summary use source sentences; changing selection behavior would add complexity without a demonstrated user harm.
- PRD quiz-from-notes finding is deferred and recorded above because quiz generation from notes is outside this story's approved scope.
- The two approved test patches are implemented and pass; improvement findings 3–7 are deferred below.
