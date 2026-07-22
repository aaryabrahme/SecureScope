import streamlit as st
import json


from theme import (
    setup_page,
    sidebar,
    page_header,
    section_header,
    premium_divider,
)


from utils import (
    load_security_report,
    get_risky_users_dataframe,
    get_high_risk_files_dataframe,
)



# ==========================
# Setup
# ==========================

setup_page()
sidebar()


page_header(
    "Security Reports",
    "Review and export unified SecureScope intelligence reports."
)



# ==========================
# Load Report
# ==========================

try:

    report = load_security_report()


except FileNotFoundError:


    st.warning(
        "No unified security report found. Run intelligence pipeline first."
    )

    st.stop()



# ==========================
# Summary
# ==========================

summary = report["summary"]


section_header(
    "📊 Executive Report Summary"
)



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.metric(
        "Files Scanned",
        summary["files_scanned"]
    )


with col2:

    st.metric(
        "Sensitive Findings",
        summary["sensitive_findings"]
    )


with col3:

    st.metric(
        "Events Analysed",
        summary["events_analyzed"]
    )


with col4:

    st.metric(
        "Anomalies",
        summary["anomalies_detected"]
    )



premium_divider()



# ==========================
# Security Score
# ==========================


section_header(
    "🛡 Security Score"
)


score = report.get(
    "security_score",
    0
)


if score >= 70:

    st.error(
        f"""
## 🔴 High Risk

Security Score:

# {score}/100
"""
    )


elif score >= 40:

    st.warning(
        f"""
## 🟡 Moderate Risk

Security Score:

# {score}/100
"""
    )


else:

    st.success(
        f"""
## 🟢 Low Risk

Security Score:

# {score}/100
"""
    )



premium_divider()



# ==========================
# Data Exposure Report
# ==========================


section_header(
    "🔐 Data Security Findings"
)



files_df = get_high_risk_files_dataframe()



if not files_df.empty:


    st.dataframe(

        files_df[
            [
                "file",
                "risk_level",
                "risk_score",
            ]
        ],

        use_container_width=True,

        hide_index=True
    )


else:

    st.info(
        "No high-risk files detected."
    )



premium_divider()



# ==========================
# Insider Risk Report
# ==========================


section_header(
    "🚨 Insider Risk Events"
)



users_df = get_risky_users_dataframe()



st.dataframe(

    users_df[

        [
            "employee_id",
            "file_name",
            "action",
            "severity",
            "risk_score",
            "reasons",
        ]

    ],

    use_container_width=True,

    hide_index=True

)



premium_divider()



# ==========================
# Downloads
# ==========================


section_header(
    "⬇️ Export Reports"
)



json_data = json.dumps(
    report,
    indent=4
)



csv_data = users_df.to_csv(
    index=False
)



col1, col2 = st.columns(2)



with col1:

    st.download_button(

        "📦 Download Full JSON Report",

        json_data,

        file_name="securescope_security_report.json",

        mime="application/json",

        use_container_width=True

    )



with col2:


    st.download_button(

        "📄 Download Insider Risk CSV",

        csv_data,

        file_name="securescope_insider_risk.csv",

        mime="text/csv",

        use_container_width=True

    )



st.caption(
    "🛡 SecureScope • Version 1.3 • AI-Powered Security Intelligence"
)