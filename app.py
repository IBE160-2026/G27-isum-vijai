"""Streamlit-grensesnitt for den lokale notat- og quizprototypen."""

import streamlit as st

from prototype.generator import (
    InputValidationError,
    ResultGenerationError,
    generate_result,
)
from prototype.pdf_ingestion import PdfIngestionError, extract_pdf_text


st.set_page_config(page_title="Notater til sammendrag og quiz", page_icon="📚")
st.title("Foredragsnotater → Sammendrag & Quizgenerator")
st.write("Lim inn tekst eller last opp en PDF med forelesningsnotater.")
st.warning(
    "Sammendrag og begreper velges direkte fra notatene med lokal tekstbehandling. "
    "Dette er ikke KI-generering. Quizzen er demo-data, og ingen KI-tjeneste brukes."
)

def _clear_previous_result():
    st.session_state.pop("prototype_result", None)
    st.session_state.pop("quiz_feedback", None)


input_mode = st.radio(
    "Notatformat",
    ["Tekst", "PDF"],
    horizontal=True,
    on_change=_clear_previous_result,
)
if input_mode == "PDF":
    st.caption(
        "PDF behandles lokalt i minnet. Bare maskinlesbar tekst støttes; "
        "skannede PDF-er og OCR støttes ikke. Filen lagres ikke."
    )

with st.form("notes_form"):
    if input_mode == "Tekst":
        notes = st.text_area(
            "Forelesningsnotater",
            placeholder="Lim inn notatene dine her …",
            height=220,
        )
        uploaded_pdf = None
    else:
        uploaded_pdf = st.file_uploader(
            "Last opp forelesningsnotater",
            type=["pdf"],
            help="Maks 10 MiB. PDF-en behandles lokalt og blir ikke lagret.",
        )
        notes = None
    generate_clicked = st.form_submit_button("Lag sammendrag og begreper")

if generate_clicked:
    st.session_state.pop("prototype_result", None)
    st.session_state.pop("quiz_feedback", None)
    try:
        if input_mode == "PDF":
            if uploaded_pdf is None:
                raise PdfIngestionError("Velg en PDF-fil før du genererer.")
            notes = extract_pdf_text(uploaded_pdf.getvalue())
        st.session_state.prototype_result = generate_result(notes)
    except PdfIngestionError as exc:
        st.error(str(exc))
    except InputValidationError as exc:
        st.error(str(exc))
    except ResultGenerationError:
        st.error("Resultatet kunne ikke genereres. Prøv igjen.")
    except Exception:
        st.error("Det oppstod en uventet feil. Prøv igjen.")

result = st.session_state.get("prototype_result")
if result:
    st.divider()
    st.caption("SAMMENDRAG OG BEGREPER · LOKAL TEKSTBEHANDLING · IKKE KI")

    st.header("Sammendrag")
    st.write(result["summary"])

    st.header("Sentrale begreper")
    if result["concepts"]:
        st.write(" · ".join(result["concepts"]))
    else:
        st.info("Fant ingen tydelige begreper i teksten.")

    st.header("Quiz · demonstrasjonsdata")
    st.caption("Disse faste quizspørsmålene er ikke laget fra notatene.")
    with st.form("quiz_form"):
        answers = {}
        for index, question in enumerate(result["questions"]):
            answers[index] = st.radio(
                question["question"],
                question["options"],
                key=f"answer_{index}",
            )
        check_clicked = st.form_submit_button("Sjekk svar")

    if check_clicked:
        score = sum(
            answers[index] == question["answer"]
            for index, question in enumerate(result["questions"])
        )
        st.session_state.quiz_feedback = (answers, score)

    feedback = st.session_state.get("quiz_feedback")
    if feedback:
        submitted_answers, score = feedback
        st.subheader(f"Resultat: {score} av {len(result['questions'])} riktige")
        for index, question in enumerate(result["questions"]):
            if submitted_answers[index] == question["answer"]:
                st.success(f"Spørsmål {index + 1}: Riktig. {question['explanation']}")
            else:
                st.info(
                    f"Spørsmål {index + 1}: Fasit: {question['answer']}. "
                    f"{question['explanation']}"
                )
