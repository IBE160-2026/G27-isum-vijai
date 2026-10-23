---
title: 'Første fungerende prototype for notater og quiz'
type: 'feature'
created: '2026-10-23'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Repositoryet inneholder ingen applikasjonskode. Gruppen trenger en liten prototype som viser kjerneflyten fra tekstinput til resultat uten avhengighet av en ekstern KI-tjeneste.

**Approach:** Lag en isolert Python/Streamlit-prototype med lokal mock, tydelig merking av demonstrasjonsdata, norsk feilhåndtering, pytest-kompatible tester og oppstartsdokumentasjon. Dette er et foreløpig prototypvalg, ikke en beslutning om produksjonsarkitektur. Ikke legg til PDF eller ekstern KI i denne iterasjonen.

</frozen-after-approval>

## Implementation Notes

- Foreløpig prototypestakk: Python 3.12 + Streamlit; lokal deterministisk mock. Ingen produksjonsbeslutning.
- Opprettet UI i `app.py`, logikk/mock i `prototype/`, tester i `tests/`, avhengigheter i `requirements.txt`, pytest-konfigurasjon i `pytest.ini`, lokal-only Streamlit-binding i `.streamlit/config.toml`, og kjøreinstruksjoner i README.
- Testene validerer input, resultatstruktur (inkludert ugyldige mockresultater) og kontrollert feil. Pytest og unittest: 6 bestått hver. `compileall` bestod. Streamlit-helsesjekken `/_stcore/health` svarte `ok` på `127.0.0.1:8765`; serveren ble stoppet.
- Avhengigheter ble installert bare etter at behovet var forklart og godkjent, i ignorert `.venv/`. Den eksisterende PRD-`.memlog.md` ble ikke åpnet for skriving eller endret.

## Review Triage Log

- **patch (low):** Spec-status var fortsatt `in-progress` selv om implementering og verifisering var fullført; frontmatter er nå `done`.
- **patch (medium):** README beskrev avhengighetene som uinstallerte uten å skille første kontroll fra senere installasjon; teksten angir nå begge tidspunktene korrekt.
- **patch (low):** Testene verifiserte ikke at ugyldig mockstruktur avvises; la til test for ugyldig alternativtype og bekreftet `ResultGenerationError`.
- **patch (low):** README sa Python 3.11+ mens bare Python 3.12-oppskriften var vist; dokumentet angir nå 3.12 som versjon for oppskriften.
- **patch (low):** Windows-aktiveringskommandoen hadde doble bokstavelige skråstreker; README viser nå PowerShell-kommandoen `.venv\\Scripts\\Activate.ps1`.
- **patch (medium):** Quizvalideringen godtok tom spørsmålstekst og tom forklaring; begge feltene må nå inneholde ikke-blank tekst.
- **patch (medium):** Quizvalideringen godtok ikke-tekstlige svaralternativer som kunne feile i Streamlit-radioen; alternativer må nå være ikke-tomme strenger.
- **patch (low):** Strukturtesten sjekket ikke at spørsmål/forklaring var ikke-tomme eller at svaralternativer var strenger; forventningene er nå uttrykkelig testet.
- **patch (low):** README omtalte kontrollert generatorfeilhåndtering, men manglet testen for ugyldig returverdi; den nye testen dekker dette sammen med uventet generatorfeil.
- **patch (low):** UI-innledningen forklarte ikke at innlimt tekst bare brukes i inputkontrollen; den opplyser nå at demoresultatene ikke påvirkes av notatene.
