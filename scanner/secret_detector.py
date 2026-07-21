from typing import Any

from constants import (
    HIGH,
    HIGH_ENTROPY_SECRET,
    MIN_SECRET_ENTROPY,
    MIN_SECRET_LENGTH,
)
from scanner.entropy import calculate_entropy


def detect_high_entropy_strings(
    text: str,
) -> list[dict[str, Any]]:
    """
    Detect potential secrets based on Shannon entropy.

    Strings that are sufficiently long and highly random
    are flagged as possible API keys, tokens, or passwords.

    Returns:
        List of entropy-based findings.
    """

    findings: list[dict[str, Any]] = []

    for word in text.split():

        clean_word = word.strip()

        if not clean_word:
            continue

        if len(clean_word) < MIN_SECRET_LENGTH:
            continue

        entropy = calculate_entropy(clean_word)

        if entropy >= MIN_SECRET_ENTROPY:

            findings.append(
                {
                    "type": HIGH_ENTROPY_SECRET,
                    "value": clean_word,
                    "entropy": round(entropy, 2),
                    "reason": (
                        "String contains high randomness and "
                        "may represent a secret token"
                    ),
                    "risk": HIGH,
                }
            )

    return findings
