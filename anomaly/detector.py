

import pandas as pd
from sklearn.ensemble import IsolationForest

from logger import logger
from config import (
    ANOMALY_CONTAMINATION,
    ISOLATION_ESTIMATORS,
)


def train_model(
    features: pd.DataFrame,
) -> IsolationForest:
    """
    Train an Isolation Forest anomaly detection model.

    Args:
        features:
            Prepared ML feature dataframe.

    Returns:
        Trained Isolation Forest model.
    """

    logger.info(
        "Training Isolation Forest | Samples=%d Features=%d",
        features.shape[0],
        features.shape[1],
    )

    model = IsolationForest(
        n_estimators=ISOLATION_ESTIMATORS,
        contamination=ANOMALY_CONTAMINATION,
        random_state=42,
    )

    model.fit(features)

    logger.info(
        "Model training completed."
    )

    return model


def detect_anomalies(
    model: IsolationForest,
    features: pd.DataFrame,
) -> list[int]:
    """
    Predict anomalous events.

    Returns:
        List of predictions:
        -1 = anomaly
         1 = normal
    """

    logger.info(
        "Running anomaly detection..."
    )

    predictions = model.predict(features)

    return predictions.tolist()


def add_predictions(
    df: pd.DataFrame,
    predictions: list[int],
) -> pd.DataFrame:
    """
    Add anomaly predictions to original dataset.
    """

    result = df.copy()

    result["risk_status"] = [
        "ANOMALY" if prediction == -1 else "NORMAL"
        for prediction in predictions
    ]

    return result
