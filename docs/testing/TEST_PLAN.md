# Testplan

Alle T-001–T-009 står fortsatt **PLANLAGT** som testtilfeller: ingen av dem har dokumentert dekning av samtlige planlagte underkasus. Matrisene viser implementasjon og delvis kode-/testdekning på to ulike snapshots, ikke godkjenning av et helt scenario. `Implementasjon` gjelder atferden som er spesifisert for det aktuelle testtilfellet; `Full` / `Delvis` / `Ingen` beskriver testdekningen.

| ID | Område | Planlagt kontroll | Forventet resultat | Status |
|---|---|---|---|---|
| T-001 | PDF-opplasting | Last opp en gyldig PDF med testnotater; kontroller også ugyldig filtype og tom fil. | Gyldig fil godtas/behandles; ugyldige filer gir forståelig feilmelding. | PLANLAGT |
| T-002 | Tekstbehandling | Send inn limt tekst, tom tekst og tekst med linjeskift/uvanlig formatering. | Tekst behandles uten at tomt eller ugyldig input gir skjult feil. | PLANLAGT |
| T-003 | Sammendrag | Bruk faste testnotater og kontroller at sammendraget dekker avtalte hovedpoeng og respekterer valgt lengde så langt løsningen støtter det. | Resultatet vurderes mot en godkjent fasit/sjekkliste. | PLANLAGT |
| T-004 | Quizgenerering | Generer avtalt antall spørsmål på flere vanskelighetsgrader fra kjente testnotater. | Spørsmål har fasit, følger valgt antall/grad og kan spores til kildematerialet. | PLANLAGT |
| T-005 | Interaktiv quiz | Når dette eventuelt vedtas: svar riktig og feil på hvert spørsmål, og fullfør quizen. | Tilbakemelding og eventuell poengsum samsvarer med svarnøkkelen. | PLANLAGT |
| T-006 | Poengberegning | Når poengsum vedtas: test alle riktige, alle gale og blandede svar, inkludert grenseverdier. | Poengsum følger dokumentert beregningsregel. | PLANLAGT |
| T-007 | Kildehenvisninger | Når kildehenvisninger implementeres: kontroller at hvert spørsmål peker på relevant avsnitt i testnotatene. | Henvisningen støtter spørsmålet og finnes i kilden. | PLANLAGT |
| T-008 | Feilhåndtering | Simuler uleselig PDF, manglende input og utilgjengelig KI-tjeneste/feilsvar. | Brukeren får tydelig feilmelding; hemmeligheter eller interne detaljer vises ikke. | PLANLAGT |
| T-009 | Testmodus uten API-nøkkel | Start appen uten API-nøkkel og utfør kjerneflyten i valgt testmodus. | Ferdig eksempelsvar/mock gjør flyten prøvbar uten ekstern nøkkel. | PLANLAGT |

## Kryssreferanse til PRD og beslutninger

Dette er en indeks mellom PRD-krav, åpne beslutninger og testtilfeller; den dokumenterer ikke at et krav eller testcase er bestått. «Manglende direkte testcase» betyr at T-001–T-009 ikke dekker kravet fullt ut. Dekningsstatus og konkrete snapshotbevis står i tabellene nedenfor. Alle DEC-statusene er fortsatt `Uavklart`.

| PRD-krav | Relaterte beslutninger (ikke vedtatt) | Relevante testtilfeller | Avgrensning / manglende dekning |
|---|---|---|---|
| FR-1 tekstinput | DEC-005 (teknologistakk) | T-002 | T-002 er delvis dekket; formateringsvarianter gjenstår. |
| FR-2 PDF-input | DEC-005 (PDF-verktøy) | T-001, T-008 | PDF-støtte og PDF-feil er ikke implementert/testet. |
| FR-3 sammendragslengde | DEC-005 (teknologistakk) | T-003 | Valg av lengde er ikke særskilt dekket. |
| FR-4 quizinnstillinger | DEC-001 (quizinteraksjon, fortsatt uavklart), DEC-005 (teknologistakk, fortsatt uavklart) | T-004, T-006 | Genereringsinnstillinger, antall og vanskelighetsgrad mangler full dekning; poengberegning i T-006 er betinget av et gruppevedtak under DEC-001. |
| FR-5 sammendrag og begrepsliste | DEC-003 (KI-tjeneste) | T-003 | Strukturelle/deterministiske kontroller finnes, men godkjent fasitbasert kvalitetsdekning mangler. |
| FR-6 quiz og fasit fra notater | DEC-003 (KI-tjeneste), DEC-005 (teknologistakk) | T-004, T-007 | Quizgenerering fra notatene og kildebinding er ikke implementert/dekket; demoquiz er ikke bevis for kravet. |
| FR-7 oversiktlig resultatvisning | DEC-001 (quizinteraksjon) | T-005, T-009 | Automatisert UI-dekning er delvis; veiledningsfri brukertest mangler. |
| FR-8 forståelige feilbeskjeder | DEC-003 (KI-tjeneste), DEC-005 (PDF-behandling) | T-001, T-008 | Input-/generatorfeil har delvis dekning; PDF- og ekstern tjenestefeil mangler. |
| NFR-1 kildebinding | DEC-003 (KI-tjeneste) | T-003, T-004, T-007 | Ingen godkjente testnotater/fasit; full kildebinding er ikke dokumentert. |
| NFR-2 korrekthetsforbehold | — | Ingen direkte testcase | Manglende direkte testdekning. |
| NFR-3 veiledningsfri arbeidsflyt | DEC-004 (testmodus) | T-009 | Automatisert AppTest er ikke en veiledningsfri brukertest. |
| NFR-4 hemmeligheter og feildetaljer | DEC-003 (KI-tjeneste/nøkkel) | T-008 | Delvis feilhåndtering; ekstern tjenestefeil er ikke dekket. |
| NFR-5 begrenset lagring | DEC-002 (lagring) | Ingen direkte testcase | Manglende direkte testdekning. |
| NFR-6 kursmateriale ved lagring | DEC-002 (lagring) | Ingen direkte testcase | Manglende direkte testdekning. |
| NFR-7 ekstern databehandling/oppbevaring | DEC-003 (KI-tjeneste/dataflyt) | Ingen direkte testcase | Manglende direkte testdekning. |

