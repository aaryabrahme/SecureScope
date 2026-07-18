import os
import joblib

from anomaly.logger import logger

MODELS_DIR = "models"

os.makedirs(MODELS_DIR, exist_ok=True)

MODEL_PATH = os.path.join(
    MODELS_DIR,
    "isolation_forest.pkl"
)


def save_model(model):

    joblib.dump(model, MODEL_PATH)

    logger.info(f"Model saved to {MODEL_PATH}")


def load_model():

    if not os.path.exists(MODEL_PATH):

        logger.info("No saved model found.")

        return None

    logger.info("Loading trained model...")

    return joblib.load(MODEL_PATH)