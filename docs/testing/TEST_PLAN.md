# Testplan

**Status for alle testtilfeller: PLANLAGT. Ingen av testene nedenfor er dokumentert som gjennomført.** Planen beskriver hva som skal kontrolleres når funksjonaliteten finnes. Testdata opprettes separat i `testdata/` når gruppen har godkjent egnet, ufølsomt materiale.

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

Før testene kan gjennomføres må relevante funksjoner finnes, forventede resultater konkretiseres og testnotater/fasit godkjennes. Registrer faktiske kjøringer i [testloggmalen](TEST_LOG_TEMPLATE.md); ikke endre status til gjennomført uten resultatbevis.
