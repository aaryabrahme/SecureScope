from pathlib import Path
from datetime import datetime

import streamlit as st

from styles import load_css

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LOGO,
    APP_TAGLINE,
)

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

    load_css()


# ==========================================================
# Sidebar
# ==========================================================

def sidebar():

    with st.sidebar:

        # ----------------------------------------
        # Logo
        # ----------------------------------------

        if ICON.exists():

            left, right = st.columns([1, 3])

            with left:

                st.image(
                    str(ICON),
                    width=70,
                )

            with right:

                st.markdown(
                    """
                    <div style="margin-top:4px;">

                    <div style="
                        font-size:24px;
                        font-weight:800;
                        color:#111827;
                        line-height:1;
                    ">
                        SecureScope
                    </div>

                    <div style="
                        color:#6B7280;
                        font-size:13px;
                        margin-top:6px;
                    ">
                        Executive Security Intelligence
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        else:

            st.title("🛡 SecureScope")

        st.markdown("<br>", unsafe_allow_html=True)

        st.divider()

        # ----------------------------------------
        # Navigation
        # ----------------------------------------

        st.markdown(
            """
### 🧩 Platform Modules

---

🔍 **Data Discovery**

Find sensitive enterprise data

---

🤖 **AI Detection**

Isolation Forest anomaly detection

---

⚠️ **Risk Intelligence**

Behavior analytics & scoring

---

📊 **Executive Dashboard**

KPIs, ORI & trends

---

📄 **Reports**

CSV / JSON exports

---
"""
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.info(
            "Version **1.3**"
        )

        st.caption(
            "© 2026 Aarya"
        )


# ==========================================================
# Dashboard Hero
# ==========================================================

def page_header(
    title,
    subtitle,
    last_scan=None,
):

    if last_scan is not None:

        scan_time = datetime.fromtimestamp(
            last_scan
        ).strftime(
            "%d %b %Y • %I:%M %p"
        )

    else:

        scan_time = "No scan available"

    st.markdown(
        f"""
<div style="

background:linear-gradient(
135deg,
#2563EB,
#1D4ED8);

padding:34px;

border-radius:24px;

color:white;

box-shadow:
0 18px 40px rgba(37,99,235,.22);

margin-bottom:30px;

">

<div style="
font-size:15px;
opacity:.9;
font-weight:600;
">

🛡 SecureScope

</div>

<div style="
font-size:40px;
font-weight:800;
margin-top:8px;
">

{title}

</div>

<div style="
font-size:17px;
opacity:.95;
margin-top:10px;
max-width:850px;
line-height:1.6;
">

{subtitle}

</div>

<div style="margin-top:25px;">

<span style="
background:rgba(255,255,255,.16);

padding:10px 18px;

border-radius:50px;

font-size:14px;

font-weight:600;
">

🕒 Latest Scan • {scan_time}

</span>

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# Section Header
# ==========================================================

def section_header(
    title,
    subtitle=None,
):

    st.markdown(
        f"""
<div style="margin-top:12px;margin-bottom:22px;">

<div style="
font-size:28px;
font-weight:700;
color:#111827;
">

{title}

</div>

{"<div style='color:#6B7280;margin-top:6px;font-size:15px;'>"+subtitle+"</div>" if subtitle else ""}

</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# Premium Divider
# ==========================================================

def premium_divider():

    st.markdown(
        """
<div style="
height:1px;
background:#E5E7EB;
margin:30px 0;
"></div>
""",
        unsafe_allow_html=True,
    )