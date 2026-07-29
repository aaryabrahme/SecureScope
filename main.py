"""Run the complete SecureScope local demo pipeline."""

import subprocess
import sys

from config import (
    ANOMALY_LATEST_REPORT,
    CORRELATED_EVENTS_PATH,
    SCANNER_LATEST_REPORT,
    UNIFIED_SECURITY_REPORT_PATH,
    ensure_runtime_directories,
)
from core.correlation import correlate_reports, save_final_report
from intelligence.aggregator import create_security_report
from logger import logger


def run_module(module_name: str) -> None:
    logger.info("Running module: %s", module_name)
    result = subprocess.run([sys.executable, "-m", module_name], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"{module_name} failed:\n{result.stderr.strip()}")
    if result.stdout:
        print(result.stdout)


def main() -> None:
    ensure_runtime_directories()
    print("=" * 70)
    print("SecureScope local security-analysis demo")
    print("=" * 70)

    run_module("scanner.main")
    run_module("anomaly.main")

    for report_path, label in (
        (SCANNER_LATEST_REPORT, "scanner"),
        (ANOMALY_LATEST_REPORT, "anomaly"),
    ):
        if not report_path.exists():
            raise FileNotFoundError(f"{label.title()} stage did not produce required report: {report_path}")

    events = correlate_reports(SCANNER_LATEST_REPORT, ANOMALY_LATEST_REPORT)
    save_final_report(events, CORRELATED_EVENTS_PATH)
    unified_report = create_security_report(
        SCANNER_LATEST_REPORT,
        ANOMALY_LATEST_REPORT,
        CORRELATED_EVENTS_PATH,
        UNIFIED_SECURITY_REPORT_PATH,
    )
    print(f"Unified report: {unified_report}")
    print("Note: demo anomaly results are risk indicators, not confirmed malicious activity.")


if __name__ == "__main__":
    main()
