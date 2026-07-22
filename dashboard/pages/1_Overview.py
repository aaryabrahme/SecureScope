import streamlit as st

from charts import security_score_gauge, severity_chart
from theme import page_header, premium_divider, section_header, setup_page, sidebar
from utils import available_columns, load_dashboard_data, score_status


setup_page()

try:
    data = load_dashboard_data()
except FileNotFoundError as error:
    sidebar()
    st.error("The unified security report is unavailable.")
    st.caption(str(error))
    st.stop()

sidebar(data.generated_at)
page_header(
    "Security Command Center",
    "A unified view of current data exposure and prioritized insider-risk signals.",
    data.generated_at,
)

status, alert_type = score_status(data.security_score)
metrics = st.columns(4)
metrics[0].metric("Security score", f"{data.security_score}/100", status)
metrics[1].metric("Files scanned", data.summary["files_scanned"])
metrics[2].metric("Sensitive findings", data.summary["sensitive_findings"])
metrics[3].metric("Anomalies detected", data.summary["anomalies_detected"])

premium_divider()
left, right = st.columns([1, 1])
with left:
    section_header("Security posture", "The report's authoritative security score.")
    st.plotly_chart(security_score_gauge(data.security_score), use_container_width=True)

with right:
    section_header("Priority event severity", "Distribution within the report's top-risk event list.")
    if data.risky_users.empty:
        st.info("No prioritized insider-risk events are present in this report.")
    else:
        st.plotly_chart(severity_chart(data.risky_users), use_container_width=True)

if alert_type == "success":
    st.success("Security posture is strong. Continue monitoring the prioritized events below.")
elif alert_type == "warning":
    st.warning("Security posture needs attention. Review the highest-risk files and events.")
else:
    st.error("Security posture indicates elevated risk. Prioritize containment and investigation.")

premium_divider()
section_header("Priority investigations", "Top-risk events supplied by the unified report.")
if data.risky_users.empty:
    st.info("No risky users are available.")
else:
    columns = available_columns(
        data.risky_users,
        ["employee_id", "file_name", "action", "severity", "risk_score", "reasons"],
    )
    st.dataframe(data.risky_users[columns], use_container_width=True, hide_index=True)

premium_divider()
section_header("High-risk data exposure", "Files requiring security review.")
if data.high_risk_files.empty:
    st.info("No high-risk files are available.")
else:
    columns = available_columns(data.high_risk_files, ["file", "risk_level", "risk_score"])
    st.dataframe(data.high_risk_files[columns], use_container_width=True, hide_index=True)
