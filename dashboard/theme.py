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


def _navigation_item(label: str, page: str, icon: str, active_page: str):
    if label == active_page:
        st.markdown(f'<div class="active-nav"><span>{icon}</span>{label}</div>', unsafe_allow_html=True)
    else:
        try:
            st.page_link(page, label=label, icon=icon, use_container_width=True)
        except KeyError:
            st.markdown(f'<div class="disabled-nav"><span>{icon}</span>{label}</div>', unsafe_allow_html=True)


def sidebar(generated_at: str | None = None, active_page: str = "Overview"):
    with st.sidebar:
        st.markdown('<div class="sidebar-brand">', unsafe_allow_html=True)
        if LOGO.exists():
            st.image(str(LOGO), width=46)
        st.markdown("<div class='brand-name'>SecureScope</div>", unsafe_allow_html=True)
        st.markdown("<div class='brand-subtitle'>AI Security Intelligence Platform</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="nav-section-label">WORKSPACE</div>', unsafe_allow_html=True)
        _navigation_item("Overview", "0_Home.py", "🏠", active_page)
        _navigation_item("Security Posture", "pages/1_Overview.py", "🛡️", active_page)
        _navigation_item("Risk Explorer", "pages/2_Risk_Explorer.py", "🔎", active_page)
        _navigation_item("Intelligence Center", "pages/4_Intelligence.py", "🧠", active_page)
        _navigation_item("Reports", "pages/3_Reports.py", "📄", active_page)

        st.markdown('<div class="nav-section-label">PLATFORM</div>', unsafe_allow_html=True)
        st.markdown('<div class="disabled-nav"><span>⚙️</span>Settings <small>Coming soon</small></div>', unsafe_allow_html=True)

        st.markdown('<div class="sidebar-spacer"></div>', unsafe_allow_html=True)
        if generated_at:
            st.markdown('<div class="sidebar-report-label">LATEST UNIFIED REPORT</div>', unsafe_allow_html=True)
            st.caption(generated_at)
        st.markdown('<div class="sidebar-footer">Version 1.3<br>© 2026 Aarya</div>', unsafe_allow_html=True)


def page_header(title: str, subtitle: str, generated_at: str | None = None):
    timestamp = generated_at or "No unified report available"
    brand_icon = "🛡️"
    st.markdown(
        f"""
        <div class="page-hero">
            <div class="eyebrow">{brand_icon} SECURESCOPE / AI SECURITY INTELLIGENCE</div>
            <div class="hero-title">{title}</div>
            <div class="hero-subtitle">{subtitle}</div>
            <div class="report-timestamp">Latest scan: {timestamp}</div>
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
