from pathlib import Path

import pandas as pd


def load_dataset():

    dataset_path = Path("datasets/access_logs.csv")

    df = pd.read_csv(dataset_path)

    return df
def prepare_features(df):
    x= df.copy()
    x= x.drop(
    columns=[
        "employee_id",
        "file_name",
        "is_anomaly"
        ]
    )
    x= pd.get_dummies(
    x,
    columns=[
        "action",
        "location",
        "device",
        "file_sensitivity"
        ]
    )
    return x

if __name__ == "__main__":

    df = load_dataset()

    features = prepare_features(df)

    print(features.head())

    print()

    print(features.info())