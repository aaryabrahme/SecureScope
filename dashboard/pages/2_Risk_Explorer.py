import streamlit as st

from theme import page_header, premium_divider, section_header, setup_page, sidebar
from utils import available_columns, load_dashboard_data


def format_reasons(reasons) -> list[str]:
    if isinstance(reasons, list):
        return [str(reason) for reason in reasons]
    if isinstance(reasons, str) and reasons.strip():
        return [reasons]
    return ["No rationale was included in the unified report."]


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
    "Priority Investigations",
    "Review the highest-risk insider events included in the unified report.",
    data.generated_at,
)

events = data.risky_users.copy()
if events.empty:
    st.info("No prioritized insider-risk events are available in this report.")
    st.stop()

section_header("Investigation queue", "Filter the report's prioritized events before opening a case.")
filter_columns = st.columns(2)
with filter_columns[0]:
    severities = sorted(events["severity"].dropna().unique()) if "severity" in events else []
    selected_severities = st.multiselect("Severity", severities, default=severities)
with filter_columns[1]:
    actions = sorted(events["action"].dropna().unique()) if "action" in events else []
    selected_actions = st.multiselect("Action", actions, default=actions)

if "severity" in events:
    events = events[events["severity"].isin(selected_severities)]
if "action" in events:
    events = events[events["action"].isin(selected_actions)]

if events.empty:
    st.warning("No events match the selected filters.")
    st.stop()

display_columns = available_columns(
    events,
    ["employee_id", "file_name", "action", "location", "severity", "risk_score"],
)
st.dataframe(events[display_columns], use_container_width=True, hide_index=True)

premium_divider()
section_header("Case details", "Review the selected event and its provided risk rationale.")
event_labels = events.apply(
    lambda row: f"{row.get('employee_id', 'Unknown')} · {row.get('file_name', 'Unknown file')} · {row.get('risk_score', 0)}/100",
    axis=1,
)
selected_index = st.selectbox("Select prioritized event", event_labels.index, format_func=event_labels.get)
event = events.loc[selected_index]

metrics = st.columns(4)
metrics[0].metric("Risk score", f"{event.get('risk_score', 0)}/100")
metrics[1].metric("Severity", str(event.get("severity", "Unknown")))
metrics[2].metric("Action", str(event.get("action", "Unknown")))
metrics[3].metric("Device", str(event.get("device", "Unknown")))

detail_columns = st.columns(2)
with detail_columns[0]:
    st.markdown("**Activity context**")
    st.write(f"File: {event.get('file_name', 'Unknown')}")
    st.write(f"Sensitivity: {event.get('file_sensitivity', 'Unknown')}")
    st.write(f"Location: {event.get('location', 'Unknown')}")
with detail_columns[1]:
    st.markdown("**Risk rationale**")
    for reason in format_reasons(event.get("reasons")):
        st.write(f"• {reason}")

st.info("Recommended next step: validate the activity against access policy and supporting audit logs.")
