from typing import Any


def print_banner() -> None:
    """Display the SecureScope banner."""

    print("\n========== SecureScope ==========\n")


def print_report(report: dict[str, Any]) -> None:
    """Display the scan report for a single file."""

    print("=" * 50)
    print(f"File       : {report['file']}")
    print(f"Risk Score : {report['risk_score']}")
    print(f"Risk Level : {report['risk_level']}")
    print()

    if not report["findings"]:
        print("No sensitive data found.\n")
        return

    print("Findings:\n")

    for finding in report["findings"]:

        print(f"[{finding['risk']}] {finding['type']}")
        print(f"Value      : {finding['value']}")

        if "entropy" in finding:
            print(f"Entropy    : {finding['entropy']}")

        if "reason" in finding:
            print(f"Reason     : {finding['reason']}")

        print()


def print_summary(
    total_files: int,
    total_findings: int,
    high_risk_files: int,
    critical_files: int,
    average_score: float,
    scan_time: float,
    report_path: str,
) -> None:
    """Display the final scan summary."""

    print("=" * 50)
    print("Scan Summary")
    print("=" * 50)

    print(f"Files Scanned : {total_files}")
    print(f"Total Findings: {total_findings}")
    print(f"High Risk Files : {high_risk_files}")
    print(f"Critical Files  : {critical_files}")
    print(f"Average Score   : {average_score:.1f}")
    print(f"Scan Time       : {scan_time:.2f} sec")

    print()
    print("=" * 50)
    print("[OK] Report exported successfully")
    print(f"Location: {report_path}")
