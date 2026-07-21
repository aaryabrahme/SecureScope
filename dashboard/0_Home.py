from pathlib import Path
import streamlit as st

from theme import setup_page, sidebar, page_header

# ==========================================================
# Setup
# ==========================================================

setup_page()
sidebar()


# ==========================================================
# Assets
# ==========================================================

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

LOGO = ASSETS / "logo.png"
ICON = ASSETS / "icon.png"


# ==========================================================
# Hero Section
# ==========================================================

if LOGO.exists():
    left, right = st.columns([2,1])

    with left:

        page_header(
            "SecureScope",
            "AI-Powered Insider Risk Detection & Security Intelligence Platform"
        )

        st.write(
            """
            Detect insider threats using machine learning,
            investigate suspicious activity and monitor your
            organization's overall security posture.
            """
        )

    with right:

        st.image(
            str(ICON),
            width=170
        )

st.markdown(
    "### AI-Powered Insider Risk Detection & Security Intelligence Platform"
)

st.write(
    """
SecureScope is an AI-powered cybersecurity platform designed to identify
insider threats, detect anomalous behaviour, and provide security teams
with actionable risk intelligence through interactive dashboards and
automated reporting.
"""
)

st.divider()

# ==========================================================
# Core Capabilities
# ==========================================================

st.header("🚀 Core Capabilities")

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.subheader("🔍 Data Discovery")

        st.write("""
- Scan enterprise datasets
- Detect secrets & credentials
- Identify sensitive files
- Generate structured reports
""")

with col2:

    with st.container(border=True):

        st.subheader("🤖 AI Risk Intelligence")

        st.write("""
- Isolation Forest detection
- Behavioural anomaly analysis
- Insider threat identification
- Dynamic risk scoring
""")

with col3:

    with st.container(border=True):

        st.subheader("📊 Executive Dashboard")

        st.write("""
- Organizational Risk Index
- Executive AI Summary
- Interactive analytics
- Investigation workspace
""")

st.divider()

# ==========================================================
# Platform Workflow
# ==========================================================

st.header("⚙️ SecureScope Workflow")

with st.container(border=True):

    st.markdown(
        """
**1. 🔍 Discover Data**

Scan enterprise files and identify sensitive information.

⬇️

**2. 🤖 Analyze Behaviour**

Machine learning detects anomalous user activity.

⬇️

**3. ⚠️ Calculate Risk**

Generate insider risk scores and classify severity.

⬇️

**4. 📊 Investigate**

Explore suspicious events using the interactive dashboard.

⬇️

**5. 📄 Report**

Export executive-ready CSV and JSON reports.
"""
    )

st.divider()

# ==========================================================
# Quick Navigation
# ==========================================================

st.header("🧭 Quick Navigation")

with st.container(border=True):

    st.markdown("""
### 📊 Overview
View organizational KPIs, AI executive summaries, risk analytics and security posture.

### 🔎 Risk Explorer
Investigate individual employees, inspect suspicious activity and review analyst recommendations.

### 📄 Reports
Download and review generated CSV and JSON reports.
""")

st.divider()

# ==========================================================
# Platform Information
# ==========================================================

left, right = st.columns(2)

with left:

    with st.container(border=True):

        st.subheader("🎯 Purpose")

        st.write(
            """
SecureScope enables security teams to proactively identify insider threats,
prioritize investigations and understand organizational risk using
AI-driven analytics.
"""
        )

with right:

    with st.container(border=True):

        st.subheader("🛠 Technology Stack")

        st.write("""
- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- JSON / CSV Reporting
""")

st.divider()

st.success(
    "👈 Use the navigation menu in the sidebar to begin exploring SecureScope."
)

st.divider()

st.caption(
    "🛡️ SecureScope • Version 1.3 • AI-Powered Security Intelligence • © 2026 Aarya"
)