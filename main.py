import subprocess
import json
from pathlib import Path
import sys

from logger import logger

from core.correlation import (
    correlate_reports,
    save_final_report,
)


def run_module(module_name):
    """
    Execute a SecureScope module.
    """

    logger.info(
        "Running module: %s",
        module_name
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            module_name
        ],
        capture_output=True,
        text=True,
    )


    if result.returncode != 0:

        logger.error(
            "%s failed",
            module_name
        )

        print(result.stderr)

        raise RuntimeError(
            f"{module_name} failed"
        )


    print(result.stdout)



def find_latest_report(prefix):

    reports_dir = Path("reports")

    files = list(
        reports_dir.glob(
            f"{prefix}*.json"
        )
    )


    if not files:
        raise FileNotFoundError(
            f"No report found for {prefix}"
        )


    return max(
        files,
        key=lambda file: file.stat().st_mtime
    )



def main():

    print("=" * 70)
    print("              SecureScope Platform")
    print("=" * 70)


    # -------------------------
    # Phase 1
    # -------------------------

    run_module(
        "scanner.main"
    )


    scanner_report = Path(
        "reports/scanner/latest/scan_report.json"
    )


    # -------------------------
    # Phase 2
    # -------------------------

    run_module(
        "anomaly.main"
    )


    anomaly_report = Path(
        "reports/latest/insider_risk.json"
    )


    # -------------------------
    # Phase 3
    # -------------------------

    logger.info(
        "Starting risk correlation..."
    )


    final_events = correlate_reports(
        scanner_report,
        anomaly_report,
    )


    final_report = save_final_report(
        final_events
    )


    print()

    print("=" * 70)
    print("          SecureScope Complete")
    print("=" * 70)

    print()

    print(
        f"Final Report: {final_report}"
    )


    logger.info(
        "SecureScope execution completed successfully"
    )



if __name__ == "__main__":
    main()