import math
from collections import Counter


def calculate_entropy(text: str) -> float:
    """
    Calculate the Shannon entropy of a string.

    Higher entropy indicates greater randomness and may
    suggest the presence of secrets such as API keys,
    tokens, or passwords.

    Args:
        text: Input string.

    Returns:
        Shannon entropy as a float.
    """

    if not text:
        return 0.0

    character_counts = Counter(text)

    entropy = 0.0

    text_length = len(text)

    for count in character_counts.values():

        probability = count / text_length

        entropy += probability * math.log2(probability)

    return -entropy