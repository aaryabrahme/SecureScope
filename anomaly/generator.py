import random
from pathlib import Path

import pandas as pd
EMPLOYEES = [f"EMP{str(i).zfill(3)}" for i in range(1, 51)]

FILES = [
    ("employee_handbook.pdf", "LOW"),
    ("team_notes.docx", "LOW"),
    ("project_plan.xlsx", "MEDIUM"),
    ("finance_report.xlsx", "HIGH"),
    ("salary.xlsx", "CRITICAL"),
    ("payroll.xlsx", "CRITICAL"),
]

ACTIONS = [
    "READ",
    "WRITE",
    "DOWNLOAD",
    "DELETE"
]

LOCATIONS = [
    "Office",
    "Remote",
    "VPN"
]

DEVICES = [
    "Managed",
    "Personal"
]
def generate_normal_event():

    file_name, sensitivity = random.choice(FILES)

    return {
        "employee_id": random.choice(EMPLOYEES),

        "login_hour": random.randint(8, 18),

        "file_name": file_name,

        "file_sensitivity": sensitivity,

        "action": random.choices(
            ACTIONS,
            weights=[60, 30, 5, 5]
        )[0],

        "location": random.choice(LOCATIONS),

        "device": "Managed",

        "files_accessed": random.randint(1, 30),

        "is_anomaly": 0
    }
def generate_anomaly_event():

    file_name, sensitivity = random.choice([
        ("salary.xlsx", "CRITICAL"),
        ("payroll.xlsx", "CRITICAL"),
        ("finance_report.xlsx", "HIGH"),
    ])

    return {
        "employee_id": random.choice(EMPLOYEES),

        "login_hour": random.randint(1, 4),

        "file_name": file_name,

        "file_sensitivity": sensitivity,

        "action": random.choices(
            ACTIONS,
            weights=[5, 5, 85, 5]
        )[0],

        "location": "VPN",

        "device": "Personal",

        "files_accessed": random.randint(150, 500),

        "is_anomaly": 1
    }
def generate_dataset(total_events=1000):

    events = []

    normal_events = int(total_events * 0.95)
    anomaly_events = total_events - normal_events

    for _ in range(normal_events):
        events.append(generate_normal_event())

    for _ in range(anomaly_events):
        events.append(generate_anomaly_event())

    random.shuffle(events)

    return pd.DataFrame(events)
def save_dataset(df):

    output_dir = Path("datasets")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "access_logs.csv"

    df.to_csv(output_path, index=False)

    return output_path
if __name__ == "__main__":

    dataset = generate_dataset(1000)

    path = save_dataset(dataset)

    print(dataset.head())

    print()

    print(f"Dataset saved to: {path}")

    print(f"Total events: {len(dataset)}")

    print()

    print(dataset["is_anomaly"].value_counts())