"""
Application-wide constants used throughout SecureScope.
"""

# -----------------------------
# Severity Levels
# -----------------------------

LOW = "LOW"
MEDIUM = "MEDIUM"
HIGH = "HIGH"
CRITICAL = "CRITICAL"

SEVERITY_LEVELS = [
    LOW,
    MEDIUM,
    HIGH,
    CRITICAL,
]

# -----------------------------
# User Actions
# -----------------------------

READ = "READ"
WRITE = "WRITE"
DOWNLOAD = "DOWNLOAD"
DELETE = "DELETE"

ACTIONS = [
    READ,
    WRITE,
    DOWNLOAD,
    DELETE,
]

# -----------------------------
# File Sensitivity
# -----------------------------

PUBLIC = "PUBLIC"
INTERNAL = "INTERNAL"
CONFIDENTIAL = "CONFIDENTIAL"
SENSITIVE = "SENSITIVE"

SENSITIVITY_LEVELS = [
    PUBLIC,
    INTERNAL,
    CONFIDENTIAL,
    SENSITIVE,
]

# -----------------------------
# Devices
# -----------------------------

MANAGED = "Managed"
UNMANAGED = "Unmanaged"

# -----------------------------
# Locations
# -----------------------------

OFFICE = "Office"
REMOTE = "Remote"
VPN = "VPN"