import streamlit as st

from theme import setup_page, sidebar
from utils import load_latest_report
from theme import setup_page, sidebar, page_header

from components import (
    risk_filters,
    risk_details,
    style_risk_table,
)

# ==========================================================
# Page Setup
# ==========================================================

setup_page()
sidebar()

page_header(
    "Risk Explorer",
    "Investigate suspicious user activity and insider threats."
)


# ==========================================================
# Load Latest Report
# ==========================================================

df, _ = load_latest_report()

if df is None:

    st.warning(
        "No reports found. Run the anomaly detection pipeline first."
    )

    st.stop()


# ==========================================================
# Filters
# ==========================================================

df = risk_filters(df)

if df.empty:

    st.warning(
        "🔍 No events match the selected filters."
    )

    st.stop()


# ==========================================================
# Matching Risk Events
# ==========================================================

with st.container(border=True):

    st.subheader("🚨 Matching Risk Events")

    st.caption(
        f"Showing **{len(df)}** matching events after applying the selected filters."
    )

    display_df = (
        df.sort_values(
            "risk_score",
            ascending=False
        )[
            [
                "employee_id",
                "action",
                "severity",
                "risk_score",
                "location",
                "device",
            ]
        ]
    )

    st.dataframe(
        style_risk_table(display_df),
        use_container_width=True,
        hide_index=True,
    )


st.divider()


# ==========================================================
# Investigation Workspace
# ==========================================================

with st.container(border=True):

    risk_details(df)


st.divider()


# ==========================================================
# Footer
# ==========================================================

st.caption(
    "🛡️ SecureScope • Version 1.3 • AI-Powered Security Intelligence • © 2026 Aarya"
)