from pathlib import Path
import json
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

REPORT_PATH = (
    BASE_DIR
    / "reports"
    / "unified"
    / "security_report.json"
)


def load_security_report():

    if not REPORT_PATH.exists():

        raise FileNotFoundError(
            f"Missing report: {REPORT_PATH}"
        )


    with open(
        REPORT_PATH,
        "r"
    ) as file:

        return json.load(file)



def get_summary():

    report = load_security_report()

    return report["summary"]



def get_security_score():

    report = load_security_report()

    return report.get(
        "security_score",
        0
    )



def get_risky_users_dataframe():

    report = load_security_report()

    users = (
        report
        ["insider_risk"]
        ["top_risky_users"]
    )

    return pd.DataFrame(users)



def get_high_risk_files_dataframe():

    report = load_security_report()

    files = (
        report
        ["data_security"]
        ["high_risk_files"]
    )

    return pd.DataFrame(files)