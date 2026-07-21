import pandas as pd

from anomaly.detector import (
    add_predictions,
    detect_anomalies,
    train_model,
)
from anomaly.features import load_dataset, prepare_features
from logger import logger
from anomaly.model_manager import (
    load_model,
    save_model,
    load_feature_schema,
)
from anomaly.risk import calculate_risk


def run_pipeline() -> pd.DataFrame:
    """
    Execute the complete anomaly detection pipeline.

    Pipeline steps:
        1. Load the dataset.
        2. Prepare features.
        3. Load or train the Isolation Forest model.
        4. Detect anomalies.
        5. Calculate business risk scores.

    Returns:
        DataFrame containing anomaly predictions,
        risk scores, severity levels, and reasons.
    """

    logger.info("Loading dataset...")
    df = load_dataset()

    logger.info("Preparing features...")
    X = prepare_features(df)

    feature_columns = X.columns

    feature_schema = None

    logger.info("Loading trained model...")
    model = load_model()

    feature_schema = load_feature_schema()


    if model is None or feature_schema is None:

        logger.info(
            "Training new model..."
        )

        model = train_model(
            X
        )


        save_model(
            model,
            X.columns
        )


    else:

        logger.info(
            "Using existing trained model."
        )


    X = X.reindex(
        columns=feature_schema,
        fill_value=0
    )

    logger.info("Detecting anomalies...")
    predictions = detect_anomalies(model, X)

    logger.info("Adding predictions to dataset...")
    df = add_predictions(df, predictions)

    logger.info("Calculating business risk scores...")

    risk_results = []

    for _, event in df.iterrows():
        risk_results.append(calculate_risk(event))

    df["risk_score"] = [
        result["risk_score"]
        for result in risk_results
    ]

    df["severity"] = [
        result["severity"]
        for result in risk_results
    ]

    df["reasons"] = [
        ", ".join(result["reasons"])
        for result in risk_results
    ]

    logger.info("Pipeline completed successfully.")

    return df
