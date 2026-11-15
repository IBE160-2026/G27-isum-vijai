"""UI-regresjonstester for resultatkilder og ugyldig input."""

from pathlib import Path

import pytest
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


def test_editing_notes_clears_previous_result_immediately():
    app = _submit_notes("Existing text result. More notes here.")
    assert any("Existing text result." in item.value for item in app.markdown)

    app.text_area[0].set_value("Updated source notes. Different content.").run()

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


def test_gemini_requires_active_consent():
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater om energi.").run()
    app.button[0].click()
    app.run()
    assert any("Bekreft personverninformasjonen" in item.value for item in app.error)


def test_gemini_mode_without_key_shows_safe_guidance(monkeypatch):
    from prototype import gemini_service
    monkeypatch.setattr(gemini_service, "get_api_key", lambda: None)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater om energi.").run()
    app.checkbox[0].check()
    app.button[0].click()
    app.run()
    assert any("API-nøkkel mangler" in item.value for item in app.error)


def test_gemini_controls_match_mvp_002_defaults_and_bounds():
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()

    assert app.selectbox[1].options == ["kort", "middels", "lang"]
    assert app.selectbox[1].value == "middels"
    assert app.selectbox[2].options == ["lett", "middels", "vanskelig"]
    assert app.selectbox[2].value == "middels"
    assert app.slider[0].min == 1
    assert app.slider[0].max == 10
    assert app.slider[0].value == 5


def test_gemini_pdf_upload_alone_does_not_start_generation(make_text_pdf):
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.radio[0].set_value("PDF").run()
    app.file_uploader[0].set_value(
        ("synthetic-notes.pdf", make_text_pdf(["Syntetiske forelesningsnotater om energi."]), "application/pdf")
    ).run()
    assert not app.exception
    assert not app.error
    assert not any(item.value == "Syntetiske forelesningsnotater om energi." for item in app.markdown)


def test_switching_generation_mode_clears_prior_result():
    app = _submit_notes("Prior local result. More text for concepts.")
    assert any("Prior local result." in item.value for item in app.markdown)
    app.selectbox[0].set_value("Gemini AI").run()
    assert not any("Prior local result." in item.value for item in app.markdown)


def test_gemini_answers_are_hidden_until_quiz_submission(monkeypatch):
    import prototype.gemini_service as service

    result = {
        "summary": "Kort sammendrag", "concepts": [], "insufficient_questions": False,
        "questions": [{"question": "Spørsmål?", "options": ["A", "B", "C", "D"], "answer": "A", "explanation": "Fordi notatene sier det."}],
    }
    monkeypatch.setattr(service, "generate_gemini_result", lambda *args, **kwargs: result)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater.").run()
    app.checkbox[0].check()
    app.button[0].click().run()
    assert not any("Fasit" in item.value or "Fordi notatene" in item.value for item in app.markdown)
    app.button[-1].click().run()
    assert any("Fasit: A" in item.value and "Fordi notatene" in item.value for item in app.info)


def test_gemini_result_renders_note_based_quiz_without_demo_label(monkeypatch):
    from prototype import gemini_service

    calls = []

    def fake_generate(notes, **settings):
        calls.append((notes, settings))
        return {
            "summary": "Energi kan utføre arbeid.",
            "concepts": [{"term": "Energi", "explanation": "Evne til å utføre arbeid."}],
            "questions": [{"question": "Hva kan energi gjøre?", "options": ["A", "B", "C", "D"], "answer": "A", "explanation": "Dette står i notatene."}],
            "insufficient_questions": True,
        }

    monkeypatch.setattr(gemini_service, "generate_gemini_result", fake_generate)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater om energi.").run()
    app.checkbox[0].check()
    app.button[0].click()
    app.run()

    assert calls and calls[0][0] == "Syntetiske notater om energi."
    assert any("Hva kan energi gjøre?" in item.value for item in app.markdown)
    assert any("Notatene ga grunnlag for 1 av 5" in item.value for item in app.info)
    assert not any("Fasit: A" in item.value or "Dette står i notatene." in item.value for item in app.markdown)
    assert not any("faste quizspørsmålene" in item.value for item in app.caption)

    app.selectbox[0].set_value("Lokal").run()
    assert not any("Energi kan utføre arbeid." == item.value for item in app.markdown)


