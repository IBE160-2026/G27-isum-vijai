# PROMPT 028 – Godkjenning av dokumentasjonsarbeid

Dette er den ordrette oppfølgingsinstruksen som godkjente dokumentasjonsutførelsen. Den opprinnelige analyseprompten for PROMPT 028 er ikke rekonstruert her; utførte krav og resultater er beskrevet i [_bmad-output/implementation-artifacts/prompt-028-product-brief-alignment.md](../../_bmad-output/implementation-artifacts/prompt-028-product-brief-alignment.md).

```text
Jeg godkjenner at vi går videre med dokumentasjonsdelen av PROMPT 028.

Bruk resultatene fra den gjennomførte analysen og BMAD Method v6.12.4.

Opprett en ny branch fra oppdatert main:

docs/028-product-brief-alignment

Før du oppretter branchen, bekreft at main er oppdatert, at arbeidsmappen er trygg, og at .memlog.md ikke påvirkes.

Oppgaver:

1. Opprett en avgrenset PROMPT 028-artefakt med kravmatrise, faktisk implementasjonsstatus og testbevis.
2. Kjør relevant BMAD Product Brief Validate/Update-prosess.
3. Bevar opprinnelige produktmål og suksesskriterier.
4. Dokumenter forskjeller mellom Product Brief, PRD og implementasjonen.
5. Oppdater relevante prosjektlogger, inkludert promptlogg, testlogg, testplan, prosjektkontekst og BMAD-status.
6. Kontroller også beslutningsloggen, changelog-prosessen, README og øvrige relevante artefakter. Endre dem bare dersom det finnes et dokumentert behov.
7. Registrer verifiserte merge-commits, main-SHA og faktiske testresultater.
8. Dokumenter manglende funksjonalitet og åpne beslutninger.
9. Behold PRD som draft dersom blokkerende valg fortsatt er åpne.
10. Foreslå nødvendige PRD-endringer, men ikke gjennomfør endringer som forutsetter nye gruppebeslutninger.

Viktige begrensninger:

* Ikke endre produktets opprinnelige mål.
* Ikke implementer nye funksjoner.
* Ikke endre applikasjonskode.
* Ikke finn på testresultater eller beslutninger.
* Ikke marker DEC-001–DEC-005 som vedtatt uten dokumentert godkjenning.
* Ikke slett historiske logger.
* Ikke rør .memlog.md.
* Ikke endre Git-identitet.
* Ikke commit, push, merge eller opprett PR.

Kjør relevante dokumentasjonstester og git diff --check etter endringene.

Avslutt med en rapport som viser alle endrede filer, testresultater, åpne beslutninger og eventuelle BMAD-valideringsfunn.

Stopp deretter og vent på godkjenning.
```
