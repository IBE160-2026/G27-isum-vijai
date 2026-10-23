# Tillegg: vurdering av foreslått teknologistakk

Dette tillegget bevarer teknologiinnspillene fra PROMPT 021 for senere arkitekturarbeid. Ingen av forslagene nedenfor er vedtatt; DEC-005 i `docs/decisions/DECISION_LOG.md` står fortsatt som uavklart.

| Forslag | Vurdering | Uavklart før valg |
|---|---|---|
| Python | Relevant kandidat for rask applikasjonsutvikling og integrasjon med Python-bibliotekene i vurderingen. | Gruppens kompetanse, prosjektkrav og valgt driftsmåte. |
| Streamlit | Relevant kandidat for et raskt UI med interaktive felt og resultatvisning. | Om rammens mønster passer ønsket brukeropplevelse, interaktiv quiz og tilgjengelighet. |
| PyMuPDF | Relevant kandidat for uttrekk av tekst fra PDF med maskinlesbart innhold. | Uttrekk kan gi uventet leserekkefølge/linjeskift; skannede PDF-er trenger OCR og ytterligere OCR-komponent/data. Avklar støtteomfanget før valg. |
| pytest | Relevant kandidat for automatiserte Python-tester og testoppdagelse. | Endelig testoppsett følger valgt stakk. |
| KI-tjeneste | Kan generere sammendrag, begreper og quiz. | Leverandør, modell, pris, nøkkel, personvern og feilgrenser er ikke besluttet. Ikke lås integrasjon før disse er avklart. |
| Lokal testmodus | Ferdige eksempelresultater eller en mock kan støtte demonstrasjon og repeterbare tester uten API-nøkkel. | Om testmodus skal være del av produktet, og hvordan den merkes og aktiveres. |

**Foreløpig stackforslag, ikke vedtak:** Python + Streamlit + PyMuPDF for tekstbasert PDF + pytest, med en lokal mock/testmodus. Behandle OCR som utenfor første implementasjon inntil gruppen bestemmer noe annet. KI-provider legges til først etter beslutning om kostnad, nøkkel og dataflyt. Dette forslaget passer ønsket om en enkel demonstrerbar arbeidsflyt, men krever gruppens godkjenning og kontroll mot emnekrav.

**Kildestøtte for vurderingen:** [Python Tutorial](https://docs.python.org/3/tutorial/index.html) beskriver Python som egnet til rapid application development; [Streamlit Get Started](https://docs.streamlit.io/get-started) beskriver interaktive widgets og app-layouts; [PyMuPDF text extraction](https://pymupdf.readthedocs.io/en/latest/recipes-text.html) dokumenterer tekstuttrekk og mulige layout-/leserekkefølgeproblemer, mens [PyMuPDF OCR](https://pymupdf.readthedocs.io/en/latest/recipes-ocr.html) beskriver OCR-forutsetninger; [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html) dokumenterer testoppdagelse og kjøring.

Disse alternativene er vurderingspunkter, ikke arkitekturvalg. BMAD Architecture bør dokumentere endelige valg etter at gruppen har tatt dem.
