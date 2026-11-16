# Sluttrevisjon – G27-isum-vijai

**Dato:** 2026-11-16. **Audit-branch:** `chore/ibe160-final-quality-audit`, fra `origin/main` `fef77e85f078b6e5ecdb82f09a903b8a6a1d4fc1`. Dette er en retrospektiv teknisk/dokumentasjonsrevisjon, ikke formell faglærergodkjenning.

**PR:** [#7](https://github.com/IBE160-2026/G27-isum-vijai/pull/7), åpen mot `main`, MERGEABLE/CLEAN ved siste GitHub-kontroll; ikke merget.

## Sammendrag

MVP-ens beskrevne kjernestrøm finnes: lokal tekst/PDF-behandling, valgfri Gemini-generering etter aktivt samtykke og brukerhandling, strukturerte sammendrag/begreper/quiz, interaktiv quizretting og poengsum. Lokal quiz er demo-data. Gemini bruker standard `gemini-3.5-flash-lite` med `GEMINI_MODEL`-overstyring. DEC-003 tillater bare avgrenset prototypebruk. Ingen produksjonsbruk med personopplysninger er godkjent.

Ingen P0/P1 kodefeil ble funnet i denne statiske kontrollen og regresjonssuiten. P2-forbedring: tre syntetiske, dokumenterte testcaser og eksplisitt README nøkkelfri demooppskrift er lagt til. Auditfiler markerer krav som `PARTIAL` eller `NOT VERIFIED` der dokumentasjon mangler.

Høgskolens [offisielle emnebeskrivelse for IBE160 Høst 2026](https://www.himolde.no/studier/emner/log/2026/host/ibe160.html) beskriver mappevurdering med prosjektkode/funksjonalitet (70 %) og refleksjonsrapport (30 %). Beskrivelsen er ikke gruppens fulle oppgave eller sensorens detaljrubrikk; ingen refleksjonsrapport ble funnet i repoet.

## Faglærerkriterier

| Område | Status | Evidens / begrensning |
|---|---|---|
| Prosess og KI-styring – 30 % | PARTIAL | Brief, beslutninger, specs, test- og promptlogger finnes; prompt 027 og flere eldre originalprompts mangler. Et kilde-sporbart BMAD-PRD-utkast finnes, men står som `draft`/ikke build-ready; separate komplette epics/stories ble ikke funnet. |
| Funksjonalitet og omfang – 20 % | PARTIAL | Interaktiv quiz/score, PDF- og Gemini-mockflyter er automatisert testet; lokal quiz er eksplisitt demo. Brukerrapporterte Gemini-resultater er ikke gjentatt i denne auditten. |
| Kvalitetssikring og testing – 15 % | PARTIAL | Sluttkjøring: 109 automatiserte tester, 6 docs-tester og 3 syntetiske fixtures; ingen uavhengig semantisk modellfasit. |
| Design og brukeropplevelse – 10 % | PARTIAL | UI-tilstandsflyter AppTestet; ingen formell visuell review/ny manuell brukertest i denne auditten. |
| Kodekvalitet og arkitektur – 10 % | PARTIAL | Modulgrenser, mockbar adapter og validering er direkte inspisert/testet; prompt injection reduseres i instruks, kan ikke fullstendig elimineres. |
| README og kjørbarhet – 10 % | PARTIAL | Clean Python 3.12 venv installert; lokal server health check uten nøkkel ga 200. Nøkkelfri Gemini-generering er med vilje utilgjengelig. |
| Repository-ryddighet – 5 % | PASS | `.gitignore` dekker venv/secrets; denne branchens diff er dokumentasjon/tester, ingen lokale secrets. |

## Funn og håndtering

- **P2 – testdata ikke konkretisert:** `testdata/README.md` meldte ingen testnotater. Lagt til tre syntetiske case med fakta, begreper og ukjent påstand samt deterministiske tester.
- **P2 – README nøkkelfri prøveflyt:** La til steg for lokal demo, tydelig at quiz er fast demo og at Gemini krever key.
- **PARTIAL – kildeforankring:** JSON-schema sikrer format. Literal-sitatkontroll avviser sitat som mangler, men gir ikke semantisk relevans eller faktagaranti; beholdes og beskrives.
- **NOT VERIFIED – full emnekrav:** Repoet har ikke fullstendig oppgavetekst/sensorveiledning. Et PRD-utkast finnes, men er ikke den offisielle gruppeoppgaven og er fortsatt ikke build-ready. Gruppen må sammenholde leveransen med emneplattformen.
- **PARTIAL – refleksjonsrapport:** Offisiell emnebeskrivelse bekrefter gruppevis rapport (30 %) og temaer, men ikke omfang/format/leveringssted. En tydelig merket gruppeoutline er laget lokalt i `REFLECTION_REPORT_GROUP_DRAFT.md`; den er ikke ferdig, ikke personlig og ikke inkludert i PR. Gruppen må fullføre og sende den i riktig kanal.
- **Promptarkivering:** PROMPT 029 og PROMPT 030 er arkivert i fulltekst; PROMPT 027, flere eldre originaltekster og PROMPT 019s redigering består som historiske hull.

## Direkte svar

1. **Er MVP teknisk ferdig?** Kjernestrømmen er implementert og automatisert testet, men det er en prototype med dokumenterte begrensninger; “ferdig” avhenger av faktisk innleveringsrubrikk.
2. **Alle tilgjengelige faglærerkommentarer håndtert?** Vurdert; flere er PARTIAL, særlig måling av semantisk kvalitet, visuell UX og komplett prosessarkiv.
3. **Dokumentasjon konsistent med kode?** Oppdatert retrospektivt for gjeldende funksjoner; se traceability for restgap.
4. **Kan sensor kjøre uten API-nøkkel?** Ja for lokal demo, bekreftet med clean install og server-health check; ikke for AI-generering.
5. **Promptarkiv så komplett som kilder tillater?** PROMPT 029 og 030 er arkivert i fulltekst; PROMPT 027 og eldre originale tekster mangler, og PROMPT 019 er personvernredigert.
6. **Uløste kritiske feil?** Ingen identifisert i denne kontrollen; automatisk sitatkontroll er begrenset.
7. **Klar for demonstrasjon?** Teknisk lokal demo ja; AI-demo krever gyldig key og tillatte syntetiske/offentlige/anonymiserte notater.
8. **Klar for innlevering?** Ikke endelig verifiserbart før formell oppgavetekst og endelige krav sammenholdes.
9. **Ikke verifisert?** Gruppens fullstendige assignment/detaljrubric, rapportformat/-omfang/-kanal, visuell brukertest, semantisk correctness og faktisk Gemini-generering i denne auditten.
10. **Manuelt:** Hent oppgavetekst og refleksjonsrapportinstruks fra Canvas; gruppen må gjennomgå refleksjonsutkastet og skrive egne erfaringer; utfør visuell demo med tillatte syntetiske notater.

Testbevis: [`FINAL_TEST_REPORT.md`](FINAL_TEST_REPORT.md). Krav og lærerfeedback: [`REQUIREMENTS_TRACEABILITY.md`](REQUIREMENTS_TRACEABILITY.md), [`TEACHER_FEEDBACK_RESOLUTION.md`](TEACHER_FEEDBACK_RESOLUTION.md). Sjekkliste: [`FINAL_SUBMISSION_CHECKLIST.md`](FINAL_SUBMISSION_CHECKLIST.md).
