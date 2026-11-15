"""Local text extraction for bounded, machine-readable PDF notes."""

from io import BytesIO

from pypdf import PdfReader


MAX_FILE_BYTES = 10 * 1024 * 1024
MAX_PAGES = 200
MAX_EXTRACTED_CHARACTERS = 1_000_000


class PdfIngestionError(ValueError):
    """A PDF could not be safely read for local text extraction."""


def extract_pdf_text(data: bytes) -> str:
    """Extract text from an unencrypted, machine-readable PDF in memory."""
    if not isinstance(data, bytes) or not data:
        raise PdfIngestionError("PDF-filen er tom eller ugyldig.")
    if len(data) > MAX_FILE_BYTES:
        raise PdfIngestionError("PDF-filen er større enn grensen på 10 MiB.")

    try:
        reader = PdfReader(BytesIO(data), strict=True)
        if reader.is_encrypted:
            raise PdfIngestionError("Passordbeskyttede PDF-filer støttes ikke.")
        if len(reader.pages) > MAX_PAGES:
            raise PdfIngestionError("PDF-filen har mer enn grensen på 200 sider.")

        extracted = []
        total_characters = 0
        for page in reader.pages:
            def enforce_text_limit(text, *_context):
                nonlocal total_characters
                total_characters += len(text)
                if total_characters > MAX_EXTRACTED_CHARACTERS:
                    raise PdfIngestionError(
                        "PDF-teksten overskrider grensen på 1 000 000 tegn."
                    )

            page_text = page.extract_text(visitor_text=enforce_text_limit) or ""
            extracted.append(page_text)
    except PdfIngestionError:
        raise
    except Exception as exc:
        raise PdfIngestionError("PDF-filen kunne ikke leses. Kontroller at den er gyldig.") from exc

    normalized_pages = []
    for page_text in extracted:
        lines = [" ".join(line.split()) for line in page_text.splitlines()]
        normalized_pages.append("\n".join(line for line in lines if line))
    text = "\n".join(normalized_pages).strip()
    if not text:
        raise PdfIngestionError(
            "Fant ingen uttrekkbar tekst i PDF-filen. Skannede PDF-er med OCR støttes ikke."
        )
    return text
