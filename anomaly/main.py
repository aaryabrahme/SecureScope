from anomaly.pipeline import run_pipeline
from anomaly.summary import generate_summary
from anomaly.ranking import get_top_risk_events
from anomaly.exporter import export_csv, export_json
from datetime import datetime
from anomaly.logger import logger

def main():

    df = run_pipeline()

    summary = generate_summary(df)

    print("\n" + "=" * 60)
    print("               SecureScope Phase 2 Summary")
    print("=" * 60)
    logger.info("Starting SecureScope Phase 2")
    print(f"Total Events       : {summary['total_events']}")
    print(f"Normal Events      : {summary['normal_events']}")
    print(f"Anomalies Detected : {summary['anomaly_events']}")
    print(f"Average Risk Score : {summary['average_risk']}")
    print(f"Highest Risk Score : {summary['highest_risk']}")

    print("\nSeverity Breakdown")
    print("-" * 25)

    for level, count in summary["severity_counts"].items():
        print(f"{level:<12}: {count}")

    top_events = get_top_risk_events(df)

    print("\n" + "=" * 60)
    print("                TOP 10 RISK EVENTS")
    print("=" * 60)

    for rank, (_, event) in enumerate(top_events.iterrows(), start=1):

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

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    csv_file = export_csv(df, timestamp)
    json_file = export_json(df, timestamp)

    print("\nReports Generated")
    print("-" * 25)
    print(f"CSV  : {csv_file}")
    print(f"JSON : {json_file}")
    logger.info("SecureScope execution completed.")
    print("\n" + "=" * 60)
    print("          SecureScope Analysis Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()