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
    assert len(app.radio) == 2


def test_quiz_submission_shows_score_and_feedback_for_each_answer():
    app = _submit_notes("Fotosyntese oppstår. Glukose dannes i planter. Glukose gir energi.")
    app.radio[0].set_value("Trekke fram de viktigste poengene")
    app.radio[1].set_value("Endre forelesningsnotatene automatisk")
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
