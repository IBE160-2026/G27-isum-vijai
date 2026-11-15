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


def test_structured_result_and_settings_passed(monkeypatch):
    monkeypatch.delenv("GEMINI_MODEL", raising=False)
    client = FakeClient(response())
    result = generate_gemini_result("notes", client=client, question_count=3, length="lang", difficulty="vanskelig")
    assert result["insufficient_questions"] is True
    assert result["concepts"][0]["term"] == "Energi"
    assert client.models.calls[0]["model"] == "gemini-3.5-flash-lite"
    assert "vanskelig" in client.models.calls[0]["contents"]
    assert client.models.calls[0]["config"]["response_mime_type"] == "application/json"
    assert client.models.calls[0]["config"]["response_schema"]["required"] == ["summary", "summary_evidence", "concepts", "questions"]


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
    import prototype.gemini_service as service
    monkeypatch.setattr(service, "get_api_key", lambda: None)
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


def test_sdk_initialization_configuration_error_is_classified_safely(monkeypatch):
    from google import genai
    import prototype.gemini_service as service

    def reject_configuration(**kwargs):
        raise ValueError("private configuration")

    monkeypatch.setattr(genai, "Client", reject_configuration)
    with pytest.raises(GeminiServiceError, match="GEMINI-CONFIG") as caught:
        service.generate_gemini_result("notes", api_key="synthetic-key")
    assert "private" not in str(caught.value)


def test_streamlit_secrets_programming_error_is_not_misreported_as_missing_key(monkeypatch):
    import streamlit
    import prototype.gemini_service as service

    class BrokenSecrets:
        def get(self, key):
            raise RuntimeError("private secret backend detail")

    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setattr(streamlit, "secrets", BrokenSecrets(), raising=False)
    with pytest.raises(GeminiServiceError, match="GEMINI-SECRETS") as caught:
        service.generate_gemini_result("notes")
    assert "private" not in str(caught.value)


def test_configured_model_override_reaches_sdk(monkeypatch):
    monkeypatch.setenv("GEMINI_MODEL", "gemini-custom-test")
    client = FakeClient(response())
    generate_gemini_result("notes", client=client)
    assert client.models.calls[0]["model"] == "gemini-custom-test"


def test_explicit_model_argument_takes_precedence_over_environment(monkeypatch):
    monkeypatch.setenv("GEMINI_MODEL", "environment-model")
    client = FakeClient(response())
    generate_gemini_result("notes", client=client, model="argument-model")
    assert client.models.calls[0]["model"] == "argument-model"


def test_empty_quiz_is_rejected():
    body = json.loads(response())
    body["questions"] = []
    with pytest.raises(GeminiServiceError, match="ugyldig antall spørsmål"):
        generate_gemini_result("notes", client=FakeClient(json.dumps(body)))


def test_oversized_notes_are_rejected_before_provider_call(monkeypatch):
    import prototype.gemini_service as service

    client = FakeClient(response())
    monkeypatch.setattr("prototype.gemini_service.get_api_key", lambda: pytest.fail("key lookup should not occur"))
    monkeypatch.setattr(service, "MAX_EXTRACTED_CHARACTERS", 20)
    with pytest.raises(GeminiServiceError, match="20 tegn"):
        generate_gemini_result("x" * 21, client=client)
    assert client.models.calls == []


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
    (RuntimeError("429 rate limit and private details"), "GEMINI-UNKNOWN"),
])
def test_timeout_and_rate_limit_have_safe_guidance(error, expected):
    with pytest.raises(GeminiServiceError, match=expected):
        generate_gemini_result("notes", client=FakeClient(error=error))


@pytest.mark.parametrize(("status_code", "api_status", "expected"), [
    (401, "UNAUTHENTICATED", "GEMINI-AUTH"),
    (403, "PERMISSION_DENIED", "GEMINI-ACCESS"),
    (404, "NOT_FOUND", "GEMINI-MODEL"),
    (429, "RESOURCE_EXHAUSTED", "GEMINI-QUOTA"),
    (429, "OTHER", "GEMINI-RATE-LIMIT"),
    (400, "INVALID_ARGUMENT", "GEMINI-REQUEST"),
])
def test_google_genai_api_errors_are_classified_without_response_body(status_code, api_status, expected):
    from google.genai.errors import ClientError
    error = ClientError(status_code, {"status": api_status, "message": "private note and key detail"})
    with pytest.raises(GeminiServiceError, match=expected) as caught:
        generate_gemini_result("notes", client=FakeClient(error=error))
    assert "private" not in str(caught.value)
    assert "key detail" not in str(caught.value)


@pytest.mark.parametrize(("error", "expected"), [
    (ConnectionError("private host and credential detail"), "GEMINI-NETWORK"),
    (ValueError("private configuration detail"), "GEMINI-CONFIG"),
])
def test_provider_failure_categories_are_specific_and_sanitized(error, expected):
    with pytest.raises(GeminiServiceError, match=expected) as caught:
        generate_gemini_result("notes", client=FakeClient(error=error))
    assert "private" not in str(caught.value)
    assert "credential" not in str(caught.value)


def test_unknown_programming_error_gets_safe_unknown_code():
    with pytest.raises(GeminiServiceError, match="GEMINI-UNKNOWN") as caught:
        generate_gemini_result("notes", client=FakeClient(error=TypeError("private programming detail")))
    assert "private" not in str(caught.value)


@pytest.mark.parametrize("body", ["", "not json"])
def test_empty_or_malformed_provider_response_has_safe_specific_error(body):
    with pytest.raises(GeminiServiceError, match="ufullstendig|tomt"):
        generate_gemini_result("notes", client=FakeClient(body))


def test_missing_response_text_is_reported_as_incomplete():
    client = FakeClient()
    client.models.generate_content = lambda **kwargs: object()
    with pytest.raises(GeminiServiceError, match="tomt eller ufullstendig"):
        generate_gemini_result("notes", client=client)
