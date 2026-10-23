"""Fast demonstrasjonsinnhold. Innholdet er ikke avledet fra brukerens notater."""


def demo_result() -> dict:
    """Returner et nytt, fast eksempelresultat for UI-demonstrasjonen."""
    return {
        "is_demo": True,
        "summary": (
            "Et godt sammendrag trekker fram hovedpoengene i et tema og gjør dem "
            "lettere å repetere. Denne teksten er fast demonstrasjonsdata."
        ),
        "concepts": [
            "Hovedpoeng",
            "Repetisjon",
            "Selvtesting",
        ],
        "questions": [
            {
                "question": "Hva er et sammendrag ment å gjøre?",
                "options": [
                    "Gjengi alle detaljer ordrett",
                    "Trekke fram de viktigste poengene",
                    "Erstatte originalmaterialet helt",
                ],
                "answer": "Trekke fram de viktigste poengene",
                "explanation": "Et sammendrag løfter fram hovedinnholdet.",
            },
            {
                "question": "Hva kan en quiz hjelpe studenten med?",
                "options": [
                    "Teste egen forståelse",
                    "Endre forelesningsnotatene automatisk",
                    "Garantere et bestemt eksamensresultat",
                ],
                "answer": "Teste egen forståelse",
                "explanation": "Spørsmål kan brukes til aktiv selvtesting.",
            },
        ],
    }
