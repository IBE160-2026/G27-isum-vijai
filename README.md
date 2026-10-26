# G27 — Team Utviklerne

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026 (15 studiepoeng).

Repoet inneholder gruppens applikasjon og dokumentasjon av utvikling, testing og kvalitetssikring med KI.

## Medlemmer

- Thor E Isum
- Akshayah Vijai
- Abena Vijai

## Prototype: forelesningsnotater til sammendrag og quiz

En liten Streamlit-prototype lar deg lime inn notater, hente et enkelt utdragssammendrag og sentrale begreper fra teksten, og svare på en kort quiz. Sammendraget velger inntil tre innholdsrike originalsetninger, og begrepslisten rangerer hyppige ord fra notatene. Dette er enkel, lokal tekstbehandling — **ikke KI-generering**. Quizspørsmålene er faste demonstrasjonsdata og er ikke laget fra notatene. Prototypen bruker ingen KI-tjeneste eller API-nøkkel.

Dette er et foreløpig prototypvalg for å demonstrere kjerneflyten, ikke en vedtatt produksjonsarkitektur. PDF-opplasting/-uttrekk, ekstern KI, lagring og testmodus som produktfunksjon er ennå ikke implementert. PyMuPDF er ikke nødvendig for denne versjonen.

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

Testene i `tests/test_generator.py` er kompatible med pytest og bruker også `unittest`, slik at logikken kan testes med standardbiblioteket:

```bash
python -m unittest discover -s tests -v
pytest -q
```

Kjøring med `pytest` krever at avhengighetene i `requirements.txt` er installert. Testene dekker lokal behandling av notater, kilde- og demo-merking, tekstvalidering, quizstruktur, avvisning av ugyldige mockresultater og kontrollert håndtering av uventede generatorfeil.
