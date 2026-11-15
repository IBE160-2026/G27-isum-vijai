import json
import sys
import types

import pytest

from prototype.gemini_service import GeminiServiceError, generate_gemini_result


class FakeModels:
    def __init__(self, text=None, error=None):
        self.text, self.error, self.calls = text, error, []

    def generate_content(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return type("Response", (), {"text": self.text})()


class FakeClient:
    def __init__(self, text=None, error=None):
        self.models = FakeModels(text, error)


def response(n=1, source_excerpt="notes"):
    return json.dumps({"summary": "Et sammendrag", "summary_evidence": ["notes"], "concepts": [{"term": "Energi", "explanation": "Evne til å utføre arbeid.", "term_excerpt": "notes", "explanation_excerpt": "notes"}], "questions": [{"question": "Hva kan lagres?", "options": ["A", "B", "C", "D"], "answer": "A", "explanation": "Notatene sier det.", "source_excerpt": source_excerpt, "answer_excerpt": "notes", "explanation_excerpt": "notes"} for _ in range(n)]})


def test_structured_result_and_settings_passed():
    client = FakeClient(response())
    result = generate_gemini_result("notes", client=client, question_count=3, length="lang", difficulty="vanskelig")
    assert result["insufficient_questions"] is True
    assert result["concepts"][0]["term"] == "Energi"
    assert client.models.calls[0]["model"] == "gemini-2.5-flash"
    assert "vanskelig" in client.models.calls[0]["contents"]


@pytest.mark.parametrize("body", ["not json", "{}", response(2)])
def test_invalid_responses_rejected(body):
    with pytest.raises(GeminiServiceError):
        generate_gemini_result("notes", client=FakeClient(body), question_count=1)


def test_duplicate_quiz_options_rejected():
    body = json.loads(response())
    body["questions"][0]["options"] = ["A", "A", "C", "D"]
    with pytest.raises(GeminiServiceError):
        generate_gemini_result("notes", client=FakeClient(json.dumps(body)))


def test_options_duplicate_after_case_and_whitespace_normalization_rejected():
    body = json.loads(response())
    body["questions"][0]["options"] = ["A", " a ", "C", "D"]
    with pytest.raises(GeminiServiceError):
        generate_gemini_result("notes", client=FakeClient(json.dumps(body)))


def test_missing_key_stops_before_call(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(GeminiServiceError, match="nøkkel"):
        generate_gemini_result("notes")


def test_streamlit_secrets_key_is_passed_explicitly(monkeypatch):
    import streamlit

    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setattr(streamlit, "secrets", {"GEMINI_API_KEY": "secrets-only-key"}, raising=False)
    captured = {}

    class KeyCapture:
        def __init__(self, *, api_key, http_options):
            captured["api_key"] = api_key
            captured["timeout"] = http_options.timeout

    genai_types = types.SimpleNamespace(
        HttpOptions=lambda **kwargs: types.SimpleNamespace(**kwargs)
    )
    genai = types.SimpleNamespace(Client=KeyCapture, types=genai_types)
    google = types.ModuleType("google")
    google.genai = genai
    monkeypatch.setitem(sys.modules, "google", google)
    monkeypatch.setitem(sys.modules, "google.genai", genai)
    models = FakeModels(response())
    monkeypatch.setattr(KeyCapture, "models", models, raising=False)
    generate_gemini_result("notes")
    assert captured["api_key"] == "secrets-only-key"
    assert captured["timeout"] == 30_000


def test_configured_model_override_reaches_sdk(monkeypatch):
    monkeypatch.setenv("GEMINI_MODEL", "gemini-custom-test")
    client = FakeClient(response())
    generate_gemini_result("notes", client=client)
    assert client.models.calls[0]["model"] == "gemini-custom-test"


def test_question_with_nonmatching_source_excerpt_is_rejected():
    with pytest.raises(GeminiServiceError, match="knyttes til notatene"):
        generate_gemini_result("notes. Notatene omtaler fotosyntese.", client=FakeClient(response(source_excerpt="energi kan lagres.")))


def test_question_accepts_case_or_whitespace_normalized_source_excerpt():
    result = generate_gemini_result(
        "  NOTES   are valid. More text.",
        client=FakeClient(response(source_excerpt="NoTeS are valid.")),
    )
    assert result["questions"]


def test_unsupported_summary_evidence_is_rejected():
    body = json.loads(response())
    body["summary_evidence"] = ["not in source"]
    with pytest.raises(GeminiServiceError):
        generate_gemini_result("notes", client=FakeClient(json.dumps(body)))


@pytest.mark.parametrize("field", ["answer_excerpt", "explanation_excerpt"])
def test_unsupported_answer_or_explanation_evidence_rejected(field):
    body = json.loads(response())
    body["questions"][0][field] = "unsupported quotation"
    with pytest.raises(GeminiServiceError, match="knyttes til notatene"):
        generate_gemini_result("notes", client=FakeClient(json.dumps(body)))


def test_unsupported_concept_evidence_rejected():
    body = json.loads(response())
    body["concepts"][0]["term_excerpt"] = "unsupported quotation"
    with pytest.raises(GeminiServiceError, match="begrep"):
        generate_gemini_result("notes", client=FakeClient(json.dumps(body)))


def test_unsupported_concept_explanation_evidence_rejected():
    body = json.loads(response())
    body["concepts"][0]["explanation_excerpt"] = "unsupported quotation"
    with pytest.raises(GeminiServiceError, match="begrep"):
        generate_gemini_result("notes", client=FakeClient(json.dumps(body)))


def test_provider_errors_are_sanitized():
    client = FakeClient(error=RuntimeError("private note and secret key"))
    with pytest.raises(GeminiServiceError) as err:
        generate_gemini_result("private note", client=client)
    assert "private" not in str(err.value)
    assert "secret" not in str(err.value)


@pytest.mark.parametrize(("error", "expected"), [
    (TimeoutError("provider details"), "for lang tid"),
    (RuntimeError("429 rate limit and private details"), "overbelastet"),
])
def test_timeout_and_rate_limit_have_safe_guidance(error, expected):
    with pytest.raises(GeminiServiceError, match=expected):
        generate_gemini_result("notes", client=FakeClient(error=error))
