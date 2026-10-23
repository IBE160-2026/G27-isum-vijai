"""Automatiske tester for input, mock-resultat og kontrollert feil."""

import unittest

from prototype.generator import (
    InputValidationError,
    ResultGenerationError,
    generate_result,
)


class GeneratorTests(unittest.TestCase):
    def test_valid_text_returns_demo_result(self):
        result = generate_result("  Notater om forelesningen.  ")

        self.assertTrue(result["is_demo"])
        self.assertTrue(result["summary"])
        self.assertTrue(result["concepts"])
        self.assertTrue(result["questions"])

    def test_empty_text_is_rejected(self):
        with self.assertRaises(InputValidationError):
            generate_result("")

    def test_whitespace_only_text_is_rejected(self):
        with self.assertRaises(InputValidationError):
            generate_result(" \n\t  ")

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
