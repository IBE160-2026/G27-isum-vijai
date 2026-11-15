# PROMPT 028 – Product Brief alignment og verifisering på main

**Dato:** 2026-10-26
**Arbeidsbranch:** `docs/028-product-brief-alignment`
**Base/testet main:** `16a34ed30aca147e1b79a0a98eb855bde1fa6a00`
**Formål:** Sammenholde Product Brief, PRD og faktisk prototype, og registrere etterprøvbare Git-, test- og prosessfunn. Ingen produktmål eller applikasjonskode endres.

## Git-status ved verifisering

- `origin` peker til `https://github.com/IBE160-2026/G27-isum-vijai.git`.
- PR #1 er merget til `main`; merge-commit `16a34ed30aca147e1b79a0a98eb855bde1fa6a00`.
- PR #2 er fortsatt `OPEN` ved kontrollen 2026-10-26. Den har ingen merge-commit-SHA. Dens dokumentasjonsendringer regnes derfor ikke som del av `main`.
- Lokal `main` var oppdatert og samsvarte med `origin/main` på angitt SHA før denne branchen ble opprettet.
- `.memlog.md` forble uendret og ustaget.

## BMAD Product Brief Validate – kildebaserte funn

Prosjektmanifestet bekrefter BMad Method Core/BMM v6.12.4. Product Brief-resolver og prosjektkonfigurasjon ble kjørt. Dette er en avgrenset, skrivebeskyttet validering; **Product Brief Validate er ikke fullført etter alle skillens kontrollkrav**, fordi brukerinstruksen forbyr å lese eller endre `.memlog.md`.

Gjeldende brief er [`product-brief.md`](../../product-brief.md), opprettet i commit `dc2a630`; git-loggen viser ingen senere endring. Den har ikke status-frontmatter. Briefens problem, målgruppe, visjon, løsning, suksesskriterier, v1-scope og utenfor-scope samsvarer i hovedsak med produktmålene oppgitt i PROMPT 028. Briefen skal fortsatt beskrive ønsket produkt, ikke nedjusteres til dagens prototype.

Valideringspunkter:

- AI er beskrevet som ønsket produktfunksjon, men ingen leverandør, databehandling eller nøkkel-/kostnadsmodell er valgt.
- Suksesskriteriene er relevante, men ikke fullt målbare ennå. Tidsbesparelse, kvalitet og kildebinding trenger godkjent testopplegg og terskler; ingen terskel er funnet på her.
- Briefen sier at studenten bør kunne gå tilbake til originalmaterialet. Den fastsetter ikke om dette betyr å beholde input synlig, side-ved-side-visning eller kildehenvisninger.
- Tekst/PDF, valg av sammendragslengde og quizinnstillinger er produktmål, ikke implementasjonsbevis.
- Product Brief er ikke endret. Ingen nye gruppebeslutninger er registrert.

## Product Brief–PRD alignment

PRD-en er [`prd.md`](../planning-artifacts/prds/prd-G27-isum-vijai-2026-10-23/prd.md), opprettet etter briefen i commit `6a247e2`. Den følger hovedmålene og dokumenterer FR-1–FR-8, NFR-1–NFR-7 og akseptansekriterier. Den står fortsatt `draft`, i tråd med uavklarte beslutninger.

Dokumenterte avklaringsbehov for en senere godkjent PRD-oppdatering:

1. Skill eksplisitt mellom AI-basert produktmål og foreløpig lokal prototypeteknikk. Provider-valget kan fortsatt stå åpent.
2. Avklar om tekstfilopplasting er et eget krav i tillegg til innliming; PRD FR-1 dekker innliming, mens briefen omtaler tekst/PDF-opplasting.
3. Gjør tilgang til originalmaterialet og brukerens mulighet til å kontrollere resultatet testbart uten å anta side-ved-side-visning eller sitater.
4. Konkretiser sammendragslengde, quizformat, vanskelighetsgrad og tillatt antall spørsmål før berørt implementasjon.
5. Avklar PDF/OCR, KI-dataflyt, oppbevaring/sletting og hvordan kvalitet/kildebinding skal måles med godkjente notater og fasit.

Punktene ovenfor er anbefalinger og åpne spørsmål, ikke vedtak. Ingen av dem er brukt til å endre PRD eller DEC-001–DEC-005.

## Krav-til-implementasjon-matrise

R-ID-ene er kartleggingsetiketter for PROMPT 028, ikke nye godkjente krav. Kilder: Product Brief-seksjonene «The Solution», «What Makes This Different», «Success Criteria» og «Scope»; PRD FR/NFR/AC som angitt.

