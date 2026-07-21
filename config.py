"""
Global configuration for SecureScope.
"""

from pathlib import Path

# -------------------------------------------------------------------
# Application
# -------------------------------------------------------------------

APP_NAME = "SecureScope"
APP_TAGLINE = "AI-Powered Insider Risk Detection Platform"
VERSION = "1.3.0"

AUTHOR = "Aarya Brahme"

# -------------------------------------------------------------------
# Project Paths
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"
ASSETS_DIR = BASE_DIR / "assets"
SAMPLE_DATA_DIR = BASE_DIR / "sample_data"

# -------------------------------------------------------------------
# Dashboard
# -------------------------------------------------------------------

PAGE_TITLE = APP_NAME
PAGE_ICON = ASSETS_DIR / "icon.png"

LOGO = ASSETS_DIR / "logo.png"

# -------------------------------------------------------------------
# ML
# -------------------------------------------------------------------

MODEL_NAME = "Isolation Forest"

# -------------------------------------------------------------------
# Risk Levels
# -------------------------------------------------------------------

LOW = "LOW"
MEDIUM = "MEDIUM"
HIGH = "HIGH"
CRITICAL = "CRITICAL"