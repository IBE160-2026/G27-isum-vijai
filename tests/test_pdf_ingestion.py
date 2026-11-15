"""Tests for in-memory PDF extraction and its safety limits."""

from io import BytesIO

import pytest
from pypdf import PdfWriter

from prototype.generator import generate_result
from prototype.pdf_ingestion import (
    MAX_FILE_BYTES,
    MAX_EXTRACTED_CHARACTERS,
    MAX_PAGES,
    PdfIngestionError,
    extract_pdf_text,
)


def _encrypted_pdf() -> bytes:
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    writer.encrypt("test-password")
    output = BytesIO()
    writer.write(output)
    return output.getvalue()


def test_machine_readable_pdf_text_is_returned(make_text_pdf):
    assert extract_pdf_text(make_text_pdf(["Hello PDF text."])) == "Hello PDF text."


def test_norwegian_text_is_extracted_from_pdf(make_text_pdf):
    assert extract_pdf_text(make_text_pdf(["Forelesning: æøå ÆØÅ."])) == (
        "Forelesning: æøå ÆØÅ."
    )


def test_pdf_text_normalizes_repeated_whitespace(make_text_pdf):
    assert extract_pdf_text(make_text_pdf(["Hello   PDF   text."])) == "Hello PDF text."


def test_text_from_multiple_pages_keeps_page_order(make_text_pdf):
    pdf = make_text_pdf(["First page note.", "Second page note."])

    assert extract_pdf_text(pdf) == "First page note.\nSecond page note."


def test_pdf_text_can_be_used_by_the_existing_summary_generator(make_text_pdf):
    notes = extract_pdf_text(
        make_text_pdf(
            [
                "Photosynthesis converts light into chemical energy.",
                "Chlorophyll absorbs light in plant cells.",
            ]
        )
    )

    result = generate_result(notes)

    assert result["summary"] == (
        "Photosynthesis converts light into chemical energy. "
        "Chlorophyll absorbs light in plant cells."
    )


def test_blank_pdf_has_no_extractable_text(blank_pdf_bytes):
    with pytest.raises(PdfIngestionError, match="ingen uttrekkbar tekst"):
        extract_pdf_text(blank_pdf_bytes)


@pytest.mark.parametrize("content", [b"", b"not a PDF"])
def test_empty_or_invalid_pdf_is_rejected(content):
    with pytest.raises(PdfIngestionError, match="tom eller ugyldig|kunne ikke leses"):
        extract_pdf_text(content)


def test_password_protected_pdf_is_rejected():
    with pytest.raises(PdfIngestionError, match="Passordbeskyttede"):
        extract_pdf_text(_encrypted_pdf())


def test_oversized_input_is_rejected_before_parsing():
    with pytest.raises(PdfIngestionError, match="10 MiB"):
        extract_pdf_text(b"x" * (MAX_FILE_BYTES + 1))


@pytest.mark.parametrize(
    ("page_count", "page_text", "message"),
    [
        (MAX_PAGES + 1, "text", "200 sider"),
        (1, "x" * (MAX_EXTRACTED_CHARACTERS + 1), "1 000 000 tegn"),
    ],
)
def test_page_count_and_extracted_text_limits(
    monkeypatch, page_count, page_text, message
):
    class Page:
        def extract_text(self, visitor_text):
            visitor_text(page_text, None, None, None, None)
            return page_text

    class Reader:
        is_encrypted = False
        pages = [Page() for _ in range(page_count)]

        def __init__(self, _stream, strict):
            assert strict is True

    monkeypatch.setattr("prototype.pdf_ingestion.PdfReader", Reader)
    with pytest.raises(PdfIngestionError, match=message):
        extract_pdf_text(b"%PDF-test")
