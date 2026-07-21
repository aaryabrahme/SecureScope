import json
from pathlib import Path
from datetime import datetime

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
)

from sklearn.model_selection import train_test_split


from anomaly.features import (
    load_dataset,
    prepare_features
)

from anomaly.detector import (
    train_model,
    detect_anomalies
)


def save_evaluation_report(report):

    reports_dir = Path("reports")

    reports_dir.mkdir(
        exist_ok=True
    )

    file_path = reports_dir / "model_evaluation.json"

    print(
        f"Saving evaluation report to: {file_path.absolute()}"
    )

    with open(file_path, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )

    return file_path



def evaluate_model():

    df = load_dataset()

    X = prepare_features(df)

    y = df["is_anomaly"]


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    print(
        "Training model..."
    )


    model = train_model(
        X_train
    )


    predictions = detect_anomalies(
        model,
        X_test
    )


    # Isolation Forest conversion
    # -1 = anomaly
    # 1 = normal

    predictions = [
        1 if prediction == -1 else 0
        for prediction in predictions
    ]



    print()

    print(
        "Confusion Matrix"
    )

    print(
        "----------------"
    )


    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )



    print()

    print(
        "Classification Report"
    )

    print(
        "---------------------"
    )


    # Human readable report

    print(
        classification_report(
            y_test,
            predictions,
            target_names=[
                "NORMAL",
                "ANOMALY"
            ]
        )
    )


    # Machine readable report
    # Used for JSON export

    report = classification_report(
        y_test,
        predictions,
        target_names=[
            "NORMAL",
            "ANOMALY"
        ],
        output_dict=True
    )



    evaluation_data = {

        "model": "Isolation Forest",

        "evaluated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "dataset_size": len(df),

        "features_used": X.shape[1],

        "accuracy": round(
            report["accuracy"],
            3
        ),

        "normal_precision": round(
            report["NORMAL"]["precision"],
            3
        ),

        "anomaly_precision": round(
            report["ANOMALY"]["precision"],
            3
        ),

        "anomaly_recall": round(
            report["ANOMALY"]["recall"],
            3
        ),

        "anomaly_f1_score": round(
            report["ANOMALY"]["f1-score"],
            3
        )

    }



    path = save_evaluation_report(
        evaluation_data
    )


    print()

    print(
        f"Evaluation report saved: {path}"
    )



if __name__ == "__main__":

    evaluate_model()
