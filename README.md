# G27 – Forelesningsnotater til sammendrag og quiz

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026. Dette er en prototype, ikke et produksjonssystem.

Applikasjonen er laget for studenter som vil repetere digitale forelesningsnotater. Den tar imot tekst eller en PDF og viser et sammendrag, sentrale begreper og en flervalgsquiz. Lokal modus fungerer uten API-nøkkel. Valgfri Gemini-modus lager KI-generert innhold fra notatene og krever nettverk og egen Gemini API-nøkkel.

## Funksjoner og modus

| Funksjon | Lokal modus (standard) | Gemini AI |
|---|---|---|
| Tekstinput | Ja | Ja |
| PDF med maskinlesbar tekst | Ja, uttrekk lokalt | Ja, uttrekk lokalt; teksten sendes først til Gemini når brukeren starter generering og samtykker |
| Sammendrag og begreper | Enkel, deterministisk tekstbehandling | KI-generert fra notatene |
| Quiz | Faste demonstrasjonsspørsmål, ikke laget fra notatene | KI-genererte spørsmål fra notatene; det kan bli færre enn ønsket hvis notatene ikke støtter flere |
| Svar, fasit og poeng | Ja | Ja, med forklaringer |
| API-nøkkel | Nei | Ja |

I Gemini-modus kan brukeren velge sammendragslengde (kort, middels, lang), vanskelighetsgrad (lett, middels, vanskelig) og 1–10 quizspørsmål. Disse valgene vises ikke i lokal modus.

## Teknologistakk

- Python (ren installasjon testet med Python 3.12.12; repositoryet angir ikke en egen minimumsversjon).
- Streamlit for brukergrensesnittet.
- `pypdf` for lokalt tekstuttrekk fra PDF.
- Googles `google-genai` SDK for den valgfrie Gemini Developer API-integrasjonen.
- `pytest` og Python `unittest` for tester. Streamlit AppTest brukes til UI-regresjoner.

Avhengigheter og versjonsintervaller står i [`requirements.txt`](requirements.txt). Det finnes ingen separat lockfil; en ny installasjon kan derfor hente nyere kompatible pakkeversjoner innenfor intervallene.

## Installer og start

Du trenger Git og Python 3.12. `python3.12 --version` (macOS/Linux) eller `py -3.12 --version` (Windows) skal vise Python 3.12.x. Installer pakkene fra prosjektets `requirements.txt` i et virtuelt miljø.

### macOS og Linux

```bash
git clone https://github.com/IBE160-2026/G27-isum-vijai.git
cd G27-isum-vijai
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### Windows PowerShell

```powershell
git clone https://github.com/IBE160-2026/G27-isum-vijai.git
cd G27-isum-vijai
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### Windows Command Prompt

