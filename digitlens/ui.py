
from __future__ import annotations

import streamlit as st

from digitlens.predictor import is_model_available


# ============================================================
# DIGITLENS - DEEP DIVE COLOR PALETTE
# ============================================================

APP_CSS = """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --deep: #0F1515;
    --dark-teal: #082829;
    --teal: #1C5052;
    --ocean: #177D81;
    --mist: #B7D7D0;
    --cream: #F5F8F7;
    --white: #FFFFFF;
    --muted: #526B69;
}

/* GLOBAL */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--cream);
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HEADINGS */
h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif;
    color: var(--deep);
    letter-spacing: -0.025em;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: var(--deep);
    border-right: 1px solid rgba(183,215,208,.15);
}

[data-testid="stSidebar"] .block-container {
    padding-top: 1.7rem;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: var(--mist);
}

.brand-mark {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    height: 42px;
    border-radius: 13px;
    background: var(--ocean);
    color: white;
    font-size: 21px;
    margin-right: 10px;
}

.brand-name {
    font-family: 'Manrope', sans-serif;
    font-size: 1.25rem;
    font-weight: 800;
    color: white;
}

/* SIDEBAR NAVIGATION */
[data-testid="stSidebar"] .stRadio label {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 10px;
}

/* SIDEBAR MODEL STATUS */
[data-testid="stSidebar"] [data-testid="stAlert"] {
    background: var(--dark-teal);
    border: 1px solid var(--ocean);
    border-radius: 12px;
}

[data-testid="stSidebar"] [data-testid="stAlert"] * {
    color: #FFFFFF !important;
}

/* HEADER */
.eyebrow {
    color: var(--ocean);
    text-transform: uppercase;
    letter-spacing: .11em;
    font-size: .72rem;
    font-weight: 700;
}

.muted {
    color: var(--muted);
}

/* CARDS */
.soft-card {
    border: 1px solid var(--mist);
    border-radius: 18px;
    padding: 20px;
    background: var(--white);
    box-shadow: 0 5px 18px rgba(15,21,21,.04);
}

.result-card {
    border: 1px solid var(--ocean);
    border-radius: 18px;
    padding: 24px;
    background: linear-gradient(
        135deg,
        var(--mist),
        var(--cream)
    );
}

.status-pill {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 999px;
    background: var(--mist);
    color: var(--dark-teal);
    font-size: .72rem;
    font-weight: 700;
}

.step-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 30px;
    height: 30px;
    border-radius: 10px;
    background: var(--mist);
    color: var(--dark-teal);
    font-weight: 800;
}

/* METRICS */
div[data-testid="stMetric"] {
    border: 1px solid var(--mist);
    padding: 14px;
    border-radius: 14px;
    background: var(--white);
}

div[data-testid="stMetric"] label {
    color: var(--dark-teal);
}

div[data-testid="stMetricValue"] {
    color: var(--ocean);
}

.small-note {
    font-size: .82rem;
    color: var(--muted);
}

/* BUTTONS */
.stButton > button,
.stDownloadButton > button {
    border-radius: 11px;
    font-weight: 600;
    border: 1px solid var(--ocean);
    transition: all .2s ease;
}

.stButton > button[kind="primary"] {
    background: var(--ocean);
    color: white;
    border: 1px solid var(--ocean);
}

.stButton > button[kind="primary"]:hover {
    background: var(--teal);
    border-color: var(--teal);
    color: white;
}

.stDownloadButton > button {
    background: var(--mist);
    color: var(--deep);
}

/* UPLOAD AREA */
[data-testid="stFileUploader"] {
    background: var(--white);
    border: 1px dashed var(--ocean);
    border-radius: 15px;
    padding: 12px;
}

[data-testid="stFileUploader"] button {
    border-radius: 9px;
    background: var(--ocean);
    color: white;
}

/* ALERTS */
[data-testid="stAlert"] {
    border-radius: 13px;
}

/* INPUT */
.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

/* DIVIDER */
hr {
    border-color: rgba(28,80,82,.25);
}

</style>
"""


# ============================================================
# MODEL STATUS
# ============================================================

@st.cache_resource(show_spinner="Memuat model CNN...")
def _model_ready() -> bool:
    """Memeriksa apakah model CNN dapat dimuat."""
    return is_model_available()


# ============================================================
# CSS INJECTION
# ============================================================

def inject_css() -> None:
    """Menerapkan stylesheet aplikasi."""
    st.markdown(APP_CSS, unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

def initialize_session_state() -> None:
    """Menyiapkan data sementara selama sesi aplikasi."""

    if "scan_history" not in st.session_state:
        st.session_state.scan_history = []

    if "last_segmentation" not in st.session_state:
        st.session_state.last_segmentation = None

    if "last_uploaded_key" not in st.session_state:
        st.session_state.last_uploaded_key = None

    if "page_navigation" not in st.session_state:
        st.session_state.page_navigation = "Beranda"


# ============================================================
# SIDEBAR
# ============================================================

def render_sidebar() -> str:
    """Menampilkan sidebar dan mengembalikan halaman terpilih."""

    with st.sidebar:

        st.markdown(
            """
            <div style="
                display:flex;
                align-items:center;
                margin-bottom:8px;
            ">
                <span class="brand-mark">⌗</span>
                <span class="brand-name">DigitLens</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption("Image-based Digit Recognition")

        st.divider()

        page = st.radio(
            "NAVIGATION",
            [
                "Beranda",
                "Recognizer",
                "History",
                "About Project",
            ],
            key="page_navigation",
        )

        st.divider()

        st.markdown("**Model status**")

        if _model_ready():

            st.success(
                "Model CNN aktif",
                icon="🧠",
            )

            st.caption(
                "Input 28×28 grayscale · output digit 0–9\n"
                "Klasifikasi dilakukan per potongan digit."
            )

        else:

            st.warning(
                "Model CNN belum dapat dimuat",
                icon="🧠",
            )

            st.caption(
                "Periksa models/model_cnn.keras dan instalasi "
                "Keras/TensorFlow. Detail ada di halaman Recognizer."
            )

        st.divider()

        st.caption(
            "Local prototype · v0.2 · Multi-digit segmentation"
        )

    return page


# ============================================================
# PAGE HEADER
# ============================================================

def render_header(title: str, subtitle: str) -> None:
    """Menampilkan judul dan deskripsi halaman."""

    st.markdown(
        f"<div class='eyebrow'>DIGITLENS / {title.upper()}</div>",
        unsafe_allow_html=True,
    )

    st.title(title)
    st.caption(subtitle)
