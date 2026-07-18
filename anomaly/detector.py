from sklearn.ensemble import IsolationForest

from anomaly.features import load_dataset, prepare_features

import pandas as pd

def train_model(X):

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(X)

    return model
def detect_anomalies(model, X):

    predictions = model.predict(X)

    return predictions
def add_predictions(df, predictions):
    df = df.copy()

    df["risk_status"] = [
        "ANOMALY" if prediction == -1 else "NORMAL"
        for prediction in predictions
    ]

    return df
if __name__ == "__main__":

    df = load_dataset()

    X = prepare_features(df)

    model = train_model(X)

    predictions = detect_anomalies(model, X)

    result = add_predictions(df, predictions)

    print(result.head())

    print()

    print(
        result["risk_status"].value_counts()
    )