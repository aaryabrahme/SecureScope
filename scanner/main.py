import time

from config import SAMPLE_DATA_DIR
from logger import logger

from scanner.console import (
    print_banner,
    print_report,
    print_summary,
)
from scanner.exporter import export_json
from scanner.report import scan_file
from scanner.scanner import FileScanner


def main() -> None:
    """
    Entry point for the SecureScope Scanner.

    Discovers supported files, scans each file for sensitive
    information, prints results, and exports a JSON report.
    """

    logger.info("Starting SecureScope scanner...")

    start_time = time.perf_counter()

    scanner = FileScanner(SAMPLE_DATA_DIR)
    files = scanner.discover_files()

    total_files = 0
    total_findings = 0
    total_score = 0

    high_risk_files = 0
    critical_files = 0

    all_reports = []

    print_banner()

    for file_path in files:

        report = scan_file(file_path)

        all_reports.append(report)

        total_files += 1
        total_findings += len(report["findings"])
        total_score += report["risk_score"]

        if report["risk_level"] == "HIGH":
            high_risk_files += 1

        elif report["risk_level"] == "CRITICAL":
            critical_files += 1

        print_report(report)

    report_path = export_json(all_reports)

    elapsed = time.perf_counter() - start_time

    average_score = (
        total_score / total_files
        if total_files
        else 0
    )

    print_summary(
        total_files=total_files,
        total_findings=total_findings,
        high_risk_files=high_risk_files,
        critical_files=critical_files,
        average_score=average_score,
        scan_time=elapsed,
        report_path=report_path,
    )

    logger.info(
        "Scan completed | Files=%d Findings=%d Duration=%.2fs",
        total_files,
        total_findings,
        elapsed,
    )


if __name__ == "__main__":
    main()
