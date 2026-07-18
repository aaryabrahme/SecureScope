from pathlib import Path
import streamlit as st

# ==========================================================
# Paths
# ==========================================================

ROOT = Path(__file__).resolve().parent.parent

ASSETS = ROOT / "assets"

LOGO = ASSETS / "logo.png"
ICON = ASSETS / "icon.png"


# ==========================================================
# Page Configuration
# ==========================================================

def setup_page():

    st.set_page_config(
        page_title="SecureScope",
        page_icon=str(ICON),
        layout="wide",
        initial_sidebar_state="expanded",
    )


# ==========================================================
# Sidebar
# ==========================================================

def sidebar():

    with st.sidebar:

        # ----------------------------
        # Brand Header
        # ----------------------------

        if ICON.exists():
            st.image(str(ICON), width=95)

        st.markdown(
            """
            <h2 style="margin-top:-5px;margin-bottom:0px;">
            SecureScope
            </h2>

            <p style="color:#9ca3af;margin-top:-8px;">
            Executive Security Intelligence Platform
            </p>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # ----------------------------
        # Platform Modules
        # ----------------------------

        st.markdown("### 🧩 Platform Modules")

        st.markdown("""
• 🔍 Data Discovery

• 🤖 AI Anomaly Detection

• ⚠️ Risk Intelligence

• 📊 Executive Dashboard

• 📄 Reports & Exports
""")   

def page_header(title, subtitle=None):

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()