# Prompt-historikk – hull og verifiseringsstatus

Kontroll utført 2026-11-15 i `/private/tmp/G27-isum-vijai-mvp-002-gemini`, branch `feature/mvp-002-gemini-ai`. Kildene var prosjektets dokumenter, tilgjengelige lokale branches/refs og Git-objekter for sporbare commits. Ingen sessionlogg ble åpnet: tilgjengelige verktøy ga ikke et trygt, prompt-only uttrekk som kunne utelukke hemmeligheter. `.memlog.md`, Secrets og originalarbeidsmappen ble ikke åpnet eller endret.

## Nummererte oppføringer før kontrollen

`docs/CODEX_PROMPT_LOG.md` inneholdt 30 overskrifter av formen `## PROMPT NNN`, fordelt på 27 unike numre: PROMPT 001–026 og PROMPT 028. PROMPT 023 har tre overskrifter for hovedoppdrag og oppfølging; PROMPT 028 har to overskrifter for ulike integrasjonsfaser. Dette er historiske underoppføringer, ikke nye promptnumre. PROMPT 027 mangler som nummerert oppføring.

PROMPT 027 forekommer i `docs/CHANGELOG_PROCESS.md` som branchnavnet `docs/027-documentation-completion` for ferdigstilling av PROMPT 024/025/026. Ingen undersøkt kilde bekrefter at en brukermelding med nummeret PROMPT 027 faktisk fantes. Derfor er 027 registrert som et uavklart nummereringshull, ikke som en rekonstruert prompt.

Etter kontrollen er det fortsatt 30 nummererte overskrifter og 27 unike historiske ID-er, fordi nummereringen og alle eksisterende oppføringer er bevart. I tillegg er to originaloppdrag fra denne samtalen lagt til som ordrette, unummererte kildefiler. Det ble ikke opprettet et nytt PROMPT-nummer.

## Prompter etter PROMPT 028

| Aktivitet | Kildebevis | Prompttekststatus | Resultat-/historikkstatus |
|---|---|---|---|
| PR #3-integrasjon og dokumentasjon i PDF-branchen | `docs/CODEX_PROMPT_LOG.md`, `docs/CHANGELOG_PROCESS.md`, Git-mergetreet | Original prompttekst ikke gjenfunnet – rekonstruert sammendrag. | Merge-SHA og lokale commits verifisert i Git; PR-hendelsene omtales som historiske dokumenterte fakta |
| MVP-001 PDF-implementering, review og integrasjon | `spec-mvp-001-pdf-ingestion.md`, testlogg, BMAD-status, commits `967d48a…` og `ef834cd…` | Original prompttekst ikke gjenfunnet – rekonstruert sammendrag. | Lokal commit, mergeforeldre og testlogger verifisert; PR #4-mergecommit er `f528b5179aef03e0fe0eec6f9cb7f7eb819281a9` |
| MVP Sprint 002 Gemini-implementering og valg | `spec-mvp-002-gemini-ai.md`, testlogg, BMAD-status og commit `875a8f5…` | Original prompttekst ikke gjenfunnet – rekonstruert sammendrag. | Lokal commit verifisert; ingen remote-branch/PR for Sprint 002 finnes blant lokale refs |
| Gemini Secrets, første manuelle feil, testisolering og exception-diagnostikk | Promptlogg, prosjektkontekst og testlogg | Original prompttekst ikke gjenfunnet – rekonstruert sammendrag. | Test- og kodehistorikk er dokumentert; lokal Secret ble kun kontrollert for filens eksistens/status i denne kontrollen |
| GEMINI-MODEL-feil og denne historikkontrollen | [Gemini-modelloppdraget](PROMPT_UNNUMBERED_GEMINI_MODEL_2026-11-15.md) og [historikkontrollen](PROMPT_UNNUMBERED_HISTORY_AUDIT_2026-11-15.md) | Originalpromptene er gjenfunnet ordrett i denne samtalen og arkivert som unummererte filer | Aktiv oppfølging; ferdigresultat, testbevis og BMAD-status føres når kontrollene er avsluttet |

Andre sporbare aktiviteter etter PROMPT 028 finnes i `docs/CODEX_PROMPT_LOG.md` under MVP SPRINT 002, MVP-001 og GIT INTEGRATION 002. Der de ikke peker til en arkivert originalprompt, skal de leses som dokumenterte sammendrag, ikke ordrette prompttranskripsjoner.

## PROMPT 001–028: kontrollresultat

