import streamlit as st

from theme import setup_page, sidebar
from theme import setup_page, sidebar, page_header
from utils import (
    load_latest_report,
    convert_to_json,
)

# ==========================================================
# Page Setup
# ==========================================================

setup_page()
sidebar()

page_header(
    "Reports",
    "Review and export the latest SecureScope security assessment."
)


# ==========================================================
# Load Report
# ==========================================================

df, _ = load_latest_report()

if df is None:

    st.warning(
        "No reports found. Run the anomaly detection pipeline first."
    )

    st.stop()


# ==========================================================
# Report Status
# ==========================================================

st.success("✅ Latest security report loaded successfully.")

st.divider()


# ==========================================================
# Executive Summary
# ==========================================================

with st.container(border=True):

    st.subheader("📊 Report Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📄 Total Events",
        len(df)
    )

    col2.metric(
        "🚨 Highest Risk",
        int(df["risk_score"].max())
    )

    col3.metric(
        "🔴 Critical Events",
        len(
            df[
                df["severity"] == "CRITICAL"
            ]
        )
    )

    col4.metric(
        "🤖 Anomalies",
        int(
            (df["is_anomaly"] == 1).sum()
        )
    )


st.divider()


# ==========================================================
# Report Preview
# ==========================================================

with st.container(border=True):

    st.subheader("👀 Report Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True,
    )


st.divider()


# ==========================================================
# Export Reports
# ==========================================================

with st.container(border=True):

    st.subheader("⬇️ Export Reports")

    st.write(
        "Download the latest SecureScope report in your preferred format."
    )

    csv_data = df.to_csv(index=False)

    json_data = convert_to_json(df)

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            "📄 Download CSV Report",
            data=csv_data,
            file_name="securescope_report.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with col2:

        st.download_button(
            "📦 Download JSON Report",
            data=json_data,
            file_name="securescope_report.json",
            mime="application/json",
            use_container_width=True,
        )


st.divider()


# ==========================================================
# Footer
# ==========================================================

st.caption(
    "🛡️ SecureScope • Version 1.3 • AI-Powered Security Intelligence • © 2026 Aarya"
)