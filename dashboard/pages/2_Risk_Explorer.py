import streamlit as st

from theme import (
    setup_page,
    sidebar,
    page_header,
    section_header,
    premium_divider,
)

from utils import get_risky_users_dataframe


# ==========================
# Setup
# ==========================

setup_page()
sidebar()


page_header(
    "Risk Explorer",
    "Investigate suspicious employee behaviour and insider risk events."
)



# ==========================
# Load Data
# ==========================

df = get_risky_users_dataframe()


if df.empty:

    st.warning(
        "No risky events available."
    )

    st.stop()



# ==========================
# Employee Selection
# ==========================


section_header(
    "👤 Employee Investigation",
    "Select an employee to view detailed risk intelligence."
)



employees = df["employee_id"].unique()


selected_employee = st.selectbox(
    "Select Employee",
    employees
)



employee_data = df[
    df["employee_id"] == selected_employee
]



# ==========================
# Risk Profile
# ==========================


row = employee_data.iloc[0]


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Risk Score",
        row["risk_score"]
    )


with col2:

    st.metric(
        "Severity",
        row["severity"]
    )


with col3:

    st.metric(
        "Device",
        row["device"]
    )


with col4:

    st.metric(
        "Location",
        row["location"]
    )



premium_divider()



# ==========================
# Activity Details
# ==========================


section_header(
    "📋 Activity Details"
)



with st.container(border=True):


    st.write(
        f"""
### File Accessed

**{row['file_name']}**


### Action

**{row['action']}**


### File Sensitivity

**{row['file_sensitivity']}**


### Login Hour

**{row['login_hour']}:00**


### Files Accessed

**{row['files_accessed']}**
"""
    )



premium_divider()



# ==========================
# AI Explanation
# ==========================


section_header(
    "🤖 AI Risk Explanation"
)



with st.container(border=True):


    st.error(
        f"""
### Threat Analysis

SecureScope classified this activity as:

**{row['risk_status']}**


Reason:

{row['reasons']}


Recommended actions:

- Review employee activity logs
- Verify access legitimacy
- Check privileged file access
- Investigate credential usage
"""
    )



premium_divider()



# ==========================
# All Related Events
# ==========================


section_header(
    "📊 Employee Risk History"
)



st.dataframe(

    employee_data,

    use_container_width=True,

    hide_index=True

)



st.caption(
    "🛡 SecureScope • Version 1.3 • AI-Powered Security Intelligence"
)