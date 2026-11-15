"""Streamlit-grensesnitt for den lokale notat- og quizprototypen."""

import streamlit as st

from prototype.generator import (
    InputValidationError,
    ResultGenerationError,
    generate_result,
)
from prototype.pdf_ingestion import PdfIngestionError, extract_pdf_text
from prototype.gemini_service import GeminiServiceError, generate_gemini_result


st.set_page_config(page_title="Notater til sammendrag og quiz", page_icon="📚")
st.title("Foredragsnotater → Sammendrag & Quizgenerator")
st.write("Lim inn tekst eller last opp en PDF med forelesningsnotater.")

def _clear_previous_result():
    st.session_state.pop("prototype_result", None)
    st.session_state.pop("quiz_feedback", None)


generation_mode = st.selectbox("Genereringsmodus", ["Lokal", "Gemini AI"], on_change=_clear_previous_result)
if generation_mode == "Lokal":
    st.warning(
        "Sammendrag og begreper velges direkte fra notatene med lokal tekstbehandling. "
        "Dette er ikke KI-generering. Quizzen er demo-data, og ingen KI-tjeneste brukes."
    )
if generation_mode == "Gemini AI":
    st.warning("Ved generering sendes notatteksten til Google Gemini for ekstern behandling. Free Tier-data kan brukes til å forbedre Googles produkter. KI-resultater kan være feil. Del aldri sensitive eller fortrolige notater.")
    summary_length = st.selectbox("Sammendragslengde", ["kort", "middels", "lang"], index=1)
    difficulty = st.selectbox("Quizvanskelighetsgrad", ["lett", "middels", "vanskelig"], index=1)
    question_count = st.slider("Antall quizspørsmål", 1, 10, 5)

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

if input_mode == "Tekst":
    notes = st.text_area(
        "Forelesningsnotater",
        placeholder="Lim inn notatene dine her …",
        height=220,
        on_change=_clear_previous_result,
    )
    uploaded_pdf = None
else:
    uploaded_pdf = st.file_uploader(
        "Last opp forelesningsnotater",
        type=["pdf"],
        help=("Maks 10 MiB. Teksten trekkes ut lokalt og sendes til Gemini først etter at du starter generering og bekrefter samtykke."
              if generation_mode == "Gemini AI" else "Maks 10 MiB. PDF-en behandles lokalt og blir ikke lagret."),
        on_change=_clear_previous_result,
    )
    notes = None
consent = st.checkbox("Jeg forstår at notatene sendes til Google Gemini for behandling.") if generation_mode == "Gemini AI" else False
generate_clicked = st.button("Generer læringsressurser")

if generate_clicked:
    st.session_state.pop("prototype_result", None)
    st.session_state.pop("quiz_feedback", None)
    try:
        if input_mode == "PDF":
            if uploaded_pdf is None:
                raise PdfIngestionError("Velg en PDF-fil før du genererer.")
            notes = extract_pdf_text(uploaded_pdf.getvalue())
        if generation_mode == "Gemini AI":
            if not consent:
                st.error("Bekreft personverninformasjonen før Gemini-generering.")
            else:
                st.session_state.prototype_result = generate_gemini_result(
                    notes, length=summary_length, difficulty=difficulty, question_count=question_count
                )
        else:
            st.session_state.prototype_result = generate_result(notes)
    except PdfIngestionError as exc:
        st.error(str(exc))
    except InputValidationError as exc:
        st.error(str(exc))
    except ResultGenerationError:
        st.error("Resultatet kunne ikke genereres. Prøv igjen.")
    except GeminiServiceError as exc:
        st.error(str(exc))
    except Exception:
        st.error("Det oppstod en uventet feil. Prøv igjen.")

result = st.session_state.get("prototype_result")
if result:
    st.divider()
    is_ai = "questions" in result and "sources" not in result
    st.caption("SAMMENDRAG · BEGREPER · QUIZ · GEMINI AI" if is_ai else "SAMMENDRAG OG BEGREPER · LOKAL TEKSTBEHANDLING · IKKE KI")
    if is_ai:
        st.caption(result.get("grounding_notice", "Innholdet er kontrollert mot sitater fra notatene, men kontrollen garanterer ikke at alt er feilfritt."))

    st.header("Sammendrag")
    st.write(result["summary"])

    st.header("Sentrale begreper")
    if result["concepts"]:
        if is_ai:
            for concept in result["concepts"]:
                st.markdown(f"**{concept['term']}** — {concept['explanation']}")
        else:
            st.write(" · ".join(result["concepts"]))
    else:
        st.info("Fant ingen tydelige begreper i teksten.")

    if is_ai:
        st.header("Quiz")
        for i, question in enumerate(result["questions"], 1):
            st.markdown(f"**{i}. {question['question']}**")
            st.write(" · ".join(question["options"]))
        if result["insufficient_questions"]:
            st.info(f"Notatene ga grunnlag for {len(result['questions'])} av {question_count} ønskede spørsmål.")
    else:
        st.header("Quiz · demonstrasjonsdata")
    if not is_ai:
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
            if is_ai:
                status = "Riktig" if submitted_answers[index] == question["answer"] else "Ikke riktig"
                st.info(f"Spørsmål {index + 1}: {status}. Fasit: {question['answer']}. {question['explanation']}")
            elif submitted_answers[index] == question["answer"]:
                st.success(f"Spørsmål {index + 1}: Riktig. {question['explanation']}")
            else:
                st.info(f"Spørsmål {index + 1}: Fasit: {question['answer']}. {question['explanation']}")
