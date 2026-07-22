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
ICON = ASSETS / "icon.png"


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
        st.caption("Security intelligence workspace")
        st.divider()
        st.markdown("**Coverage**")
        st.caption("Data exposure · Insider risk · Executive posture")

        if generated_at:
            st.divider()
            st.caption("Unified report generated")
            st.caption(generated_at)

        st.divider()
        st.caption("Version 1.3 · 2026")


def page_header(title: str, subtitle: str, generated_at: str | None = None):
    timestamp = generated_at or "No unified report available"
    st.markdown(
        f"""
        <div class="page-hero">
            <div class="eyebrow">SECURESCOPE · UNIFIED SECURITY REPORT</div>
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
