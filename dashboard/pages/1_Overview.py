import streamlit as st
from datetime import datetime

from theme import setup_page, sidebar
from utils import load_latest_report
from history import load_scan_history
from theme import setup_page, sidebar, page_header

from components import (
    global_filters,
    display_metrics,
    style_risk_table,
)

from charts import (
    severity_chart,
    anomaly_chart,
    risk_distribution,
    risk_gauge,
    risk_trend_chart,
)

from executive_summary import generate_summary


# -------------------------------------------------
# Page Setup
# -------------------------------------------------

setup_page()
sidebar()

page_header(
    "Overview",
    "Executive security intelligence dashboard"
)
st.caption("Executive Security Dashboard")


# -------------------------------------------------
# Load Data
# -------------------------------------------------

df, last_scan = load_latest_report()

if df is None:
    st.warning("No reports found.")
    st.stop()


# -------------------------------------------------
# Filters
# -------------------------------------------------

filtered_df = global_filters(df)

if filtered_df.empty:
    st.warning("No events match your selected filters.")
    st.stop()


# -------------------------------------------------
# Executive Metrics
# -------------------------------------------------

with st.container(border=True):

    display_metrics(filtered_df)

    st.caption(
        f"🕒 Last Scan: {datetime.fromtimestamp(last_scan).strftime('%d %b %Y • %I:%M %p')}"
    )


st.divider()


# -------------------------------------------------
# Security Intelligence Assessment
# -------------------------------------------------

with st.container(border=True):

    st.subheader("🛡️ Security Intelligence Assessment")

    summary = generate_summary(filtered_df)

    st.markdown(summary)


st.divider()


# -------------------------------------------------
# Executive Charts
# -------------------------------------------------

with st.container(border=True):

    st.subheader("📈 Risk Analytics")

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            severity_chart(filtered_df),
            use_container_width=True,
            key="severity_chart",
        )

    with col2:

        st.plotly_chart(
            anomaly_chart(filtered_df),
            use_container_width=True,
            key="anomaly_chart",
        )

    st.plotly_chart(
        risk_distribution(filtered_df),
        use_container_width=True,
        key="risk_distribution",
    )


st.divider()


# -------------------------------------------------
# Organizational Risk
# -------------------------------------------------

with st.container(border=True):

    st.subheader("🎯 Organizational Risk")

    left, right = st.columns(2)

    with left:

        gauge_fig, org_risk = risk_gauge(filtered_df)

        st.plotly_chart(
            gauge_fig,
            use_container_width=True,
            key="risk_gauge",
        )

    with right:

        history_df = load_scan_history()

        if len(history_df) > 1:

            st.plotly_chart(
                risk_trend_chart(history_df),
                use_container_width=True,
                key="risk_trend_chart",
            )

        else:

            st.info(
                "Run additional scans to view organizational risk trends."
            )


st.divider()


# -------------------------------------------------
# Security Posture
# -------------------------------------------------

with st.container(border=True):

    st.subheader("🛡️ Security Posture")

    if org_risk < 30:

        st.success(
            "🟢 **Healthy**\n\n"
            "The organization currently exhibits a low overall risk profile. "
            "Continue routine monitoring and periodic security reviews."
        )

    elif org_risk < 70:

        st.warning(
            "🟡 **Elevated**\n\n"
            "Several indicators require attention. "
            "Review high-risk users and monitor suspicious activities."
        )

    else:

        st.error(
            "🔴 **Critical**\n\n"
            "The organization is experiencing a high-risk security posture. "
            "Immediate investigation of critical users and events is recommended."
        )

    st.caption(
        """
**Organizational Risk Index (ORI)**

The ORI is calculated using:

• **60%** Average Risk Score

• **30%** Percentage of Anomalous Events

• **10%** Percentage of Critical Severity Events
"""
    )


st.divider()


# -------------------------------------------------
# Recent Risk Events
# -------------------------------------------------

with st.container(border=True):

    st.subheader("🚨 Recent Risk Events")

    display_df = (
        filtered_df
        .sort_values("risk_score", ascending=False)[
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


# -------------------------------------------------
# Footer
# -------------------------------------------------

st.divider()

st.caption(
    "🛡️ SecureScope • AI-Powered Risk Intelligence • Version 1.3 • © 2026 Aarya"
)