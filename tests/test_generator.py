"""Automatiske tester for input, mock-resultat og kontrollert feil."""

import re
import unittest

from prototype.generator import (
    InputValidationError,
    ResultGenerationError,
    generate_result,
)


class GeneratorTests(unittest.TestCase):
    def test_valid_text_returns_local_content_and_demo_quiz(self):
        notes = "Fotosyntese oppstår. Glukose dannes i planter. Glukose gir energi."
        result = generate_result(notes)

        self.assertIn("Glukose", result["summary"])
        self.assertIn("fotosyntese", result["concepts"])
        self.assertEqual(
            result["sources"],
            {
                "summary": "local",
                "concepts": "local",
                "questions": "demo",
            },
        )
        self.assertEqual(result["questions"], generate_result("Andre notater")["questions"])

    def test_summary_uses_up_to_three_source_sentences_ranked_by_content(self):
        notes = (
            "Og i det. Fotosyntese oppstår. Glukose dannes i planter. "
            "Glukose gir energi. Glukose er viktig."
        )

        summary = generate_result(notes)["summary"]

        self.assertEqual(
            summary,
            "Glukose dannes i planter. Glukose gir energi. Glukose er viktig.",
        )

    def test_concepts_are_frequent_source_words_with_stable_ties(self):
        notes = "Glukose driver fotosyntese. Fotosyntese lager glukose."

        concepts = generate_result(notes)["concepts"]

        self.assertEqual(concepts[:2], ["glukose", "fotosyntese"])
        source_words = {
            word.casefold() for word in re.findall(r"[^\W\d_]+", notes, re.UNICODE)
        }
        self.assertTrue(set(concepts).issubset(source_words))

    def test_repeating_a_word_inside_one_sentence_does_not_change_ranking(self):
        original = (
            "Glukose dannes i planter. Fotosyntese krever lysenergi. "
            "Lysenergi driver reaksjonen. Karbon lagres senere."
        )
        repeated = original.replace("Glukose dannes", "Glukose glukose glukose dannes")

        original_summary = generate_result(original)["summary"]
        repeated_summary = generate_result(repeated)["summary"]

        self.assertIn("Fotosyntese krever lysenergi.", original_summary)
        self.assertIn("Fotosyntese krever lysenergi.", repeated_summary)
        self.assertIn("Lysenergi driver reaksjonen.", original_summary)
        self.assertIn("Lysenergi driver reaksjonen.", repeated_summary)
        self.assertNotIn("Karbon lagres senere.", original_summary)
        self.assertNotIn("Karbon lagres senere.", repeated_summary)

    def test_common_filler_words_are_not_extracted_as_concepts(self):
        notes = (
            "Dette blir også viktig etter dette blir også klart. "
            "Planter vokser raskt. Energi flyttes gjennom planter."
        )

        concepts = generate_result(notes)["concepts"]

        self.assertTrue(set(concepts).isdisjoint({"dette", "blir", "også", "etter"}))

    def test_empty_text_is_rejected(self):
        with self.assertRaises(InputValidationError):
            generate_result("")

    def test_whitespace_only_text_is_rejected(self):
        with self.assertRaises(InputValidationError):
            generate_result(" \n\t  ")

    def test_non_string_text_is_rejected(self):
        with self.assertRaises(InputValidationError):
            generate_result(None)

    def test_mock_has_expected_question_structure(self):
        result = generate_result("Noen testnotater")

        for question in result["questions"]:
            self.assertTrue(question["question"].strip())
            self.assertIsInstance(question["options"], list)
            self.assertTrue(
                all(isinstance(option, str) and option.strip() for option in question["options"])
            )
            self.assertIn(question["answer"], question["options"])
            self.assertTrue(question["explanation"].strip())

    def test_malformed_mock_result_is_rejected(self):
        malformed_result = {
            "is_demo": True,
            "summary": "Demonstrasjon",
            "concepts": ["Begrep"],
            "questions": [
                {
                    "question": "Hva er dette?",
                    "options": ["Gyldig", 42],
                    "answer": "Gyldig",
                    "explanation": "Forklaring",
                }
            ],
        }

        with self.assertRaises(ResultGenerationError):
            generate_result("Gyldige notater", generator=lambda _notes: malformed_result)

    def test_unexpected_generator_error_is_wrapped(self):
        def broken_generator(_notes):
            raise RuntimeError("intern detalj som ikke skal vises")

        with self.assertRaises(ResultGenerationError) as error:
            generate_result("Gyldige notater", generator=broken_generator)

        self.assertEqual(str(error.exception), "Resultatet kunne ikke genereres.")


if __name__ == "__main__":
    unittest.main()
