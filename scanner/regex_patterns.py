"""
Regex definitions for detecting sensitive information.

Each pattern contains:
- regex: Compiled regular expression
- risk: Risk assigned if matched
- reason: Optional explanation displayed in reports
"""

from typing import Any
import re

from constants import (
    MEDIUM_RISK,
    HIGH_RISK,
    CRITICAL_RISK,
)

PATTERNS: dict[str, dict[str, Any]] = {

    # --------------------------------------------------
    # Personal Information
    # --------------------------------------------------

    "EMAIL": {
        "regex": re.compile(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        ),
        "risk": MEDIUM_RISK,
    },

    "PHONE": {
        "regex": re.compile(
            r"\b[6-9]\d{9}\b"
        ),
        "risk": MEDIUM_RISK,
    },

    "PAN": {
        "regex": re.compile(
            r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
        ),
        "risk": HIGH_RISK,
    },

    "AADHAAR": {
        "regex": re.compile(
            r"\b\d{4}\s?\d{4}\s?\d{4}\b"
        ),
        "risk": HIGH_RISK,
    },

    # --------------------------------------------------
    # Credentials
    # --------------------------------------------------

    "PASSWORD_EXPOSURE": {
        "regex": re.compile(
            r'(?i)(password|passwd|pwd)\s*[:=]\s*["\']?([^\s"\']+)["\']?'
        ),
        "risk": CRITICAL_RISK,
        "reason": "Plaintext password detected in file",
    },

    # --------------------------------------------------
    # Cloud Secrets
    # --------------------------------------------------

    "AWS_ACCESS_KEY": {
        "regex": re.compile(
            r"\bAKIA[0-9A-Z]{16}\b"
        ),
        "risk": CRITICAL_RISK,
        "reason": "Potential AWS Access Key detected",
    },

    "GITHUB_TOKEN": {
        "regex": re.compile(
            r"\bghp_[A-Za-z0-9]{36}\b"
        ),
        "risk": CRITICAL_RISK,
        "reason": "Potential GitHub Personal Access Token detected",
    },
}