| ID | Produktkrav og PRD-kilde | Status på main | Kode og eksisterende testbevis | Gap/avhengighet |
|---|---|---|---|---|
| R-01 | Lime inn notater; FR-1/AC-1 | Implementert | `app.py`; `test_generator.py`, `test_app.py` | Ingen vesentlig prototypegap for innliming. |
| R-02 | Laste opp tekstfiler; brief Scope IN, FR-1 dekker bare innliming | Ikke implementert | Ingen filopplasting eller slik test | Avklar om tekstfil er eget inputformat. |
| R-03 | Laste opp PDF; FR-2/AC-2 | Ikke implementert | Ingen PDF-komponent eller test | Avklar maskinlesbar PDF versus OCR før implementering. |
| R-04 | Sammendrag fra egne notater; FR-5/AC-4 | Delvis implementert | `generator.py` velger opptil tre kildesetninger; tester kontrollerer kildeinnhold og UI-visning | Lokal ekstraksjonsheuristikk, ikke AI-generering eller semantisk parafrase. Sammendragslengde kan ikke velges. |
| R-05 | Sentrale begreper fra notater; FR-5/AC-4 | Delvis implementert | `generator.py` frekvensteller kildeord; generator- og AppTest tester ordkilde/rangering | Enkel ordheuristikk, ikke semantisk begrepsuttrekk. |
| R-06 | Quiz fra notater; FR-6/NFR-1/AC-8 | Ikke implementert | Testen `test_valid_text_returns_local_content_and_demo_quiz` verifiserer at spørsmålene er like for ulik input | Fast demoquiz; notatbasert quiz er allerede registrert som utsatt i `deferred-work.md`. |
| R-07 | Fasit; FR-6/AC-4 | Delvis implementert | Demoresultat har svarnøkkel; generatorstrukturen og AppTest-feedback testes | Fasit gjelder bare demoquiz, ikke quiz generert fra notatene. |
| R-08 | Velge sammendragslengde; FR-3/AC-3 | Ikke implementert | Ingen UI-innstilling eller test | UX-valg og grenser må fastsettes. |
| R-09 | Velge quizvanskelighetsgrad; FR-4/AC-3 | Ikke implementert | Ingen UI-innstilling eller test | Definer nivåer og kvalitetskriterier før generering. |
| R-10 | Velge antall spørsmål; FR-4/AC-3/AC-5 | Ikke implementert | Ingen UI-innstilling eller test | Gruppen må fastsette gyldige grenser. |
| R-11 | Håndtere tom/ugyldig input; FR-8/AC-1/AC-7 | Delvis implementert | Tom, blank og ikke-tekstlig input testes; AppTest kontrollerer synlig tom-input-feil | Ingen dokumentopplasting finnes; ugyldige PDF-/tekstfiler kan derfor ikke testes. |
| R-12 | Full arbeidsflyt uten hjelp; FR-7/NFR-3/AC-6 | Delvis implementert | AppTest kontrollerer innsending, resultatvisning og quizbesvarelse | Ingen dokumentert brukertest; produktets fil-, innstillings- og kildebaserte quizflyt mangler. |
| R-13 | Skille demo fra generert innhold; PRD §1/FR-7 | Implementert for prototypen | UI viser lokal/ikke-KI-merking og merker quiz som demo; AppTest kontrollerer etiketter | Ikke et bevis på at produktkravene for AI-generering er oppfylt. |
| R-14 | Opplyse om mulige feil og støtte kontroll mot kilden; PRD NFR-2/FR-7 | Delvis implementert | UI forklarer lokal behandling og demoquiz | Mangler tydelig generell advarsel om at læringsinnhold kan være feil og konkret kontrollflyt mot originalen. |
| R-15 | Personvern/lagring; PRD NFR-4–NFR-7, DEC-002/003 | Delvis implementert / uavklart | Ingen ekstern KI eller varig lagring i prototypen | Produktets oppbevaring, sletting, KI-dataflyt og lagringsmodell er ikke vedtatt eller spesifisert. |

## Testbevis og begrensninger

Siste sluttkontroll etter dokumentasjonsendringene 2026-10-26 kl. 15:40 CET brukte `./.venv/bin/python -m pytest -q && git diff --check` på app-/testkoden fra `16a34ed30aca147e1b79a0a98eb855bde1fa6a00`: 15 bestått, 0 feilet, ingen pytest-warnings; `git diff --check` exit 0. Detaljer og separat AppTest-/dokumentasjonstest står i [`TEST_LOG.md`](../../docs/testing/TEST_LOG.md). Ingen applikasjonskode er endret i PROMPT 028.

Automatisk pytest dekker 11 generator- og 4 Streamlit AppTest-scenarioer. De er prototypetester og gjør ikke T-001–T-009 fullført. AppTest med to ulike notatsett viste at sammendrag og ordliste endres med input; eksisterende test viser at demoquizens spørsmål ikke gjør det. Nettleserbasert manuell test ble ikke gjennomført.

