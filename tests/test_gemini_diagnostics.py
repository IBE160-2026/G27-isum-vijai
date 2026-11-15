from types import SimpleNamespace

import pytest

from prototype import gemini_diagnostics
from prototype.gemini_service import GeminiServiceError


class FakeModels:
    def __init__(self, models=None, error=None):
        self.items = models or []
        self.error = error
        self.calls = []

    def list(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return iter(self.items)


class FakeClient:
    def __init__(self, models=None, error=None):
        self.models = FakeModels(models, error)


def test_model_diagnostic_lists_ids_and_actions_only(monkeypatch):
    monkeypatch.setattr(
        gemini_diagnostics,
        "get_api_key",
        lambda: pytest.fail("injected client must not read local secrets"),
    )
    client = FakeClient(
        [
            SimpleNamespace(
                name="models/gemini-b",
                supported_actions=["generateContent", "countTokens"],
            ),
            SimpleNamespace(name="models/gemini-a", supported_actions=None),
            SimpleNamespace(name=None, supported_actions=["generateContent"]),
        ]
    )

    result = gemini_diagnostics.list_available_models(client=client)

    assert result == [
        {"model_id": "gemini-a", "supported_actions": []},
        {
            "model_id": "gemini-b",
            "supported_actions": ["countTokens", "generateContent"],
        },
    ]
    assert client.models.calls == [{"config": {"page_size": 100}}]


def test_model_diagnostic_requires_key_before_client_creation(monkeypatch):
    monkeypatch.setattr(gemini_diagnostics, "get_api_key", lambda: None)

    with pytest.raises(GeminiServiceError, match="API-nøkkel mangler"):
        gemini_diagnostics.list_available_models()


def test_model_diagnostic_passes_key_explicitly_without_displaying_it(monkeypatch, capsys):
    from google import genai

    captured = {}

    class KeyCaptureClient(FakeClient):
        def __init__(self, *, api_key, http_options):
            captured["api_key"] = api_key
            captured["timeout"] = http_options.timeout
            super().__init__(models=[])

    monkeypatch.setattr(genai, "Client", KeyCaptureClient)
    monkeypatch.setattr(gemini_diagnostics, "get_api_key", lambda: "synthetic-secret")

    assert gemini_diagnostics.main(
        ["--list-models", "--confirm-external-call"]
    ) == 0
    output = capsys.readouterr().out
    assert captured == {"api_key": "synthetic-secret", "timeout": 30_000}
    assert "synthetic-secret" not in output


def test_model_diagnostic_sanitizes_provider_error():
    client = FakeClient(error=RuntimeError("private key and response body"))

    with pytest.raises(GeminiServiceError) as caught:
        gemini_diagnostics.list_available_models(
            api_key="synthetic-test-key", client=client
        )

    assert "private" not in str(caught.value)
    assert "synthetic-test-key" not in str(caught.value)
    assert "GEMINI-UNKNOWN" in str(caught.value)


def test_cli_does_not_call_without_explicit_external_confirmation(monkeypatch, capsys):
    def must_not_run():
        pytest.fail("external diagnostic must not run without explicit confirmation")

    monkeypatch.setattr(gemini_diagnostics, "list_available_models", must_not_run)

    assert gemini_diagnostics.main(["--list-models"]) == 2
    assert "Avbrutt uten API-kall" in capsys.readouterr().err


def test_cli_without_list_flag_only_prints_help(monkeypatch, capsys):
    def must_not_run():
        pytest.fail("diagnostic must not run without --list-models")

    monkeypatch.setattr(gemini_diagnostics, "list_available_models", must_not_run)

    assert gemini_diagnostics.main([]) == 0
    assert "--confirm-external-call" in capsys.readouterr().out
