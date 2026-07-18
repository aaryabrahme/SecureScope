import json
from pathlib import Path
import pandas as pd


def load_latest_report():

    report_dir = Path("reports")

    json_files = list(report_dir.glob("*.json"))

    if not json_files:
        return None, None

    latest_file = max(
        json_files,
        key=lambda x: x.stat().st_mtime
    )

    with open(latest_file, "r") as file:
        data = json.load(file)

    return (
        pd.DataFrame(data),
        latest_file.stat().st_mtime
    )


def convert_to_json(df):

    return json.dumps(
        df.to_dict(orient="records"),
        indent=4
    )