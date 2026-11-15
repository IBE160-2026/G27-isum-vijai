# G27 — Team Utviklerne

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026 (15 studiepoeng).

Repoet inneholder gruppens applikasjon og dokumentasjon av utvikling, testing og kvalitetssikring med KI.

## Medlemmer

- Thor E Isum
- Akshayah Vijai
- Abena Vijai

## Prototype: forelesningsnotater til sammendrag og quiz

En liten Streamlit-prototype lar deg lime inn notater eller laste opp en PDF. PDF-er behandles lokalt i minnet med `pypdf`; bare maskinlesbar tekst støttes. Skannede PDF-er har ikke OCR-støtte. Filer over 10 MiB, PDF-er med mer enn 200 sider og uttrekk over 1 000 000 tegn avvises. I lokal modus velges sammendrag og begreper med enkel tekstbehandling, og quizspørsmålene er faste demonstrasjonsdata.

Dette er et foreløpig prototypvalg for å demonstrere kjerneflyten, ikke en vedtatt produksjonsarkitektur. Valgfri ekstern KI er nå tilgjengelig som Gemini-modus; varig lagring og egen testmodus er ikke implementert. PDF-beslutningen gjelder bare lokal tekstuttrekking i denne MVP-funksjonen; DEC-005 står fortsatt åpen for øvrige teknologivalg.

Lokal modus er fortsatt standard og bruker enkel lokal tekstbehandling — **ikke KI-generering**. Quizspørsmålene i lokal modus er faste demonstrasjonsdata og er ikke laget fra notatene. Valgfri Gemini-modus kan generere sammendrag, forklarte begreper og notatbasert quiz. Før hver generering kreves aktiv bekreftelse på at notatene sendes til Google for ekstern behandling. Google opplyser at Free Tier-data kan brukes til produktforbedring; genererte resultater kan være feil. Ingen notater lagres varig av appen. Ikke send sensitive eller fortrolige notater.

Gemini-resultatet ber også om sitater fra notatene for sammendrag, begreper, spørsmål, svar og forklaringer. Appen avviser svar der disse sitatene ikke finnes i kildeteksten etter normalisering av store/små bokstaver og whitespace. Denne tekstkontrollen kan ikke garantere at sitatene semantisk underbygger innholdet eller at resultatet er feilfritt.

Gemini-nøkkel konfigureres som `GEMINI_API_KEY` i miljøet eller Streamlit Secrets. Valgfri modell konfigureres med `GEMINI_MODEL` (standard `gemini-3.5-flash-lite`). Appen foretar ikke Gemini-kall ved opplasting alene. Bruk bare notater du har lov til å sende til ekstern behandling.

Samtykke bekreftes før Gemini-generering og nullstilles når du endrer notatene, PDF-filen eller genereringsmodus. Du må bekrefte på nytt før nye notater sendes.

### Starte lokalt

Den dokumenterte oppskriften bruker Python 3.12. Opprett et isolert miljø og installer pakkene som står i `requirements.txt`:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Åpne adressen Streamlit viser i terminalen. Prototypen er konfigurert til å lytte bare på `127.0.0.1` på denne maskinen. I Windows PowerShell aktiveres miljøet med `.venv\Scripts\Activate.ps1`.

Ved første kontroll manglet `streamlit` og `pytest` i utviklingsmiljøets standard-Python. Etter at installasjonsbehovet var forklart og godkjent, ble avhengighetene installert i prosjektets isolerte `.venv` og brukt til verifiseringen.

### Tester

Testene i `tests/test_generator.py` er kompatible med pytest og bruker også `unittest`, slik at logikken kan testes med standardbiblioteket. Pytest kjører i tillegg Streamlit UI-regresjonstestene i `tests/test_app.py` med AppTest:

```bash
python -m unittest discover -s tests -v
pytest -q
```

Kjøring med `pytest` krever at avhengighetene i `requirements.txt` er installert. Testene dekker lokal behandling av notater, PDF-uttrekk/feil, kilde- og demo-merking, tekstvalidering, quizstruktur, avvisning av ugyldige mockresultater og kontrollert håndtering av uventede generatorfeil.