- Alle 27 numre som faktisk har en overskrift, har en historisk promptseksjon. PROMPT 001–026 og PROMPT 028 er dekket; 027 mangler og er ikke oppfunnet.
- PROMPT 028 har egne ordrette originalkilder i `PROMPT_028_ANALYSIS.md` og `PROMPT_028_APPROVAL.md`, og promptloggen lenker til begge.
- Promptloggen inneholder originaltekst eller eksplisitt kilde-/gjenfinningstillegg for de eldre promptene. PROMPT 009s resultatstatus sier at identifiserbart fullstendig Codex-svar ikke ble gjenfunnet. PROMPT 019s tekst er bevisst personvernredigert, og dette er oppgitt.
- PROMPT 003 har to distinkte meldinger med samme nummer; PROMPT 023 og 028 har legitime oppfølgingsoppføringer med samme nummer. Nummereringen er ikke endret.
- Testresultater og Git-referanser varierer per oppføring; ikke alle historiske prompts har en egen commit eller PR. Dette er ikke i seg selv et hull dersom utfallet uttrykkelig sier «ingen commit/PR» eller peker til samtidige kilder.

## Verifiserte Git-milepæler

- PR #3 mergecommit `73fafcc0443019bf58ab69aaece503d17010c754` finnes lokalt. PR #4 mergecommit / Sprint 002-base `f528b5179aef03e0fe0eec6f9cb7f7eb819281a9` finnes lokalt.
- PDF-implementeringscommit `967d48abd1372beea239db7db576e0de2f5f7daf`, PDF-mergecommit `ef834cd2a49383940ed1739a6654feb8a4a9672c`, etterfølgende PDF-dokumentasjonscommit `78b6c26ed46a393cd1b383ea335a8f0b3788ecb0` og Sprint 002-commit `875a8f57205467d30b9b81f9a31084cc80b6bf5f` finnes som lokale Git-objekter.
- Sprint 002-committen er lokal på denne branchen. Ingen push eller PR ble utført eller bekreftet under denne kontrollen. PR-status er ikke live-kontrollert.
- Git-loggen bekrefter commits og mergecommit-objekter; den alene brukes ikke til å hevde en nyere GitHub PR-status.

## Gjenstående avgrensninger

1. PROMPT 027s eksistens og originaltekst er uavklart. Branchnavnet `docs/027-documentation-completion` viser ikke alene at prompten var nummerert 027.
2. Originalpromptene for de senere PDF-/Gemini-/integrasjonsaktivitetene er ikke gjenfunnet i prosjektfiler. Deres gjeldende sammendrag skal være merket «Original prompttekst ikke gjenfunnet – rekonstruert sammendrag.»
3. Codex-sessionlogger ble ikke undersøkt, fordi det ikke fantes et verktøy som kunne hente kun promptinnhold uten samtidig å lese eller vise potensielle hemmeligheter.
4. Det finnes ingen komplett, uavhengig kildeoversikt over alle brukerforespørsler før arkiveringen startet. Loggen kan derfor regnes som komplett for tilgjengelige og kontrollerte kilder, ikke som bevist fullstendig historikk.

## Gemini-modelloppdraget – undersøkelse så langt