def test_gemini_pdf_sends_only_locally_extracted_text_after_consent(monkeypatch, make_text_pdf):
    from prototype import gemini_service

    calls = []

    def fake_generate(notes, **settings):
        calls.append((notes, settings))
        return {
            "summary": "Energi kan utføre arbeid.",
            "concepts": [],
            "questions": [],
            "insufficient_questions": True,
        }

    monkeypatch.setattr(gemini_service, "generate_gemini_result", fake_generate)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.radio[0].set_value("PDF").run()
    app.file_uploader[0].set_value(
        ("synthetic-notes.pdf", make_text_pdf(["Syntetiske notater om energi."]), "application/pdf")
    ).run()
    assert not calls
    app.checkbox[0].check()
    app.button[0].click()
    app.run()

    assert len(calls) == 1, [item.value for item in app.error]
    assert "Syntetiske notater om energi." in calls[0][0]


def _install_fake_gemini(monkeypatch):
    from prototype import gemini_service

    calls = []

    def fake_generate(notes, **settings):
        calls.append((notes, settings))
        return {
            "summary": "Syntetisk AI-sammendrag",
            "concepts": [],
            "questions": [{
                "question": "Syntetisk spørsmål?",
                "options": ["A", "B", "C", "D"],
                "answer": "A",
                "explanation": "Syntetisk forklaring.",
            }],
            "insufficient_questions": False,
        }

    monkeypatch.setattr(gemini_service, "generate_gemini_result", fake_generate)
    return calls


def test_changing_notes_revokes_consent_and_prevents_repeat_call(monkeypatch):
    calls = _install_fake_gemini(monkeypatch)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Original syntetiske notater.").run()
    app.checkbox[0].check()
    app.button[0].click().run()
    assert len(calls) == 1
    assert any("Syntetisk AI-sammendrag" == item.value for item in app.markdown)
    app.session_state["answer_0"] = "B"
    assert app.session_state.get("answer_0") == "B"
    app.run()

    app.text_area[0].set_value("Endrede syntetiske notater.").run()
    assert not app.checkbox[0].value
    assert "answer_0" not in app.session_state
    assert not any("Syntetisk AI-sammendrag" == item.value for item in app.markdown)
    app.button[0].click().run()

    assert len(calls) == 1
    assert any("Bekreft personverninformasjonen" in item.value for item in app.error)


def test_changing_uploaded_pdf_revokes_consent(monkeypatch, make_text_pdf):
    calls = _install_fake_gemini(monkeypatch)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.radio[0].set_value("PDF").run()
    first_pdf = make_text_pdf(["Første syntetiske PDF-notat."])
    second_pdf = make_text_pdf(["Andre syntetiske PDF-notat."])
    app.file_uploader[0].set_value(("first.pdf", first_pdf, "application/pdf")).run()
    app.checkbox[0].check()
    app.button[0].click().run()
    assert len(calls) == 1
    assert app.session_state.get("prototype_result")
    app.session_state["answer_0"] = "B"
    assert app.session_state.get("answer_0") == "B"
    app.run()
    app.button[-1].click().run()
    assert app.session_state.get("quiz_feedback")

    app.file_uploader[0].set_value(("second.pdf", second_pdf, "application/pdf")).run()
    assert not app.checkbox[0].value
    assert not app.session_state.get("prototype_result")
    assert not app.session_state.get("quiz_feedback")
    assert "answer_0" not in app.session_state
    assert not any("Syntetisk AI-sammendrag" == item.value for item in app.markdown)
    app.button[0].click().run()

    assert len(calls) == 1
    assert any("Bekreft personverninformasjonen" in item.value for item in app.error)


def test_switching_generation_mode_requires_new_consent(monkeypatch):
    calls = _install_fake_gemini(monkeypatch)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater for modusskifte.").run()
    app.checkbox[0].check()
    app.button[0].click().run()
    assert len(calls) == 1

    app.selectbox[0].set_value("Lokal").run()
    app.selectbox[0].set_value("Gemini AI").run()
    assert not app.checkbox[0].value
    assert not app.session_state.get("prototype_result")
    app.button[0].click().run()

    assert len(calls) == 1
    assert any("Bekreft personverninformasjonen" in item.value for item in app.error)


