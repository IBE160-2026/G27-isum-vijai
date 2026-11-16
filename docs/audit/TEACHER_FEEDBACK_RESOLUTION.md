# Faglærerfeedback – oppfølging

Kilden er `tilbakemelding-product-brief.md`, datert 2026-10-06 og knyttet til `product-brief.md` ved commit `dc2a630`. Dette er feedback på tidlig brief, ikke den fullstendige oppgaveteksten. Tabellen er laget retrospektivt 2026-11-16 og påstår ikke at løsningene var planlagt på vurderingstidspunktet.

| Opprinnelig kommentar | Hva gruppen gjorde / nåværende bevis | Relevant fil/test | Status | Gjenstående |
|---|---|---|---|---|
| For lite omfang; foreslå quizbesvarelse/score, kildeavsnitt eller lagring | Quiz har radio-svar, fasit, forklaringer og score. Ingen lagring. Gemini-resultat krever bokstavelige kildeutdrag. | `app.py`; `tests/test_app.py`; Sprint 002 spec | PASS | Sitatkontroll er heuristisk; lokal quiz er kun demo |
| Suksesskriterier ikke målbare; foreslå 2–3 faste notater | Tre syntetiske notater og forventede fakta/begreper/ukjente påstander ligger i testdata | `testdata/synthetic_cases.json`, `tests/test_synthetic_cases.py` | PARTIAL | Ingen gold-standard for fri modellkvalitet; semantic evaluation krever menneskelig fagkontroll |
| Ingen språkmodell-/nøkkel-/kostnadsplan; sensor uten key | Gemini-modus, miljø/Streamlit nøkkel, valgfri modell og lokal modus finnes; README beskriver test uten key | README, `prototype/gemini_service.py`, DEC-003 | PARTIAL | Kostnad, kvoter og leverandørdataflyt må undersøkes ved eventuell bredere bruk |
| Primærbruker for generell | Briefen beskriver student med digitale forelesningsnotater; retrospektiv presisering knytter den til repetisjon og eksamensforberedelse | `product-brief.md` | PARTIAL | Persona og brukertest mangler |
| PDF kan ha rotete tekst / lesbarhet | pypdf trekker ut tekst; størrelse/sider/tegn avgrenset; ugyldig og tekstløs PDF meldes | `prototype/pdf_ingestion.py`, `tests/test_pdf_ingestion.py`, README | PARTIAL | OCR, kolonner, tabeller og visuell ekstraksjonskontroll ikke støttet |
| KI kan finne på stoff; bruk testnotater og mock | Prompt ber om kildesitater og ignorerer instruksjoner i notater; schema/quote validering; tre syntetiske cases; mocktester | `prototype/gemini_service.py`, testdata og tests | PARTIAL | Prompt injection og falske/irrelevante sitater kan ikke elimineres av heuristikken |
| BMAD-prosess/sporbarhet svak; få commits og prompts | README, decision log, specs, testplan/logg, promptlogg og gjenfinningsgap dokumenterer senere prosess | `docs/`, `_bmad-output/`, git log | PARTIAL | Historisk prompt 027 og flere originalprompts mangler; full audit-dokumentasjon er retrospektiv |
| Skissér grensesnitt/finn tilbake til kilde | Streamlit har tydelig input/modus/resultat/quiz flyt; Gemini viser kildekontrollforbehold | `app.py`, README | PARTIAL | Ingen formell UX-skisse eller ny manuell visuell/brukertest i denne revisjonen |

Kildens øvrige weighted criteria er kartlagt separat i `REQUIREMENTS_TRACEABILITY.md`. Ingen formell godkjenning fra faglærer hevdes.