## Beslutninger og anbefalt videre arbeid

DEC-001–DEC-005 er fortsatt **Uavklart**. PRD §9 har i tillegg åpne spørsmål om quizformat/-grenser, målbar kildebinding og OCR. Ingen teknologivalg, AI-provider, lagring eller testmodus er vedtatt her.

Foreslått neste BMAD-rekkefølge:

1. Avklar PR #2-status og innarbeid først dokumentasjon som faktisk merget.
2. Fullfør Product Brief Validate når tillatt sporgrunnlag er tilgjengelig; oppdater brief bare ved godkjente produktendringer.
3. Kjør `bmad-prd` Update etter godkjent brief-/beslutningsavklaring; la status være `draft` til blokkerende valg er lukket.
4. Bruk `bmad-create-epics-and-stories` for avhengighetene. Quiz fra notater er allerede registrert som utsatt arbeid og skal ikke dupliseres som et nytt urelatert initiativ.
5. Deretter prioriter tekst-/PDF-input, generering og innstillinger i små stories med godkjente testnotater, før produktmessig ende-til-ende-validering.

## Status for arbeidsflyten

Dette artefaktet dokumenterer gjennomført, avgrenset Product Brief-validering og implementasjonskartlegging. Full BMM Product Brief Validate er begrenset av forbudet mot å lese `.memlog.md`; `.memlog.md` er ikke lest eller endret. PRD-en er ikke redigert, og ingen PRD Validate-rapport er laget. Dette er ikke en fullført produktutviklings- eller PRD-finaliseringsworkflow.

## Post-merge-status – PR #2 integrert (2026-11-15)

- **Verifisert merge:** `origin/main` SHA `1227fb443e52815f831b3f5720b4f41844f72ad0` er mergecommitten for PR #2, med foreldre `35ff46c422948330844f77ff07816ca86c815fc1` og PR #2-head `a5778f25991d9b88fa4c3c186d5b2d2536c36212`. Commit-tiden er `2026-11-14 21:49:15 +01:00`; GitHub API-ens PR-felt `merged_at` kunne ikke hentes fra Codex-miljøet. PROMPT 028s historiske kildecommit `72c0b67d2ac715f925d6b41a56a4636c97b4b83a` er beholdt som referanse.
- **Verifisert baseline:** Integrasjonsbranchen `docs/028-product-brief-alignment-post-pr2` er basert på oppdatert `origin/main` SHA `1227fb443e52815f831b3f5720b4f41844f72ad0`.
- **Dokumentasjon:** PR #2s eksisterende logg- og testhistorikk er bevart; unike PROMPT 028-oppføringer er lagt etter den. Denne posten er gjeldende status og overstyrer ikke tidsbundne historiske rapporter.
- **Verifisering på integrasjonsbranchen:** `python -m pytest -q` ga `18 passed`; `python -m pytest -q tests/test_prompt024_traceability_docs.py` ga `3 passed`; `git diff --check` bestod.
- **Produkt- og arbeidsstatus:** Ingen applikasjonskode, Product Brief, PRD eller beslutning er endret. PRD forblir `draft`, DEC-001–DEC-005 forblir uavklart. Ingen commit, push, merge, rebase eller PR er opprettet. `.memlog.md` er ikke åpnet.

## Publisering i PR #3 (2026-11-15)

- PROMPT 028-integreringen ble kvalitetskontrollert, committet som `ec19c95a63e169ab90174abb2299bbdaba1ed357` og pushet til `docs/028-product-brief-alignment-post-pr2`.
- Arbeidet er publisert i eksisterende [PR #3](https://github.com/IBE160-2026/G27-isum-vijai/pull/3). Ved siste kontroll 2026-11-15 kl. 10:09:30 UTC var PR-en `OPEN`, `MERGEABLE`, base `main`, head `ec19c95…`; ingen CI-checks var rapportert. PR #3 avventer gjennomgang og er ikke merget.
- Product Brief Validate er ikke fullført, PRD forblir `draft`, og DEC-001–DEC-005 forblir åpne.

## Senere status – PR #3 merge (2026-11-15)

Brukeren bekreftet at PR #3 ble merget 2026-11-15T12:08:00Z med merge-SHA `73fafcc0443019bf58ab69aaece503d17010c754`. Dette erstatter ikke den tidsbundne publiseringskontrollen ovenfor, der PR #3 ennå var `OPEN`/`MERGEABLE`. PRD forblir `draft`; Product Brief Validate er ikke fullført; DEC-001–DEC-005 forblir åpne.
