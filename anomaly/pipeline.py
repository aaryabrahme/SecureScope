from anomaly.features import load_dataset, prepare_features

from anomaly.detector import (
    train_model,
    detect_anomalies,
    add_predictions
)

from anomaly.risk import calculate_risk

from anomaly.logger import logger

from anomaly.model_manager import load_model, save_model

def run_pipeline():

    logger.info("Loading dataset...")
    df = load_dataset()

    logger.info("Preparing features...")
    X = prepare_features(df)

    logger.info("Training Isolation Forest model...")
    model = load_model()

    if model is None:

        logger.info("Training new model...")

        model = train_model(X)

        save_model(model)

    else:

        logger.info("Using existing trained model.")

    logger.info("Detecting anomalies...")
    predictions = detect_anomalies(model, X)

    logger.info("Adding predictions to dataset...")
    df = add_predictions(df, predictions)

    logger.info("Calculating risk scores...")

    risk_scores = []
    severities = []
    reasons_list = []

    for _, event in df.iterrows():

        risk = calculate_risk(event)

        risk_scores.append(risk["risk_score"])
        severities.append(risk["severity"])
        reasons_list.append(", ".join(risk["reasons"]))

    df["risk_score"] = risk_scores
    df["severity"] = severities
    df["reasons"] = reasons_list

    logger.info("Pipeline completed successfully.")

    return df