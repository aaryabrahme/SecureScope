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

SCANNER_LATEST_REPORT = SCANNER_REPORTS_DIR / "latest" / "scan_report.json"
ANOMALY_LATEST_REPORT = REPORTS_DIR / "latest" / "insider_risk.json"
UNIFIED_REPORTS_DIR = REPORTS_DIR / "unified"
CORRELATED_EVENTS_PATH = UNIFIED_REPORTS_DIR / "security_events.json"
UNIFIED_SECURITY_REPORT_PATH = UNIFIED_REPORTS_DIR / "security_report.json"



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


def ensure_runtime_directories() -> None:
    """Create directories required by local pipeline execution."""
    for directory in (
        DATASET_DIR,
        SAMPLE_DATA_DIR,
        MODEL_DIR,
        REPORTS_DIR,
        SCANNER_REPORTS_DIR / "latest",
        SCANNER_REPORTS_DIR / "archive",
        REPORTS_DIR / "latest",
        REPORTS_DIR / "archive",
        UNIFIED_REPORTS_DIR,
        LOGS_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)



# =====================================
# Machine Learning Configuration
# =====================================

ANOMALY_CONTAMINATION = 0.05


ISOLATION_ESTIMATORS = 100


RANDOM_STATE = 42
