
from __future__ import annotations

import streamlit as st

from digitlens.pages.home import render_page as render_home
from digitlens.pages.about import render_page as render_about
from digitlens.pages.history import render_page as render_history
from digitlens.pages.recognizer import render_page as render_recognizer

from digitlens.ui import (
    initialize_session_state,
    inject_css,
    render_sidebar,
)


st.set_page_config(
    page_title="DigitLens | Digit Recognition",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_session_state()
inject_css()

page = render_sidebar()

if page == "Beranda":
    render_home()

elif page == "Recognizer":
    render_recognizer()

elif page == "History":
    render_history()

elif page == "About Project":
    render_about()
