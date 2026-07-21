from typing import Any

import pandas as pd


def print_summary(summary: dict[str, Any]) -> None:
    """Display the anomaly detection summary."""

    print("\n" + "=" * 60)
    print("               SecureScope Phase 2 Summary")
    print("=" * 60)

    print(f"Total Events       : {summary['total_events']}")
    print(f"Normal Events      : {summary['normal_events']}")
    print(f"Anomalies Detected : {summary['anomaly_events']}")
    print(f"Average Risk Score : {summary['average_risk']}")
    print(f"Highest Risk Score : {summary['highest_risk']}")

    print("\nSeverity Breakdown")
    print("-" * 25)

    for level, count in summary["severity_counts"].items():
        print(f"{level:<12}: {count}")


def print_top_events(events: pd.DataFrame) -> None:
    """Display the highest-risk events."""

    print("\n" + "=" * 60)
    print("                TOP 10 RISK EVENTS")
    print("=" * 60)

    for rank, (_, event) in enumerate(events.iterrows(), start=1):

        print(f"\nRank #{rank}")
        print("-" * 60)

        print(f"Employee ID : {event['employee_id']}")
        print(f"Action      : {event['action']}")
        print(f"File        : {event['file_name']}")
        print(f"Sensitivity : {event['file_sensitivity']}")
        print(f"Status      : {event['risk_status']}")
        print(f"Risk Score  : {event['risk_score']}")
        print(f"Severity    : {event['severity']}")
        print(f"Reasons     : {event['reasons']}")


def print_export_summary(
    csv_file: str,
    json_file: str,
) -> None:
    """Display export locations."""

    print("\nReports Generated")
    print("-" * 25)
    print(f"CSV  : {csv_file}")
    print(f"JSON : {json_file}")

    print("\n" + "=" * 60)
    print("          SecureScope Analysis Complete")
    print("=" * 60)
