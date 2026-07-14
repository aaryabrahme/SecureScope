PATTERNS = {
    "EMAIL": {
        "regex": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "risk": "Medium"
    },

    "PHONE": {
        "regex": r"\b[6-9]\d{9}\b",
        "risk": "Medium"
    },

    "PAN": {
        "regex": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
        "risk": "High"
    },

    "AADHAAR": {
        "regex": r"\b\d{4}\s?\d{4}\s?\d{4}\b",
        "risk": "High"
    },

    "PASSWORD_EXPOSURE": {
        "regex": r"(?i)(password|passwd|pwd)\s*[:=]\s*([^\s]+)",
        "risk": "Critical",
        "reason": "Plaintext password detected in file"
    }
}