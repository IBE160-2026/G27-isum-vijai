"""UI-regresjonstester for resultatkilder og ugyldig input."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def _submit_notes(notes: str):
    app = AppTest.from_file(str(APP_PATH)).run()
    app.text_area[0].set_value(notes)
    app.button[0].click()
    return app.run()


def test_results_show_local_sources_and_demo_quiz_label():
    notes = "Fotosyntese oppstår. Glukose dannes i planter. Glukose gir energi."
    source_sentences = [
        "Fotosyntese oppstår.",
        "Glukose dannes i planter.",
        "Glukose gir energi.",
    ]
    app = _submit_notes(notes)

    assert not app.exception
    displayed_summary = next(
        item.value for item in app.markdown if item.value == " ".join(source_sentences)
    )
    assert displayed_summary == " ".join(source_sentences)
    assert any("LOKAL TEKSTBEHANDLING · IKKE KI" in item.value for item in app.caption)
    assert any("Quiz · demonstrasjonsdata" in item.value for item in app.header)
    assert any("ikke laget fra notatene" in item.value for item in app.caption)
    assert app.radio[0].value == "Tekst"
    assert len(app.radio) == 3


def test_quiz_submission_shows_score_and_feedback_for_each_answer():
    app = _submit_notes("Fotosyntese oppstår. Glukose dannes i planter. Glukose gir energi.")
    app.radio[1].set_value("Trekke fram de viktigste poengene")
    app.radio[2].set_value("Endre forelesningsnotatene automatisk")
    app.button[1].click()
    app.run()

    assert not app.exception
    assert any("Resultat: 1 av 2 riktige" in item.value for item in app.subheader)
    assert any("Spørsmål 1: Riktig." in item.value for item in app.success)
    assert any("Spørsmål 2: Fasit: Teste egen forståelse." in item.value for item in app.info)


def test_empty_concepts_have_a_clear_ui_message():
    app = _submit_notes("og i det.")

    assert not app.exception
    assert any("Fant ingen tydelige begreper" in item.value for item in app.info)


def test_empty_input_shows_validation_error_in_ui():
    app = AppTest.from_file(str(APP_PATH)).run()
    app.button[0].click()
    app.run()

    assert any("Skriv inn forelesningsnotater" in item.value for item in app.error)


def test_pdf_upload_uses_extracted_text_in_existing_summary(make_text_pdf):
    notes = ["Photosynthesis stores energy.", "Chlorophyll absorbs light."]
    expected_summary = " ".join(notes)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.text_area[0].set_value(
        "Stale text input. This content must not be combined with the PDF."
    )
    app.button[0].click()
    app.run()
    app.radio[0].set_value("PDF").run()
    app.file_uploader[0].set_value(
        ("lecture-notes.pdf", make_text_pdf(notes), "application/pdf")
    )
    app.button[0].click()
    app.run()

    assert not app.exception
    assert any(
        item.value == expected_summary
        for item in app.markdown
    )
    assert not any("Stale text input" in item.value for item in app.markdown)
    assert any("behandles lokalt i minnet" in item.value for item in app.caption)
    assert not any("Skriv inn forelesningsnotater" in item.value for item in app.error)


def test_switching_input_mode_clears_previous_result():
    app = _submit_notes("Existing text result. More notes here.")
    assert any("Existing text result." in item.value for item in app.markdown)

    app.radio[0].set_value("PDF").run()

    assert not any("Existing text result." in item.value for item in app.markdown)


def test_pdf_mode_without_file_shows_clear_error():
    app = AppTest.from_file(str(APP_PATH)).run()
    app.radio[0].set_value("PDF").run()
    app.button[0].click()
    app.run()

    assert not app.exception
    assert any("Velg en PDF-fil" in item.value for item in app.error)


def test_invalid_uploaded_pdf_shows_safe_error():
    app = AppTest.from_file(str(APP_PATH)).run()
    app.radio[0].set_value("PDF").run()
    app.file_uploader[0].set_value(("corrupt.pdf", b"not a PDF", "application/pdf"))
    app.button[0].click()
    app.run()

    assert not app.exception
    assert any("PDF-filen kunne ikke leses" in item.value for item in app.error)
    assert not any("PdfReadError" in item.value for item in app.error)


def test_textless_uploaded_pdf_shows_ocr_scope_error(blank_pdf_bytes):
    app = AppTest.from_file(str(APP_PATH)).run()
    app.radio[0].set_value("PDF").run()
    app.file_uploader[0].set_value(
        ("scanned-notes.pdf", blank_pdf_bytes, "application/pdf")
    )
    app.button[0].click()
    app.run()

    assert not app.exception
    assert any("Fant ingen uttrekkbar tekst" in item.value for item in app.error)
    assert any("OCR støttes ikke" in item.value for item in app.error)
