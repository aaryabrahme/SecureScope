import json
from pathlib import Path
from datetime import datetime


def export_json(scan_results):

    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    # Generate timestamp
    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    output_file = reports_folder / f"scan_{timestamp}.json"


    # Calculate summary
    total_files = len(scan_results)

    total_findings = sum(
        len(report["findings"])
        for report in scan_results
    )


    report_data = {

        "scanner": "SecureScope",

        "version": "1.2",

        "scan_time": timestamp,

        "summary": {

            "files_scanned": total_files,

            "total_findings": total_findings

        },

        "results": scan_results

    }


    with open(output_file, "w", encoding="utf-8") as file:

        json.dump(
            report_data,
            file,
            indent=4
        )


    return output_file