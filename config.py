from pathlib import Path


# =====================================
# Project Root
# =====================================

BASE_DIR = Path(__file__).resolve().parent



# =====================================
# Dataset Configuration
# =====================================

DATASET_DIR = BASE_DIR / "datasets"

ACCESS_LOG_PATH = (
    DATASET_DIR /
    "access_logs.csv"
)


# Scanner sample data

SAMPLE_DATA_DIR = (
    BASE_DIR /
    "sample_data"
)



# =====================================
# Model Configuration
# =====================================

MODEL_DIR = (
    BASE_DIR /
    "models"
)


MODEL_NAME = "isolation_forest.pkl"


MODEL_PATH = (
    MODEL_DIR /
    MODEL_NAME
)


# Saved feature schema
# Used to ensure inference features
# match training features

FEATURE_SCHEMA_PATH = (
    MODEL_DIR /
    "feature_schema.pkl"
)



# =====================================
# Reports Configuration
# =====================================

REPORTS_DIR = (
    BASE_DIR /
    "reports"
)


SCANNER_REPORTS_DIR = (
    REPORTS_DIR /
    "scanner"
)


ANOMALY_REPORTS_DIR = (
    REPORTS_DIR /
    "anomaly"
)


MODEL_REPORTS_DIR = (
    REPORTS_DIR /
    "model"
)



# =====================================
# Logs Configuration
# =====================================

LOGS_DIR = (
    BASE_DIR /
    "logs"
)


LOG_FILE = (
    LOGS_DIR /
    "securescope.log"
)



# =====================================
# Machine Learning Configuration
# =====================================

ANOMALY_CONTAMINATION = 0.05


ISOLATION_ESTIMATORS = 100


RANDOM_STATE = 42