## Dekning på `main`

Snapshot: `444135e946b5635c812a24d44037c80fbf815e45`. Testfilen ved denne baselinen: [`tests/test_generator.py` på main-snapshotet](https://github.com/IBE160-2026/G27-isum-vijai/blob/444135e946b5635c812a24d44037c80fbf815e45/tests/test_generator.py). Dette snapshotet har seks pytest/unittest-tester. Det finnes ingen dokumentert manuell kontroll for dette snapshotet.

| ID | Implementasjon | Dekning | Samlet teststatus | Konkrete bevis og mangler |
|---|---|---|---|---|
| T-001 | Ikke implementert | Ingen | PLANLAGT | Ingen PDF-opplasting eller PDF-test. |
| T-002 | Implementert | Delvis | PLANLAGT | `GeneratorTests.test_valid_text_returns_demo_result`, `test_empty_text_is_rejected`, `test_whitespace_only_text_is_rejected`; gyldig tekst, tom tekst og whitespace kontrolleres, men linjeskift/uvanlig formatering er ikke særskilt verifisert. |
| T-003 | Implementert | Delvis | PLANLAGT | `test_valid_text_returns_demo_result` sjekker at sammendrag finnes, men ikke kvalitet mot godkjent fasit eller valgt lengde. |
| T-004 | Ikke implementert | Ingen | PLANLAGT | Quizspørsmål genereres ikke fra forelesningsnotatene på dette snapshotet. `test_valid_text_returns_demo_result` og `test_mock_has_expected_question_structure` verifiserer demonstrasjonsresultat/-struktur, ikke generering fra brukerens kildetekst. Antall, vanskelighetsgrad og kildebinding er heller ikke dekket. |
| T-005 | Ikke implementert | Ingen | PLANLAGT | Interaktiv quiz er ikke implementert i dette snapshotet. |
| T-006 | Ikke implementert | Ingen | PLANLAGT | Poengberegning er ikke implementert i dette snapshotet. |
| T-007 | Ikke implementert | Ingen | PLANLAGT | Påkrevd kildehenvisning fra quizspørsmål til notatavsnitt finnes ikke; eventuell demonstrasjonsquiz regnes ikke som implementasjon av kravet. |
| T-008 | Implementert | Delvis | PLANLAGT | `test_empty_text_is_rejected`, `test_whitespace_only_text_is_rejected`, `test_malformed_mock_result_is_rejected`, `test_unexpected_generator_error_is_wrapped`; dekker input-/generatorfeil, ikke uleselig PDF eller utilgjengelig ekstern KI-tjeneste. |
| T-009 | Implementert | Delvis | PLANLAGT | `test_valid_text_returns_demo_result` verifiserer mockresultat uten ekstern KI; full kjerneflyt i appen er ikke dekket av base-snapshotets tester. |

## Dekning på PROMPT 023-snapshotet

Snapshot: `89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503` (PR #1, ikke del av `main` mens PR-en er åpen). De SHA-pinnede lenkene til [`tests/test_generator.py` (11 tester)](https://github.com/IBE160-2026/G27-isum-vijai/blob/89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503/tests/test_generator.py) og [`tests/test_app.py` (4 tester)](https://github.com/IBE160-2026/G27-isum-vijai/blob/89ca55b40c26eac602e56e4d1b2c2e8ff1d0a503/tests/test_app.py) viser de committede testdefinisjonene. Den historiske kjøringen skjedde før commit på arbeidsfila som senere ble dette snapshotet; SHA-en er retrospektiv kilde-/tretilordning, ikke en commit som eksisterte da testene ble kjørt. Se [TEST_LOG.md](TEST_LOG.md) for proveniens. Ingen separat manuell kontroll er dokumentert.

| ID | Implementasjon | Dekning | Samlet teststatus | Konkrete bevis og mangler |
|---|---|---|---|---|
| T-001 | Ikke implementert | Ingen | PLANLAGT | Ingen PDF-opplasting eller PDF-tester. |
| T-002 | Implementert | Delvis | PLANLAGT | `test_empty_text_is_rejected`, `test_whitespace_only_text_is_rejected`, `test_non_string_text_is_rejected` i `tests/test_generator.py` og `test_empty_input_shows_validation_error_in_ui` i `tests/test_app.py`; linjeskift/uvanlig formatering er ikke særskilt testet. |
| T-003 | Implementert | Delvis | PLANLAGT | `test_valid_text_returns_local_content_and_demo_quiz`, `test_summary_uses_up_to_three_source_sentences_ranked_by_content` og `test_repeating_a_word_inside_one_sentence_does_not_change_ranking`; deterministisk tekstuttrekk er verifisert, men ingen godkjent fasit eller lengdevalg. |
| T-004 | Ikke implementert | Ingen | PLANLAGT | Spørsmål genereres ikke fra notater. `test_mock_has_expected_question_structure` kontrollerer demoens struktur og `tests/test_app.py::test_results_show_local_sources_and_demo_quiz_label` kontrollerer demoetiketten; disse testene dekker ikke quizgenerering fra kildetekst. Antall, vanskelighetsgrad og kildebinding er heller ikke verifisert. |
| T-005 | Implementert | Delvis | PLANLAGT | `tests/test_app.py::test_quiz_submission_shows_score_and_feedback_for_each_answer` kontrollerer ett blandet svarsett. Ikke alle riktige/gale svar og fullføringsvarianter er verifisert. |
| T-006 | Implementert | Delvis | PLANLAGT | `tests/test_app.py::test_quiz_submission_shows_score_and_feedback_for_each_answer` verifiserer 1 av 2; grenseverdier og alle-riktig/alle-gale er ikke verifisert. |
| T-007 | Ikke implementert | Ingen | PLANLAGT | Henvisning fra hvert quizspørsmål til relevant kildeavsnitt er ikke implementert/testet. Testen av lokal oppsummering og begreper viser ikke at demoquizens spørsmål har kildehenvisninger. |
| T-008 | Implementert | Delvis | PLANLAGT | `test_malformed_mock_result_is_rejected`, `test_unexpected_generator_error_is_wrapped` i `tests/test_generator.py` og `test_empty_input_shows_validation_error_in_ui` i `tests/test_app.py`; PDF-/ekstern tjenestefeil kan ikke testes fordi disse funksjonene mangler. |
| T-009 | Implementert | Delvis | PLANLAGT | `tests/test_app.py::test_results_show_local_sources_and_demo_quiz_label`, `test_quiz_submission_shows_score_and_feedback_for_each_answer`, `test_empty_concepts_have_a_clear_ui_message`, `test_empty_input_shows_validation_error_in_ui`; automatisert AppTest verifiserer UI-flyt med lokal behandling, ikke manuell kontroll. |

Før testtilfellene kan oppgraderes til `BESTÅTT`, må alle planlagte underkasus være dekket med resultatbevis, forventede resultater konkretiseres og testnotater/fasit godkjennes. Faktiske kjøringer registreres separat i [testloggen](TEST_LOG.md); malen [TEST_LOG_TEMPLATE.md](TEST_LOG_TEMPLATE.md) forblir mal.

### Reviewstatus

- **F-07 — lukket:** Dokumentasjonstesten leser lokale Git-objekter for PROMPT 023-SHA-en med `git show`, parser testfilene med Python `ast` og kontrollerer at alle dokumenterte testfunksjonsreferanser finnes. Negativ test dekker oppdiktet funksjonsnavn; manglende Git-objekter gir tydelig feil uten nettverk eller filkopiering.
- **F-10 — lukket:** Dokumentasjonstesten krever lenkemål til `tests/test_generator.py` ved full main-SHA `444135e946b5635c812a24d44037c80fbf815e45` og opplysningen om seks tester. Negative kontroller dekker feil SHA og feil testantall. Dette validerer dokumentasjonsreferansen; main-testene er ikke kjørt på nytt.
- **F-11 — lav, utsatt:** AppTest-kontrollen matcher `AppTest` generelt i miljøfeltet. En omtale i feil sammenheng kan gi falskt positivt testbevis. Oppfølging: avgrens matcher til utsagnet om at AppTest ble brukt som automatisert test.
- **F-12 — lav, utsatt:** Markdown-tabellparseren håndterer ikke escaped pipe-tegn. Nåværende testmatriser inneholder ingen slike celler; hvis formatet senere brukes der, kan tabellbevis bli feiltolket. Oppfølging: støtt escaped pipe eller avvis slike celler tydelig dersom en relevant testcase introduseres.
