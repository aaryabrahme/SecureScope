from pathlib import Path
import sys

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from dashboard.theme import page_header, premium_divider, section_header, setup_page, sidebar
from dashboard.utils import load_dashboard_data, score_status


setup_page()

try:
    data = load_dashboard_data()
except FileNotFoundError as error:
    sidebar()
    page_header(
        "Security Intelligence Workspace",
        "Generate a unified security report to begin investigation.",
    )
    st.warning("No unified security report is available.")
    st.caption(str(error))
    st.stop()

sidebar(data.generated_at)
page_header(
    "Security Intelligence Workspace",
    "Start with organizational posture, then investigate prioritized data and insider-risk signals.",
    data.generated_at,
)

status, alert_type = score_status(data.security_score)
metrics = st.columns(4)
metrics[0].metric("Security score", f"{data.security_score}/100", status)
metrics[1].metric("Files scanned", data.summary["files_scanned"])
metrics[2].metric("Sensitive findings", data.summary["sensitive_findings"])
metrics[3].metric("Priority events", len(data.risky_users))

getattr(st, alert_type)(f"Current posture: {status}.")

premium_divider()
section_header("Workflow", "Use the navigation to move from posture to evidence and export.")
columns = st.columns(3)
with columns[0]:
    with st.container(border=True):
        st.markdown("### Overview")
        st.write("Review the security score, key metrics, top events, and exposed files.")
with columns[1]:
    with st.container(border=True):
        st.markdown("### Priority investigations")
        st.write("Filter the report's highest-risk insider events and inspect their evidence.")
with columns[2]:
    with st.container(border=True):
        st.markdown("### Unified report")
        st.write("Review scanner findings and download the consolidated JSON or CSV.")

premium_divider()
section_header("Assessment scope")
st.caption(
    "This dashboard displays the generated unified security report. It does not rerun scanning, anomaly detection, or risk scoring."
)
