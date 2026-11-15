"""Explicit, read-only Gemini model-list diagnostic; never generates content."""

import argparse
import sys
from collections.abc import Iterable
from typing import Any

from prototype.gemini_service import (
    GeminiServiceError,
    _provider_error_message,
    get_api_key,
)


def list_available_models(
    *, api_key: str | None = None, client: Any = None
) -> list[dict[str, list[str] | str]]:
    """List model IDs and supported actions for this key via Models.list only.

    This performs an external metadata request when called without an injected
    client. It does not call generate_content and never prints or logs the key.
    """
    key = (
        api_key
        if api_key is not None
        else (None if client is not None else get_api_key())
    )
    if client is None and not key:
        raise GeminiServiceError(
            "Gemini API-nøkkel mangler. Konfigurer GEMINI_API_KEY eller Streamlit Secrets."
        )

    try:
        if client is None:
            from google import genai
            from google.genai import types

            client = genai.Client(
                api_key=key,
                http_options=types.HttpOptions(timeout=30_000),
            )

        models: Iterable[Any] = client.models.list(config={"page_size": 100})
        result: list[dict[str, list[str] | str]] = []
        for model_info in models:
            name = getattr(model_info, "name", None)
            if not isinstance(name, str) or not name.strip():
                continue
            model_id = name.removeprefix("models/")
            actions = getattr(model_info, "supported_actions", None) or []
            safe_actions = sorted(
                {item for item in actions if isinstance(item, str)}
            )
            result.append({"model_id": model_id, "supported_actions": safe_actions})
        return sorted(result, key=lambda item: str(item["model_id"]).casefold())
    except GeminiServiceError:
        raise
    except Exception as exc:
        raise GeminiServiceError(
            "Kunne ikke liste Gemini-modeller. Kontroller nøkkel og tilgang. "
            f"[{_provider_error_message(exc).rsplit('[', 1)[-1]}"
        ) from None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Lister modell-ID-er og støttede handlinger. Ingen generering skjer. "
            "Et eksplisitt flagg kreves fordi modellen-listingen sender en "
            "ekstern metadataforespørsel til Google. API-nøkkelen vises aldri."
        )
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="list tilgjengelige modeller via Gemini Models.list API",
    )
    parser.add_argument(
        "--confirm-external-call",
        action="store_true",
        help="bekreft at du vil sende metadataforespørselen til Google",
    )
    args = parser.parse_args(argv)
    if not args.list_models:
        parser.print_help()
        return 0
    if not args.confirm_external_call:
        print(
            "Avbrutt uten API-kall. Legg til --confirm-external-call "
            "når du godkjenner ekstern modellisting.",
            file=sys.stderr,
        )
        return 2

    try:
        models = list_available_models()
    except GeminiServiceError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not models:
        print("Ingen tilgjengelige modeller returnert.")
        return 0
    for model in models:
        actions = ", ".join(model["supported_actions"])
        print(f'{model["model_id"]}\t{actions}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