@pytest.mark.parametrize(("initial_format", "next_format"), [("Tekst", "PDF"), ("PDF", "Tekst")])
def test_switching_note_format_requires_new_consent(monkeypatch, make_text_pdf, initial_format, next_format):
    calls = _install_fake_gemini(monkeypatch)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    if initial_format == "PDF":
        app.radio[0].set_value("PDF").run()
        app.file_uploader[0].set_value(
            ("initial.pdf", make_text_pdf(["Syntetiske startnotater fra PDF."]), "application/pdf")
        ).run()
    else:
        app.text_area[0].set_value("Syntetiske startnotater fra tekst.").run()
    app.checkbox[0].check()
    app.button[0].click().run()
    assert len(calls) == 1

    app.radio[0].set_value(next_format).run()
    if next_format == "PDF":
        app.file_uploader[0].set_value(
            ("next.pdf", make_text_pdf(["Syntetiske nye PDF-notater."]), "application/pdf")
        ).run()
    else:
        app.text_area[0].set_value("Syntetiske nye tekstnotater.").run()
    assert not app.checkbox[0].value
    assert not app.session_state.get("prototype_result")
    app.button[0].click().run()

    assert len(calls) == 1
    assert any("Bekreft personverninformasjonen" in item.value for item in app.error)


@pytest.mark.parametrize(("control", "value"), [
    ("length", "lang"),
    ("difficulty", "vanskelig"),
    ("count", 6),
])
def test_changing_gemini_setting_clears_result_and_quiz_feedback(monkeypatch, control, value):
    _install_fake_gemini(monkeypatch)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater om innstillinger.").run()
    app.checkbox[0].check()
    app.button[0].click().run()
    app.session_state["answer_0"] = "B"
    assert app.session_state.get("answer_0") == "B"
    app.button[-1].click().run()
    assert any("Resultat: 0 av 1 riktige" in item.value for item in app.subheader)
    assert app.session_state.get("prototype_result")
    assert app.session_state.get("quiz_feedback")

    if control == "length":
        app.selectbox[1].set_value(value).run()
    elif control == "difficulty":
        app.selectbox[2].set_value(value).run()
    else:
        app.slider[0].set_value(value).run()

    assert not any("Syntetisk AI-sammendrag" == item.value for item in app.markdown)
    assert not any(item.value.startswith("Resultat:") for item in app.subheader)
    assert not app.session_state.get("prototype_result")
    assert not app.session_state.get("quiz_feedback")
    assert "answer_0" not in app.session_state


def test_regenerating_clears_previous_quiz_answers_and_feedback(monkeypatch):
    calls = _install_fake_gemini(monkeypatch)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater for regenerering.").run()
    app.checkbox[0].check()
    app.button[0].click().run()
    assert len(calls) == 1

    app.session_state["answer_0"] = "B"
    app.button[-1].click().run()
    assert app.session_state.get("quiz_feedback")
    assert app.session_state.get("answer_0") == "B"

    app.button[0].click().run()

    assert len(calls) == 2
    assert "quiz_feedback" not in app.session_state
    assert app.session_state.get("answer_0") == "A"
    assert app.session_state.get("prototype_result")


def test_empty_gemini_quiz_result_is_not_rendered_as_zero_of_zero(monkeypatch):
    from prototype import gemini_service

    monkeypatch.setattr(gemini_service, "generate_gemini_result", lambda *args, **kwargs: {
        "summary": "Syntetisk sammendrag", "concepts": [], "questions": [],
        "insufficient_questions": True,
    })
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("Syntetiske notater.").run()
    app.checkbox[0].check()
    app.button[0].click().run()

    assert not app.exception
    assert any("returnerte ingen quizspørsmål" in item.value for item in app.error)
    assert not any("0 av 0" in item.value for item in app.subheader)
    assert not any(item.value == "Quiz" for item in app.header)
    assert not any(item.value == "Sammendrag" for item in app.header)
    assert "prototype_result" not in app.session_state
    assert "quiz_feedback" not in app.session_state


def test_oversized_gemini_notes_show_boundary_error_without_provider_call(monkeypatch):
    import prototype.gemini_service as service

    monkeypatch.setattr(service, "MAX_EXTRACTED_CHARACTERS", 20)
    app = AppTest.from_file(str(APP_PATH)).run()
    app.selectbox[0].set_value("Gemini AI").run()
    app.text_area[0].set_value("x" * 21).run()
    app.checkbox[0].check()
    app.button[0].click().run()

    assert any("overskrider grensen på 20 tegn" in item.value for item in app.error)
