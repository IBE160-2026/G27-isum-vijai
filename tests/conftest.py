"""Shared, synthetic input fixtures for local tests."""

from collections.abc import Callable, Sequence
from io import BytesIO

import pytest
from pypdf import PdfWriter


@pytest.fixture
def blank_pdf_bytes() -> bytes:
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    output = BytesIO()
    writer.write(output)
    return output.getvalue()


@pytest.fixture
def make_text_pdf() -> Callable[[Sequence[str]], bytes]:
    """Build tiny text PDFs without storing real lecture material."""

    def build(page_texts: Sequence[str]) -> bytes:
        objects = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            b"",  # Filled after page references are known.
        ]
        page_ids = [3 + 2 * index for index in range(len(page_texts))]
        kids = " ".join(f"{page_id} 0 R" for page_id in page_ids)
        objects[1] = (
            f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode()
        )

        for index, page_text in enumerate(page_texts):
            page_id = page_ids[index]
            content_id = page_id + 1
            escaped_text = (
                page_text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            ).encode("cp1252")
            stream = (
                b"BT /F1 12 Tf 10 100 Td ("
                + escaped_text
                + b") Tj ET\n"
            )
            objects.extend(
                [
                    (
                        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] "
                        f"/Resources << /Font << /F1 << /Type /Font /Subtype /Type1 "
                        f"/BaseFont /Helvetica /Encoding /WinAnsiEncoding >> >> >> "
                        f"/Contents {content_id} 0 R >>"
                    ).encode(),
                    b"<< /Length "
                    + str(len(stream)).encode()
                    + b" >>\nstream\n"
                    + stream
                    + b"endstream",
                ]
            )

        data = bytearray(b"%PDF-1.4\n")
        offsets = []
        for number, obj in enumerate(objects, 1):
            offsets.append(len(data))
            data.extend(f"{number} 0 obj\n".encode() + obj + b"\nendobj\n")
        xref_offset = len(data)
        data.extend(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode())
        for offset in offsets:
            data.extend(f"{offset:010} 00000 n \n".encode())
        data.extend(
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_offset}\n%%EOF".encode()
        )
        return bytes(data)

    return build
