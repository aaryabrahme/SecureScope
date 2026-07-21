import random
from pathlib import Path

import pandas as pd


# ==============================
# Dataset Configuration
# ==============================

EMPLOYEES = [
    f"EMP{str(i).zfill(3)}"
    for i in range(1, 501)
]


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
    "DELETE",
    "UPLOAD",
    "EXPORT",
    "SHARE"
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


# ==============================
# Normal Behaviour Generator
# ==============================

def generate_normal_event():

    file_name, sensitivity = random.choice(FILES)

    return {

        "employee_id": random.choice(EMPLOYEES),


        # Normal working hours
        "login_hour": random.randint(8, 18),


        "file_name": file_name,


        "file_sensitivity": sensitivity,


        # Mostly normal actions
        "action": random.choices(
            ACTIONS,
            weights=[
                55,  # READ
                25,  # WRITE
                8,   # DOWNLOAD
                3,   # DELETE
                3,   # UPLOAD
                3,   # EXPORT
                3    # SHARE
            ]
        )[0],


        # Realistic location distribution
        "location": random.choices(
            LOCATIONS,
            weights=[
                70,  # Office
                25,  # Remote
                5    # VPN
            ]
        )[0],


        # Some employees may use personal devices
        "device": random.choices(
            DEVICES,
            weights=[
                90,
                10
            ]
        )[0],


        # Normal access volume
        "files_accessed": random.randint(
            1,
            30
        ),


        "is_anomaly": 0
    }



# ==============================
# Anomalous Behaviour Generator
# ==============================

def generate_anomaly_event():

    file_name, sensitivity = random.choice(
        [
            ("salary.xlsx", "CRITICAL"),
            ("payroll.xlsx", "CRITICAL"),
            ("finance_report.xlsx", "HIGH"),
        ]
    )


    return {

        "employee_id": random.choice(EMPLOYEES),


        # Suspicious login time
        "login_hour": random.randint(
            0,
            5
        ),


        "file_name": file_name,


        "file_sensitivity": sensitivity,


        # Mostly data extraction behaviour
        "action": random.choices(
            ACTIONS,
            weights=[
                5,   # READ
                5,   # WRITE
                70,  # DOWNLOAD
                5,   # DELETE
                5,   # UPLOAD
                5,   # EXPORT
                5    # SHARE
            ]
        )[0],


        # Suspicious access route
        "location": random.choices(
            [
                "VPN",
                "Remote"
            ],
            weights=[
                80,
                20
            ]
        )[0],


        "device": random.choices(
            [
                "Personal",
                "Managed"
            ],
            weights=[
                80,
                20
            ]
        )[0],


        # Possible exfiltration
        "files_accessed": random.randint(
            150,
            500
        ),


        "is_anomaly": 1
    }



# ==============================
# Dataset Generator
# ==============================

def generate_dataset(
    total_events=1000,
    seed=42
):

    random.seed(seed)


    events = []


    normal_events = int(
        total_events * 0.95
    )

    anomaly_events = (
        total_events - normal_events
    )


    for _ in range(normal_events):

        events.append(
            generate_normal_event()
        )


    for _ in range(anomaly_events):

        events.append(
            generate_anomaly_event()
        )


    random.shuffle(events)


    return pd.DataFrame(events)



# ==============================
# Dataset Export
# ==============================

def save_dataset(df):

    output_dir = Path(
        "datasets"
    )

    output_dir.mkdir(
        exist_ok=True
    )


    output_path = (
        output_dir /
        "access_logs.csv"
    )


    df.to_csv(
        output_path,
        index=False
    )


    return output_path



# ==============================
# Testing
# ==============================

if __name__ == "__main__":


    dataset = generate_dataset(
        total_events=1000
    )


    path = save_dataset(
        dataset
    )


    print(dataset.head())


    print()


    print(
        f"Dataset saved to: {path}"
    )


    print(
        f"Total events: {len(dataset)}"
    )


    print()


    print(
        "Class Distribution:"
    )


    print(
        dataset["is_anomaly"]
        .value_counts()
    )
