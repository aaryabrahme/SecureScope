import math
from collections import Counter


def calculate_entropy(text: str) -> float:

    if not text:
        return 0

    character_counts = Counter(text)

    entropy = 0

    length = len(text)

    for character, count in character_counts.items():

        probability = count / length

        entropy += probability * math.log2(probability)

    return -entropy