- Adapteren leser modell fra `GEMINI_MODEL` i prosessmiljøet; når variabelen mangler, brukes standarden `gemini-2.5-flash`. `GEMINI_MODEL` var ikke satt i den aktuelle Codex-prosessen. Secrets-innhold er ikke undersøkt; modellvalget i koden bruker ikke Streamlit Secrets.
- SDK-en er Googles `google-genai` 1.75.0. Koden bruker Gemini Developer API via `genai.Client(...).models.generate_content(...)`, JSON MIME type og response schema. SDKs standard API-versjon med API-nøkkel er `v1beta`; dette er lokal signatur-/konfigurasjonskontroll, ikke serververifisering.
- Offisiell modellside oppgir `gemini-3.5-flash-lite` som stabil, med tekstutdata og støtte for structured outputs. Offisiell prisside viser Free Tier uten tokenkostnad. Dette er en aktuell dokumentasjonsanbefaling, men den bekrefter ikke tilgang for den konfigurerte nøkkelen.
- `GEMINI-MODEL` forblir observert feil, ikke bekreftet rotårsak. `models.list()` mot brukerens nøkkel er ikke utført. Brukerens eksplisitte godkjenning må innhentes før et slikt eksternt diagnostikkall. Ingen `generate_content`-kall ble gjort.
- Kilder: [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite), [Gemini API-priser](https://ai.google.dev/gemini-api/docs/pricing), [Gemini structured outputs](https://ai.google.dev/gemini-api/docs/structured-output), [Models API](https://ai.google.dev/api/models).

### Oppdatering etter godkjent dokumentasjonskontroll

`prototype/gemini_diagnostics` og mocktester er lagt til som oppfølging. Kommandoen krever `--list-models --confirm-external-call`; den ble ikke kjørt med godkjenningsflagget. Modellstandarden er uendret. PROMPT 027 og historikkforbeholdene over står uendret.

Etter brukerens godkjenning ble kommandoen kjørt én gang. Den returnerte blant annet `gemini-2.5-flash` og `gemini-3.5-flash-lite` med `generateContent`. Ingen nøkkel eller respons-body ble lagret. Se modelltilgangsresultatet i `docs/testing/TEST_LOG.md`; PROMPT 027 og alle historikkforbehold er uendret.


## Oppdatering etter sammenligning med originalmappen (2026-11-15)

Denne oppdateringen er append-only. Den tidligere kontrollteksten over er bevart; den beskrev kildetilstanden på kontrolltidspunktet. I denne oppfølgingen ble de angitte dokumentasjonsfilene i originalmappen lest skrivebeskyttet. Originalmappen er ikke endret. `.memlog.md`, Secrets og andre sensitive filer ble ikke åpnet.

### Nummererte og ordrette kilder

- Gemini-loggen inneholder fortsatthistorikken for PROMPT 001–026 og PROMPT 028: 27 unike nummererte ID-er. PROMPT 027 er ikke gjenfunnet og skal ikke opprettes uten kildebevis.
- For 26 av de 27 dokumenterte nummererte ID-ene finnes full original prompttekst i loggen eller tilknyttede originalkilder. PROMPT 019 er uttrykkelig personvernredigert og regnes ikke som fullstendig ordrett. PROMPT 009s manglende Codex-resultat er ikke et manglende originalprompt. PROMPT 028s to originalkilder er bevart i `PROMPT_028_ANALYSIS.md` og `PROMPT_028_APPROVAL.md`.
- Sammenligningen fant ingen unik ordrett prompttekst i originalmappen som ikke allerede var representert i Gemini-worktreens eldre promptarkiv. Originalens PROMPT 028-analyse har samme ordrette prompt som Gemini-filen, mens Gemini-filen har et senere verifiseringstillegg. Den eldre Sprint 002-seksjonen i originalens CODEX_PROMPT_LOG er en statusoppsummering, ikke en original brukerprompt.

### Senere, ordrett tilgjengelige beskjeder

I tillegg til de allerede arkiverte unummererte GEMINI-MODEL- og historikkontrollpromptene er åtte senere brukerbeskjeder fra samtalen bevart ordrett i [`PROMPT_UNNUMBERED_FOLLOWUPS_2026-11-15.md`](PROMPT_UNNUMBERED_FOLLOWUPS_2026-11-15.md). De gjelder status, godkjenninger, modellisting, lokal overstyring, quizantall, manuell sluttkontroll, PR-forberedelse og denne historikkontrollen. De er ikke gitt nye PROMPT-numre.

### Fortsatt manglende originalprompter

Fire grupper av senere historiske aktiviteter står fortsatt som rekonstruerte sammendrag fordi originaltekst ikke er funnet: PR #3/Git-integrasjonsarbeid; PDF Sprint 001 implementering/review/integrering; den opprinnelige Gemini-implementeringsinstruksen; og eldre Gemini Secrets-/API-nøkkel-, feilsøkings- og testisoleringsoppdrag. Gruppene kan inneholde flere opprinnelige meldinger, og kildene gir ikke et verifiserbart antall enkeltprompter. Ikke presenter sammendragene som ordrette. PROMPT 027 er et separat, uavklart nummereringshull.

### Kildebegrensning og status

Originalmappens dokumentasjon er kontrollert uten endringer. Ingen Codex-sessionlogg ble åpnet; derfor kan det finnes flere prompttekster utenfor repoet. Loggen er komplett for kildene som kunne trygt undersøkes, men ikke bevist fullstendig for alle historiske Codex-økter.


### Avkortet historikkmelding

Den første meldingen som innledet denne sammenligningen var synlig avkuttet etter ordet «GEMINI». Den separat mottatte fortsettelses-/godkjenningsmeldingen finnes ordrett i oppfølgingsarkivet. Manglende tekst fra den avkuttede meldingen er ikke gjenfunnet eller rekonstruert og telles ikke som en full originalprompt. Dette er et eget kildehull, adskilt fra det nummererte PROMPT 027-hullet og de fire eldre aktivitetsgruppene.


## Sluttrevisjon PROMPT 029 (2026-11-16)

PROMPT 029 er tildelt den komplette sluttrevisjonsforespørselen i denne Codex-økten. `PROMPT_029_FINAL_AUDIT.md` peker på originalmeldingen i samtalen, men inneholder ikke hele prompten ordrett. Arkivet markerer derfor ikke denne oppføringen som en full originaltranskripsjon. Denne oppgaven krever full ordrett lagring når teksten er tilgjengelig; dette gjenstår som et eksplisitt dokumentasjonsavvik og skal ikke forveksles med de eldre rekonstruerte sammendragene eller PROMPT 027-hullet.
