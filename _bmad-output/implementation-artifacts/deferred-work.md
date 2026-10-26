## Deferred from: code review of spec-023-local-text-processing (2026-10-23)

- source_spec: `_bmad-output/implementation-artifacts/spec-023-local-text-processing.md`
  summary: Generate quiz questions and answers from the user's lecture notes instead of fixed demonstration data.
  evidence: PRD FR-6, AC-4, and NFR-1 expect quiz content based on the notes, while PROMPT 023 explicitly keeps the quiz as labeled demonstration data for this iteration.

## Deferred from: code review of spec-023-local-text-processing (2026-10-23)

- **Setningsdeling etter avsluttende anførselstegn eller parentes:** `_SENTENCE_PATTERN` håndterer ikke alltid tegnsetting etterfulgt av `"` eller `)`. Ta med kanttilfelle og tester i en senere tekstbehandlingshistorie.
- **Linjeombryting i forelesningsnotater:** Setningsdeleren splitter på alle linjeskift, også linjeskift midt i setninger. Vurder normalisering og avsnittsbevaring ved senere dokumentinputarbeid.
- **Stoppliste for norske fyllord:** Vanlige ord som «eller», «fordi», «deres» og «hadde» kan bli begreper. Finjuster heuristikken med tester senere.
- **Validering av injisert generatorresultat:** Hele resultatobjektet valideres selv om kun quizspørsmålene brukes. Revider hvis støtte for alternative generatorer utvides.
- **Proveniensetiketter i UI:** UI-etiketter leser ikke `sources`-metadata. Koble dem til resultatmetadata når flere kilder støttes.
