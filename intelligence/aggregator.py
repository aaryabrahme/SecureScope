import json
from pathlib import Path
from datetime import datetime

from config import REPORTS_DIR

from logger import logger


def load_report(path: Path):

    if not path.exists():
        raise FileNotFoundError(
            f"Report not found: {path}"
        )

    with open(path, "r") as file:
        return json.load(file)



def calculate_security_score(
    scanner_data,
    anomaly_data
):

    score = 100


    # Scanner impact

    high_risk_files = sum(
        1
        for item in scanner_data
        if item["risk_level"] in [
            "HIGH",
            "CRITICAL"
        ]
    )


    score -= high_risk_files * 5



    # Anomaly impact

    anomalies = sum(
        1
        for event in anomaly_data
        if event["risk_status"] == "ANOMALY"
    )


    score -= min(
        anomalies // 5,
        30
    )


    return max(score, 0)



def create_security_report():

    logger.info(
        "Generating unified security report..."
    )


    scanner_path = (
        REPORTS_DIR /
        "scanner" /
        "latest" /
        "scan_report.json"
    )


    anomaly_path = (
        REPORTS_DIR /
        "latest" /
        "insider_risk.json"
    )



    scanner_data = load_report(
        scanner_path
    )


    anomaly_data = load_report(
        anomaly_path
    )



    high_risk_files = [

        item

        for item in scanner_data

        if item["risk_level"] in [
            "HIGH",
            "CRITICAL"
        ]

    ]



    critical_findings = [

        item

        for item in scanner_data

        if any(
            finding["risk"] == "CRITICAL"
            for finding in item["findings"]
        )

    ]



    top_users = sorted(
        anomaly_data,
        key=lambda x: x["risk_score"],
        reverse=True
    )[:10]



    anomalies = [

        event

        for event in anomaly_data

        if event["risk_status"] == "ANOMALY"

    ]



    report = {

        "project": "SecureScope",

        "generated_at":
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),


        "summary": {

            "files_scanned":
                len(scanner_data),

            "sensitive_findings":
                sum(
                    len(item["findings"])
                    for item in scanner_data
                ),

            "high_risk_files":
                len(high_risk_files),


            "events_analyzed":
                len(anomaly_data),


            "anomalies_detected":
                len(anomalies)

        },


        "data_security": {

            "high_risk_files":
                high_risk_files,


            "critical_files":
                critical_findings

        },


        "insider_risk": {

            "top_risky_users":
                top_users

        },


        "security_score":
            calculate_security_score(
                scanner_data,
                anomaly_data
            )

    }



    output_dir = (
        REPORTS_DIR /
        "unified"
    )


    output_dir.mkdir(
        exist_ok=True
    )


    output_file = (
        output_dir /
        "security_report.json"
    )



    with open(
        output_file,
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    logger.info(
        "Unified report generated: %s",
        output_file
    )


    return output_file