from pathlib import Path
import sys

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from dashboard.styles import load_css


PAGE_TITLE = "SecureScope"
PAGE_ICON = "Shield"
ASSETS = ROOT_DIR / "assets"
LOGO = ASSETS / "logo.png"


def setup_page():
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    load_css()


def sidebar(generated_at: str | None = None):
    with st.sidebar:
        if LOGO.exists():
            st.image(str(LOGO), width=44)

        st.title("SecureScope")
        st.caption("Enterprise security intelligence")
        st.divider()
        st.markdown("**Active modules**")
        st.caption("Posture management")
        st.caption("Data exposure intelligence")
        st.caption("Insider-risk investigations")

        if generated_at:
            st.divider()
            st.caption("Unified report generated")
            st.caption(generated_at)

        st.divider()
        st.caption("Platform version 1.3")


def page_header(title: str, subtitle: str, generated_at: str | None = None):
    timestamp = generated_at or "No unified report available"
    st.markdown(
        f"""
        <div class="page-hero">
            <div class="eyebrow">SECURESCOPE / UNIFIED INTELLIGENCE</div>
            <div class="hero-title">{title}</div>
            <div class="hero-subtitle">{subtitle}</div>
            <div class="report-timestamp">Report generated: {timestamp}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, subtitle: str | None = None):
    st.subheader(title)
    if subtitle:
        st.caption(subtitle)


def premium_divider():
    st.divider()
