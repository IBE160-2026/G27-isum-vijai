"""Inputvalidering og lokal, deterministisk mock for prototypen."""

from collections.abc import Callable

from prototype.mock_data import demo_result


class InputValidationError(ValueError):
    """Input mangler eller inneholder bare blanktegn."""


class ResultGenerationError(RuntimeError):
    """Resultatet kunne ikke bygges eller hadde ugyldig struktur."""


def _validate_result(result: object) -> dict:
    if not isinstance(result, dict):
        raise ResultGenerationError("Mocken returnerte ikke et resultat.")

    if result.get("is_demo") is not True:
        raise ResultGenerationError("Resultatet mangler demomerkingen.")
    if not isinstance(result.get("summary"), str) or not result["summary"].strip():
        raise ResultGenerationError("Resultatet mangler et sammendrag.")
    if not isinstance(result.get("concepts"), list) or not all(
        isinstance(item, str) and item.strip() for item in result["concepts"]
    ):
        raise ResultGenerationError("Begrepslisten har ugyldig struktur.")

    questions = result.get("questions")
    if not isinstance(questions, list) or not questions:
        raise ResultGenerationError("Resultatet mangler quizspørsmål.")
    for question in questions:
        if not isinstance(question, dict):
            raise ResultGenerationError("Et quizspørsmål har ugyldig struktur.")
        options = question.get("options")
        if (
            not isinstance(question.get("question"), str)
            or not question["question"].strip()
            or not isinstance(options, list)
            or not options
            or not all(isinstance(option, str) and option.strip() for option in options)
            or question.get("answer") not in options
            or not isinstance(question.get("explanation"), str)
            or not question["explanation"].strip()
        ):
            raise ResultGenerationError("Et quizspørsmål mangler nødvendige felt.")
    return result


def generate_result(
    notes: str,
    generator: Callable[[str], dict] | None = None,
) -> dict:
    """Valider tekst og bygg et demonstrasjonsresultat med valgt mock."""
    if not isinstance(notes, str) or not notes.strip():
        raise InputValidationError("Skriv inn forelesningsnotater før du genererer.")

    selected_generator = generator or (lambda _notes: demo_result())
    try:
        result = selected_generator(notes.strip())
        return _validate_result(result)
    except ResultGenerationError:
        raise
    except Exception as exc:
        raise ResultGenerationError("Resultatet kunne ikke genereres.") from exc
