from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_PATH = BASE_DIR / "reports" / "unified" / "security_report.json"


@dataclass(frozen=True)
class DashboardData:
    report: dict[str, Any]
    summary: dict[str, int]
    security_score: int
    risky_users: pd.DataFrame
    high_risk_files: pd.DataFrame
    critical_files: pd.DataFrame
    risk_trend: pd.DataFrame

    @property
    def generated_at(self) -> str:
        return str(self.report.get("generated_at", "Unknown"))


@st.cache_data(show_spinner=False)
def _read_report(report_mtime: float) -> dict[str, Any]:
    del report_mtime

    with REPORT_PATH.open(encoding="utf-8") as report_file:
        return json.load(report_file)


def load_security_report() -> dict[str, Any]:
    if not REPORT_PATH.exists():
        raise FileNotFoundError(f"Missing unified report: {REPORT_PATH}")

    return _read_report(REPORT_PATH.stat().st_mtime)


def load_unified_report() -> dict[str, Any]:
    return load_security_report()


def load_dashboard_data() -> DashboardData:
    report = load_security_report()
    summary = report.get("summary", {})
    data_security = report.get("data_security", {})
    insider_risk = report.get("insider_risk", {})

    return DashboardData(
        report=report,
        summary={
            "files_scanned": int(summary.get("files_scanned", 0)),
            "sensitive_findings": int(summary.get("sensitive_findings", 0)),
            "high_risk_files": int(summary.get("high_risk_files", 0)),
            "events_analyzed": int(summary.get("events_analyzed", 0)),
            "anomalies_detected": int(summary.get("anomalies_detected", 0)),
        },
        security_score=int(report.get("security_score", 0)),
        risky_users=pd.DataFrame(insider_risk.get("top_risky_users", [])),
        high_risk_files=pd.DataFrame(data_security.get("high_risk_files", [])),
        critical_files=pd.DataFrame(data_security.get("critical_files", [])),
        risk_trend=pd.DataFrame(report.get("risk_trend", [])),
    )


def get_data_security_findings() -> pd.DataFrame:
    return load_dashboard_data().high_risk_files


def get_insider_risk_users() -> pd.DataFrame:
    return load_dashboard_data().risky_users


def get_security_score() -> int:
    return load_dashboard_data().security_score


def get_data_security_summary() -> dict[str, int]:
    data = load_dashboard_data()
    return {
        "files_scanned": data.summary["files_scanned"],
        "sensitive_findings": data.summary["sensitive_findings"],
        "high_risk_files": data.summary["high_risk_files"],
        "critical_exposures": len(data.critical_files),
    }


def get_insider_risk_summary() -> dict[str, int]:
    data = load_dashboard_data()
    highest_risk_score = 0
    if not data.risky_users.empty and "risk_score" in data.risky_users:
        highest_risk_score = int(data.risky_users["risk_score"].max())

    return {
        "events_analyzed": data.summary["events_analyzed"],
        "anomalies_detected": data.summary["anomalies_detected"],
        "critical_users": count_severity(data.risky_users, "CRITICAL"),
        "highest_risk_score": highest_risk_score,
    }


def score_status(score: int) -> tuple[str, str]:
    if score >= 70:
        return "Strong", "success"
    if score >= 40:
        return "Needs attention", "warning"
    return "Elevated risk", "error"


def available_columns(dataframe: pd.DataFrame, columns: list[str]) -> list[str]:
    return [column for column in columns if column in dataframe.columns]


def count_severity(dataframe: pd.DataFrame, severity: str) -> int:
    if dataframe.empty or "severity" not in dataframe:
        return 0

    return int(dataframe["severity"].eq(severity).sum())


def executive_recommendations(data: DashboardData) -> list[str]:
    recommendations: list[str] = []

    if data.security_score < 40:
        recommendations.append("Escalate the highest-risk events to the security operations team for immediate triage.")
    elif data.security_score < 70:
        recommendations.append("Prioritize validation of high-risk users and close outstanding data exposure findings.")
    else:
        recommendations.append("Maintain continuous monitoring and validate that high-risk findings have documented owners.")

    if not data.critical_files.empty:
        recommendations.append("Contain critical file exposures and rotate any credentials found in scanned content.")

    if count_severity(data.risky_users, "CRITICAL"):
        recommendations.append("Review critical insider-risk events with the employee manager and identity team.")

    if data.summary["anomalies_detected"]:
        recommendations.append("Review anomaly evidence against access policy before closing or escalating each investigation.")

    return recommendations
