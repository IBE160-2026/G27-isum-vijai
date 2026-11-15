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

- source_spec: `_bmad-output/implementation-artifacts/spec-mvp-002-gemini-ai.md`
  summary: Avklar og vurder en maksimal notatstørrelse for tekst før ekstern Gemini-behandling.
  evidence: Tekstinput har ingen størrelsesgrense i spesifikasjonen eller implementasjonen; vurder konsekvens og fastsett grense etter avklaring av leverandørkvoter og ønsket brukerflyt.
- source_spec: `_bmad-output/implementation-artifacts/spec-mvp-002-gemini-ai.md`
  summary: Vurder en verifiserbar kildebindingsstrategi for KI-genererte sammendrag, begreper og quiz.
  evidence: Strukturert validering kontrollerer felter og form, men kan ikke bekrefte semantisk støtte i notatene; dette krever en avtalt verifikasjonsmetode og syntetiske eksempler før det kan fastslås hvor ofte innhold blir oppdiktet.
