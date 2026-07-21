import joblib
from sklearn.ensemble import IsolationForest

from logger import logger
from config import MODEL_PATH


FEATURE_PATH = MODEL_PATH.parent / "feature_schema.pkl"



def save_model(
    model: IsolationForest,
    feature_columns,
) -> None:
    """
    Save model and feature schema.
    """

    try:

        MODEL_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )


        joblib.dump(
            model,
            MODEL_PATH,
        )


        joblib.dump(
            list(feature_columns),
            FEATURE_PATH,
        )


        logger.info(
            "Model saved successfully: %s",
            MODEL_PATH,
        )

        logger.info(
            "Feature schema saved successfully: %s",
            FEATURE_PATH,
        )


    except Exception as error:

        logger.error(
            "Failed saving model: %s",
            error,
        )

        raise




def load_model():
    """
    Load trained model.
    """

    if not MODEL_PATH.exists():

        logger.info(
            "No saved model found."
        )

        return None


    try:

        logger.info(
            "Loading trained model..."
        )


        return joblib.load(
            MODEL_PATH
        )


    except Exception as error:

        logger.error(
            "Failed loading model: %s",
            error,
        )

        return None




def load_feature_schema():

    if not FEATURE_PATH.exists():

        logger.info(
            "No feature schema found."
        )

        return None


    return joblib.load(
        FEATURE_PATH
    )
