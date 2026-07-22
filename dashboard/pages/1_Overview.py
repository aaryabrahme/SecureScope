import streamlit as st

from theme import setup_page, sidebar, page_header, section_header, premium_divider

from utils import (
    get_summary,
    get_security_score,
    get_risky_users_dataframe,
    get_high_risk_files_dataframe,
)

from charts import risk_gauge


# ==========================
# Setup
# ==========================

setup_page()
sidebar()


# ==========================
# Load Data
# ==========================

summary = get_summary()

security_score = get_security_score()

users_df = get_risky_users_dataframe()

files_df = get_high_risk_files_dataframe()



# ==========================
# Header
# ==========================

page_header(
    "Security Command Center",
    "AI-powered overview of organizational security posture and insider risk."
)



# ==========================
# Security Score
# ==========================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Security Score",
        f"{security_score}/100"
    )


with col2:

    st.metric(
        "Files Scanned",
        summary["files_scanned"]
    )


with col3:

    st.metric(
        "Sensitive Findings",
        summary["sensitive_findings"]
    )


with col4:

    st.metric(
        "Anomalies",
        summary["anomalies_detected"]
    )



premium_divider()



# ==========================
# Risk Gauge
# ==========================

section_header(
    "🛡 Organizational Security Posture"
)


dummy = users_df.copy()

if not dummy.empty:

    fig, ori = risk_gauge(dummy)

    st.plotly_chart(
        fig,
        use_container_width=True
    )



premium_divider()



# ==========================
# Top Threats
# ==========================


section_header(
    "🚨 Highest Risk Users",
    "Employees requiring immediate investigation."
)



if not users_df.empty:

    display = users_df[
        [
            "employee_id",
            "file_name",
            "action",
            "device",
            "severity",
            "risk_score",
            "reasons"
        ]
    ]


    st.dataframe(
        display,
        use_container_width=True,
        hide_index=True
    )



premium_divider()



# ==========================
# Data Exposure
# ==========================


section_header(
    "🔐 Sensitive Data Exposure",
    "Files containing high-risk security findings."
)



if not files_df.empty:


    display = files_df[
        [
            "file",
            "risk_level",
            "risk_score"
        ]
    ]


    st.dataframe(
        display,
        use_container_width=True,
        hide_index=True
    )



premium_divider()



# ==========================
# Analyst Summary
# ==========================


section_header(
    "🤖 Security Analyst Summary"
)


if security_score >= 70:

    st.error(
        """
### High Risk Environment

SecureScope detected elevated security concerns.

Recommended actions:

- Investigate top risky employees
- Rotate exposed credentials
- Review critical file access
- Monitor anomalous behaviour
"""
    )


elif security_score >= 40:

    st.warning(
        """
### Moderate Risk Environment

Additional monitoring is recommended.

Review suspicious activity and sensitive data exposure.
"""
    )


else:

    st.success(
        """
### Healthy Security Posture

No major security risks detected.
"""
    )


st.caption(
    "🛡 SecureScope • Version 1.3 • AI-Powered Security Intelligence"
)