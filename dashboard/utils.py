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
    )


def score_status(score: int) -> tuple[str, str]:
    if score >= 70:
        return "Strong", "success"
    if score >= 40:
        return "Needs attention", "warning"
    return "Elevated risk", "error"


def available_columns(dataframe: pd.DataFrame, columns: list[str]) -> list[str]:
    return [column for column in columns if column in dataframe.columns]
