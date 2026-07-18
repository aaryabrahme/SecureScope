from pathlib import Path
import json
import pandas as pd


def load_scan_history():

    report_dir = Path("reports")

    history = []

    for report in sorted(report_dir.glob("*.json")):

        try:

            with open(report, "r") as f:
                data = json.load(f)

            df = pd.DataFrame(data)

            avg_risk = df["risk_score"].mean()

            anomaly_pct = (
                (df["is_anomaly"] == 1).mean() * 100
            )

            critical_pct = (
                (df["severity"] == "CRITICAL").mean() * 100
            )

            ori = (
                (avg_risk * 0.60)
                + (anomaly_pct * 0.30)
                + (critical_pct * 0.10)
            )

            history.append(
                {
                    "Scan": report.stem,
                    "ORI": round(ori, 1)
                }
            )

        except Exception:
            continue

    return pd.DataFrame(history)