```bat
git clone https://github.com/IBE160-2026/G27-isum-vijai.git
cd G27-isum-vijai
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Når serveren starter, åpner du den lokale adressen som vises i terminalen, normalt <http://localhost:8501>. Avslutt serveren med `Ctrl+C`. For å starte senere må du først gå til prosjektmappen og aktivere miljøet på nytt; bruk deretter `python -m streamlit run app.py`.

## Demonstrer uten Gemini-nøkkel

Du trenger ikke opprette konto eller API-nøkkel for å prøve den lokale demonstrasjonen:

1. Start applikasjonen med kommandoene over.
2. La **Genereringsmodus** stå på **Lokal**.
3. Velg **Tekst** og lim inn syntetiske notater, eller velg **PDF** og last opp en maskinlesbar PDF.
4. Velg **Generer læringsressurser**.
5. Les sammendraget og begrepene, svar på demoquizen og trykk **Sjekk svar** for poengsum og forklaringer.

Lokalt sammendrag og begreper lages med enkel tekstbehandling. Quizspørsmålene er faste demonstrasjonsdata, ikke generert fra innholdet du limer inn eller laster opp. Dette er en enkel demo, ikke en KI-basert quiztest. Eksempler på syntetiske testnotater finnes i [`testdata/synthetic_cases.json`](testdata/synthetic_cases.json); de brukes også av automatiserte tester.

## Valgfri Gemini-modus

Gemini er valgfritt. Før bruk må du ha en Gemini API-nøkkel fra Google AI Studio og nettverkstilgang. API-bruk kan være underlagt kvoter og kostnader; kontroller gjeldende leverandørvilkår og priser selv. Prosjektet lover ikke gratis bruk, bestemt lagringstid eller sletting.

Konfigurasjonen leses fra miljøvariablene `GEMINI_API_KEY` og `GEMINI_MODEL`. Standardmodellen er `gemini-3.5-flash-lite`; `GEMINI_MODEL` kan overstyre den. Nøkkelen kan også gis gjennom lokal Streamlit Secrets-konfigurasjon. Hold nøkkelen privat: ikke skriv den i kildekode, README, GitHub eller terminalutskrifter. `.streamlit/secrets.toml` er en lokal konfigurasjonsfil som skal holdes utenfor Git.

Sett variablene i terminalen **før** du starter Streamlit:

macOS/Linux:

```bash
(
printf "Gemini API-nøkkel (skjult): "
read -s GEMINI_API_KEY
printf '\n'
export GEMINI_API_KEY
# Valgfri overstyring; kan utelates for standardmodellen:
export GEMINI_MODEL="gemini-3.5-flash-lite"
python -m streamlit run app.py
)
```

Windows PowerShell:

```powershell
$secureKey = Read-Host "Gemini API-nøkkel" -AsSecureString
$env:GEMINI_API_KEY = [System.Net.NetworkCredential]::new("", $secureKey).Password
# Valgfri overstyring; kan utelates for standardmodellen:
$env:GEMINI_MODEL = "gemini-3.5-flash-lite"
python -m streamlit run app.py
```

Stopp Streamlit med `Ctrl+C`. Lukk terminalen etterpå for å fjerne nøkkelen fra terminalens miljø.

I applikasjonen velger du **Gemini AI**, legger inn tekst eller laster opp PDF, velger innstillinger, leser personvernmeldingen og krysser av samtykke. Trykk deretter **Generer læringsressurser**. Opplasting alene sender ikke innhold til Gemini. Endrer du notatene, PDF-en eller modus, må du samtykke på nytt. For å gå tilbake til nøkkelfri demonstrasjon starter du applikasjonen på nytt uten Gemini-variablene og velger **Lokal**.

Gemini behandler notatinnhold eksternt hos Google. DEC-003 tillater prototypen bare med syntetiske, offentlig tilgjengelige eller anonymiserte notater uten personopplysninger eller konfidensielt innhold. Dette er ikke juridisk, institusjonell eller produksjonsgodkjenning. Følg gjeldende Google-vilkår og emnekrav.

## PDF-grenser og andre begrensninger

- PDF-tekst trekkes ut lokalt i minnet med `pypdf`; appen lagrer ikke opplastingen varig.
- Bare gyldige, ukrypterte PDF-er med maskinlesbar tekst støttes. Skannede dokumenter og OCR støttes ikke.
- Grensene er 10 MiB per fil, 200 sider og 1 000 000 tegn uttrekket tekst. En PDF uten uttrekkbar tekst avvises.
- KI-resultater kan være feil eller ufullstendige. Gemini kan returnere færre quizspørsmål enn ønsket når notatene ikke gir tilstrekkelig grunnlag.
- Appen kontrollerer at sitatene i Gemini-resultatet finnes i notatene etter normalisering av store/små bokstaver og mellomrom. Dette er en tekstlig kontroll, ikke en semantisk verifikasjon eller garanti for korrekthet.
- Lokal quiz er demo-data og gjenspeiler ikke brukerens notater.
- Gemini-prototypen skal ikke brukes med personopplysninger eller konfidensielt innhold.

## Tester

Aktiver det virtuelle miljøet og stå i prosjektroten. Kjør hele pytest-suiten:

```bash
python -m pytest -q
```

Kjør også testene som bruker Python-standardbibliotekets `unittest`-runner:

```bash
python -m unittest discover -s tests -v
```

Testene i `tests/` omfatter Streamlit AppTest, lokal generator, quizretting, syntetiske PDF-er og Gemini-adapter. Automatiserte Gemini-tester bruker mock-klient og gjør ingen eksterne forespørsler. PDF-testene bruker syntetiske filer. En testbestått-suite beviser ikke semantisk korrekthet i frie Gemini-svar.

Tidligere manuelle Gemini-tekst- og PDF-resultater er brukeroppgitte i [`docs/testing/TEST_LOG.md`](docs/testing/TEST_LOG.md). De ble ikke gjentatt som del av README-kontrollen. En manuell Gemini-test krever brukerens egen nøkkel og sender notatinnhold eksternt; bruk bare data som er tillatt etter DEC-003.

## Prosjektfiler og dokumentasjon

- `app.py` – Streamlit-applikasjonens startfil.
- `prototype/generator.py`, `prototype/mock_data.py` – lokal tekstbehandling og fast demoquiz.
- `prototype/pdf_ingestion.py` – PDF-tekstuttrekk og grenser.
- `prototype/gemini_service.py` – Gemini-konfigurasjon, generering og validering.
- `tests/` – automatiserte tester; `testdata/` – syntetiske notater.
- [`product-brief.md`](product-brief.md) – produktbrief.
- [`docs/bmad/WORKFLOW_STATUS.md`](docs/bmad/WORKFLOW_STATUS.md) og [`_bmad-output/implementation-artifacts/`](_bmad-output/implementation-artifacts/) – BMAD-status og implementasjonsspesifikasjoner.
- [`docs/decisions/DECISION_LOG.md`](docs/decisions/DECISION_LOG.md) – beslutninger, inkludert avgrensningene i DEC-003.
- [`docs/testing/TEST_PLAN.md`](docs/testing/TEST_PLAN.md) og [`docs/testing/TEST_LOG.md`](docs/testing/TEST_LOG.md) – testplan og historisk testlogg.
- [`docs/CODEX_PROMPT_LOG.md`](docs/CODEX_PROMPT_LOG.md), [`docs/prompts/`](docs/prompts/) og [`docs/prompts/PROMPT_HISTORY_GAPS.md`](docs/prompts/PROMPT_HISTORY_GAPS.md) – promptarkiv og dokumenterte historiske hull.
- [`docs/audit/REQUIREMENTS_TRACEABILITY.md`](docs/audit/REQUIREMENTS_TRACEABILITY.md) og [`docs/audit/TEACHER_FEEDBACK_RESOLUTION.md`](docs/audit/TEACHER_FEEDBACK_RESOLUTION.md) – retrospektiv kravkontroll, kjente begrensninger og lærerfeedback.

## Feilsøking

- **Python 3.12 finnes ikke:** Installer Python 3.12, åpne en ny terminal, og kontroller med `python3.12 --version` (macOS/Linux) eller `py -3.12 --version` (Windows).
- **`streamlit`/`pytest` mangler eller kommandoen finnes ikke:** Kontroller at `.venv` er aktivert, og kjør `python -m pip install -r requirements.txt` fra prosjektroten.
- **Virtuelt miljø starter ikke:** Opprett det på nytt med kommandoen for operativsystemet over. På Windows kan du bruke Command Prompt-aktiveringen dersom PowerShell ikke tillater `Activate.ps1`.
- **Streamlit åpner ikke eller porten er opptatt:** Kontroller terminalens feilmelding. Streamlit viser hvilken lokal URL/port som brukes; avslutt en annen prosess på porten eller start med `python -m streamlit run app.py --server.port 8502` og åpne URL-en som vises.
- **PDF avvises:** Bruk en gyldig, ukryptert PDF under 10 MiB og 200 sider med maskinlesbar tekst. Skannede PDF-er krever OCR, som ikke er implementert.
- **Gemini sier at API-nøkkel mangler:** Sett `GEMINI_API_KEY` i samme terminal før du starter Streamlit, eller konfigurer lokal Streamlit Secrets. Nøkkelfri bruk fungerer bare i lokal modus.
- **Gemini returnerer en feilkode:** Kontroller nettverk og at modellen er tilgjengelig for nøkkelen. Appen viser trygge kategorier som `[GEMINI-AUTH]`, `[GEMINI-ACCESS]`, `[GEMINI-MODEL]`, `[GEMINI-QUOTA]`, `[GEMINI-RATE-LIMIT]` eller `[GEMINI-NETWORK]`. Ikke del API-nøkkelen. En modelliste-diagnostikk kan gjøre et eksternt `models.list()`-kall og skal bare kjøres etter uttrykkelig godkjenning; den utfører ikke generering.

## Vurderings- og prosessdokumentasjon

Prosjektets retrospektive kontroll mot tilgjengelige vurderingsområder ligger i [`docs/audit/REQUIREMENTS_TRACEABILITY.md`](docs/audit/REQUIREMENTS_TRACEABILITY.md) og [`docs/audit/TEACHER_FEEDBACK_RESOLUTION.md`](docs/audit/TEACHER_FEEDBACK_RESOLUTION.md). De markerer `PARTIAL` og `NOT VERIFIED` der full gruppespesifikasjon, detaljert sensorveiledning, visuell testing eller semantisk KI-kvalitet mangler. Se også [`docs/README.md`](docs/README.md) for dokumentasjonsinnganger.
