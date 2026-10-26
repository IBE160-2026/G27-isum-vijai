"""Inputvalidering og lokal, deterministisk mock for prototypen."""

import re
from collections import Counter
from collections.abc import Callable

from prototype.mock_data import demo_result


class InputValidationError(ValueError):
    """Input mangler eller inneholder bare blanktegn."""


class ResultGenerationError(RuntimeError):
    """Resultatet kunne ikke bygges eller hadde ugyldig struktur."""


_WORD_PATTERN = re.compile(r"[^\W\d_]+", re.UNICODE)
_SENTENCE_PATTERN = re.compile(r"(?<=[.!?])\s+|\n+")
_STOP_WORDS = {
    "at", "av", "ble", "da", "de", "deg", "dem", "den", "denne", "der",
    "det", "dette", "disse", "du", "en", "et", "etter", "for", "fra",
    "har", "hun", "i", "ikke", "jeg", "kan", "man", "med", "men", "mot",
    "når", "og", "også", "om", "opp", "oss", "over", "på", "seg", "slik",
    "som", "til", "under", "ut", "var", "ved", "vi", "vil", "blir", "å",
}


def _content_words(text: str) -> list[str]:
    return [
        word.casefold()
        for word in _WORD_PATTERN.findall(text)
        if len(word) >= 4 and word.casefold() not in _STOP_WORDS
    ]


def _local_summary(notes: str) -> str:
    """Velg opptil tre innholdsmettede originalsetninger uten å omskrive dem."""
    sentences = [
        sentence.strip()
        for sentence in _SENTENCE_PATTERN.split(notes.strip())
        if sentence.strip()
    ]
    if len(sentences) <= 3:
        return " ".join(sentences)

    sentence_words = [_content_words(sentence) for sentence in sentences]
    frequencies = Counter(
        word for words in sentence_words for word in set(words)
    )
    scored = []
    for index, (sentence, words) in enumerate(zip(sentences, sentence_words)):
        distinct_words = set(words)
        score = (
            sum(frequencies[word] for word in distinct_words) / len(distinct_words)
            if distinct_words
            else 0
        )
        scored.append((score, index, sentence))

    selected = sorted(scored, key=lambda item: (-item[0], item[1]))[:3]
    return " ".join(sentence for _, _, sentence in sorted(selected, key=lambda item: item[1]))


def _local_concepts(notes: str, limit: int = 5) -> list[str]:
    """Return frequent source words, preserving first-seen order for ties."""
    words = _content_words(notes)
    counts = Counter(words)
    first_seen = {}
    for index, word in enumerate(words):
        first_seen.setdefault(word, index)
    return sorted(counts, key=lambda word: (-counts[word], first_seen[word]))[:limit]


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
    """Bygg lokalt sammendrag/begreper og legg til fast demonstrasjonsquiz."""
    if not isinstance(notes, str) or not notes.strip():
        raise InputValidationError("Skriv inn forelesningsnotater før du genererer.")

    selected_generator = generator or (lambda _notes: demo_result())
    try:
        demo = _validate_result(selected_generator(notes.strip()))
        return {
            "summary": _local_summary(notes.strip()),
            "concepts": _local_concepts(notes.strip()),
            "questions": demo["questions"],
            "sources": {
                "summary": "local",
                "concepts": "local",
                "questions": "demo",
            },
        }
    except ResultGenerationError:
        raise
    except Exception as exc:
        raise ResultGenerationError("Resultatet kunne ikke genereres.") from exc
