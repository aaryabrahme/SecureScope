from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

from anomaly.features import load_dataset, prepare_features
from anomaly.detector import train_model, detect_anomalies


def evaluate_model():

    df = load_dataset()

    X = prepare_features(df)

    model = train_model(X)

    predictions = detect_anomalies(model, X)


    # Convert Isolation Forest output
    # 1  -> 0 (normal)
    # -1 -> 1 (anomaly)

    predictions = [
        1 if prediction == -1 else 0
        for prediction in predictions
    ]


    actual = df["is_anomaly"]


    print("Confusion Matrix")
    print("----------------")
    print(
        confusion_matrix(
            actual,
            predictions
        )
    )


    print()

    print("Classification Report")
    print("---------------------")

    print(
        classification_report(
            actual,
            predictions
        )
    )


if __name__ == "__main__":

    evaluate_model()