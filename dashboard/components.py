import streamlit as st


# ==========================================================
# Sidebar Filters
# ==========================================================

def risk_filters(df):

    st.sidebar.header("🔍 Filters")

    if st.sidebar.button("Clear Filters"):

        st.session_state["severity_filter"] = list(
            df["severity"].unique()
        )

        st.session_state["action_filter"] = list(
            df["action"].unique()
        )

        st.session_state["location_filter"] = list(
            df["location"].unique()
        )

        st.rerun()

    severity = st.sidebar.multiselect(
        "Severity",
        options=df["severity"].unique(),
        default=list(df["severity"].unique()),
        key="severity_filter"
    )

    action = st.sidebar.multiselect(
        "Action",
        options=df["action"].unique(),
        default=list(df["action"].unique()),
        key="action_filter"
    )

    location = st.sidebar.multiselect(
        "Location",
        options=df["location"].unique(),
        default=list(df["location"].unique()),
        key="location_filter"
    )

    filtered_df = df[
        (df["severity"].isin(severity))
        &
        (df["action"].isin(action))
        &
        (df["location"].isin(location))
    ]

    return filtered_df


def global_filters(df):

    st.sidebar.subheader("🌐 Global Filters")

    severity = st.sidebar.multiselect(
        "Severity",
        df["severity"].unique(),
        default=list(df["severity"].unique())
    )

    location = st.sidebar.multiselect(
        "Location",
        df["location"].unique(),
        default=list(df["location"].unique())
    )

    filtered_df = df[
        (df["severity"].isin(severity))
        &
        (df["location"].isin(location))
    ]

    return filtered_df


# ==========================================================
# Executive KPI Cards
# ==========================================================

def display_metrics(df):

    total_events = len(df)

    anomalies = (df["is_anomaly"] == 1).sum()

    avg_risk = df["risk_score"].mean()

    highest_risk = df["risk_score"].max()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📄 Total Events",
        f"{total_events:,}"
    )

    col2.metric(
        "🚨 Anomalies",
        anomalies
    )

    col3.metric(
        "📈 Avg Risk",
        f"{avg_risk:.1f}"
    )

    col4.metric(
        "🔥 Highest Risk",
        highest_risk
    )


# ==========================================================
# Investigation Panel
# ==========================================================

def risk_details(df):

    st.subheader("🔎 Investigation Panel")

    selected_employee = st.selectbox(
        "Select Employee",
        sorted(df["employee_id"].unique())
    )

    event = df[
        df["employee_id"] == selected_employee
    ].iloc[0]

    score = int(event["risk_score"])
    severity = str(event["severity"]).upper()

    # ------------------------------------------------------
    # Executive Summary Card
    # ------------------------------------------------------

    with st.container(border=True):

        st.markdown(f"## 👤 {event['employee_id']}")

        if severity == "CRITICAL":
            st.error("🔴 CRITICAL")

        elif severity == "HIGH":
            st.warning("🟠 HIGH")

        elif severity == "MEDIUM":
            st.info("🟡 MEDIUM")

        else:
            st.success("🟢 LOW")

        st.metric(
            "Risk Score",
            f"{score}/100"
        )

        st.progress(score / 100)

    # ------------------------------------------------------
    # Event Details
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("📋 Event Details")

        left, right = st.columns(2)

        with left:

            st.write("**Action**")
            st.write(event["action"])

            st.write("**Location**")
            st.write(event["location"])

            st.write("**Device**")
            st.write(event["device"])

        with right:

            st.write("**File**")
            st.write(event["file_name"])

            st.write("**Sensitivity**")
            st.write(event["file_sensitivity"])

            status = (
                "Anomaly"
                if event["is_anomaly"] == 1
                else "Normal"
            )

            st.write("**Status**")
            st.write(status)

    # ------------------------------------------------------
    # Risk Factors
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("⚠️ Risk Factors")

        reasons = event.get("reasons", [])

        if isinstance(reasons, str):

            reasons = (
                reasons
                .strip("[]")
                .replace("'", "")
                .split(",")
            )

        if reasons:

            for reason in reasons:

                st.markdown(
                    f"• {str(reason).strip()}"
                )

        else:

            st.success(
                "No additional risk factors detected."
            )

    # ------------------------------------------------------
    # Analyst Recommendation
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("🧠 Analyst Recommendation")

        if severity == "CRITICAL":

            st.error(
                """
**Immediate Action Required**

• Review authentication logs

• Verify privileged activity

• Suspend access if compromise is suspected

• Escalate to the Security Operations Center
"""
            )

        elif severity == "HIGH":

            st.warning(
                """
**Priority Investigation**

• Review recent file access

• Monitor ongoing activity

• Escalate if additional anomalies occur
"""
            )

        elif severity == "MEDIUM":

            st.info(
                """
**Continue Monitoring**

• Validate unusual behaviour

• Review future activity

• Escalate if risk increases
"""
            )

        else:

            st.success(
                """
**Routine Monitoring**

No immediate analyst action is required.
"""
            )


# ==========================================================
# Table Styling
# ==========================================================

def style_risk_table(df):

    display_df = df.copy()

    def severity_icon(value):

        if value == "CRITICAL":
            return "🔴 CRITICAL"

        elif value == "HIGH":
            return "🟠 HIGH"

        elif value == "MEDIUM":
            return "🟡 MEDIUM"

        else:
            return "🟢 LOW"

    display_df["severity"] = (
        display_df["severity"]
        .apply(severity_icon)
    )

    return display_df