from scanner.scanner import FileScanner
from scanner.report import scan_file
from scanner.exporter import export_json

def main():
    scanner = FileScanner("sample_data")
    files = scanner.discover_files()

    total_files = 0
    total_findings = 0
    all_reports = []

    print("\n========== SecureScope ==========\n")

    for file in files:
        report = scan_file(file)
        all_reports.append(report)
        total_files += 1
        total_findings += len(report["findings"])

        print("=" * 50)
        print(f"File       : {report['file']}")
        print(f"Risk Score : {report['risk_score']}")
        print(f"Risk Level : {report['risk_level']}")
        print()

        if not report["findings"]:
            print("No sensitive data found.\n")
            continue

        print("Findings:\n")

        for finding in report["findings"]:
            print(f"[{finding['risk']}] {finding['type']}")
            print(f"Value      : {finding['value']}")

            if "entropy" in finding:
                print(f"Entropy    : {finding['entropy']}")

            if "reason" in finding:
                print(f"Reason     : {finding['reason']}")

            print()

    print("=" * 50)
    print("Scan Summary")
    print("=" * 50)
    print(f"Files Scanned : {total_files}")
    print(f"Total Findings: {total_findings}")
    output_path = export_json(all_reports)
    print()
    print("=" * 50)
    print(f"JSON report exported to: {output_path}")

if __name__ == "__main__":
    main()