import json

import streamlit as st

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
    "Unified Security Report",
    "Review and export the current consolidated security assessment.",
    data.generated_at,
)

status, alert_type = score_status(data.security_score)
metrics = st.columns(4)
metrics[0].metric("Security score", f"{data.security_score}/100", status)
metrics[1].metric("Events analyzed", data.summary["events_analyzed"])
metrics[2].metric("High-risk files", data.summary["high_risk_files"])
metrics[3].metric("Critical files", len(data.critical_files))

message = f"Current posture: {status}."
getattr(st, alert_type)(message)

premium_divider()
section_header("Data security findings", "High-risk and critical files identified by the scanner.")
if data.high_risk_files.empty:
    st.info("No high-risk files are present in this report.")
else:
    columns = available_columns(data.high_risk_files, ["file", "path", "risk_level", "risk_score", "findings"])
    st.dataframe(data.high_risk_files[columns], use_container_width=True, hide_index=True)

premium_divider()
section_header("Export report", "Download the unchanged unified-report payload or its priority-event CSV view.")
left, right = st.columns(2)
with left:
    st.download_button(
        "Download unified JSON",
        json.dumps(data.report, indent=2),
        file_name="securescope_security_report.json",
        mime="application/json",
        use_container_width=True,
    )
with right:
    st.download_button(
        "Download priority events CSV",
        data.risky_users.to_csv(index=False),
        file_name="securescope_priority_events.csv",
        mime="text/csv",
        use_container_width=True,
    )
