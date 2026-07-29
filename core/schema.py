"""Stable internal contracts for SecureScope generated reports.

Scanner records use ``file_name`` as the canonical identifier and retain
``file`` as a compatibility alias for existing dashboard consumers. Correlated
events preserve both scanner and anomaly component scores plus the original
activity context. The unified report is the dashboard's single data source.
"""

from __future__ import annotations

from typing import Any


def scanner_file_name(record: dict[str, Any]) -> str:
    """Return a scanner record's canonical file identifier."""
    return str(record.get("file_name") or record.get("file") or "")


def normalize_reasons(value: Any) -> list[str]:
    """Normalize exported anomaly reasons into a predictable list."""
    if isinstance(value, list):
        return [str(reason).strip() for reason in value if str(reason).strip()]
    if isinstance(value, str):
        return [reason.strip() for reason in value.split(",") if reason.strip()]
    return []
