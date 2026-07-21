

import pandas as pd

from logger import logger
from config import ACCESS_LOG_PATH


REQUIRED_COLUMNS = {
    "employee_id",
    "file_name",
    "action",
    "location",
    "device",
    "file_sensitivity",
    "is_anomaly",
}


CATEGORICAL_FEATURES = [
    "action",
    "location",
    "device",
    "file_sensitivity",
]


DROP_COLUMNS = [
    "employee_id",
    "file_name",
    "is_anomaly",
]


def load_dataset() -> pd.DataFrame:
    """
    Load access log dataset.

    Returns:
        Raw access log dataframe.
    """

    logger.info(
        "Loading dataset from %s",
        ACCESS_LOG_PATH
    )

    df = pd.read_csv(
        ACCESS_LOG_PATH
    )

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    logger.info(
        "Dataset loaded successfully | Rows=%d Columns=%d",
        len(df),
        len(df.columns),
    )

    return df


def prepare_features(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Convert raw access logs into ML-ready features.

    Removes identifiers and labels,
    then applies one-hot encoding.

    Returns:
        Feature dataframe for anomaly detection.
    """

    logger.info("Preparing ML features...")

    features = df.copy()

    features = features.drop(
        columns=DROP_COLUMNS
    )

    features = pd.get_dummies(
        features,
        columns=CATEGORICAL_FEATURES,
    )

    logger.info(
        "Feature preparation complete | Features=%d",
        len(features.columns),
    )

    return features
