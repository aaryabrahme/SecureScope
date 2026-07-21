# =====================================
# Risk Thresholds
# =====================================

CRITICAL_THRESHOLD = 80

HIGH_THRESHOLD = 60

MEDIUM_THRESHOLD = 40



# =====================================
# Risk Scores
# =====================================

AFTER_HOURS_SCORE = 20

PERSONAL_DEVICE_SCORE = 15

VPN_SCORE = 15

HIGH_VOLUME_ACCESS_SCORE = 25

CRITICAL_FILE_SCORE = 15

ML_ANOMALY_SCORE = 30



# =====================================
# Severity Labels
# =====================================

CRITICAL = "CRITICAL"

HIGH = "HIGH"

MEDIUM = "MEDIUM"

LOW = "LOW"



# =====================================
# Scanner Risk Labels
# Backward compatibility
# =====================================

CRITICAL_RISK = CRITICAL

HIGH_RISK = HIGH

MEDIUM_RISK = MEDIUM

LOW_RISK = LOW



# =====================================
# Machine Learning Constants
# =====================================

ISOLATION_ESTIMATORS = 100

ANOMALY_CONTAMINATION = 0.05

RANDOM_STATE = 42



# =====================================
# Anomaly Labels
# =====================================

ANOMALY = "ANOMALY"

NORMAL = "NORMAL"



# =====================================
# Scanner Configuration
# =====================================

SUPPORTED_FILE_EXTENSIONS = {
    ".txt",
    ".csv",
    ".pdf",
    ".docx",
}



# =====================================
# Scanner Risk Weights
# =====================================

RISK_WEIGHTS = {
    "LOW": 5,
    "MEDIUM": 15,
    "HIGH": 35,
    "CRITICAL": 60,
}


# Backward-compatible name
SCANNER_RISK_WEIGHTS = RISK_WEIGHTS

# ==========================
# Secret Detection
# ==========================

# Minimum length of a string before entropy analysis

MIN_SECRET_LENGTH = 20


# Minimum Shannon entropy score

MIN_SECRET_ENTROPY = 4.5


# Backward compatibility

HIGH_ENTROPY_SECRET = MIN_SECRET_ENTROPY