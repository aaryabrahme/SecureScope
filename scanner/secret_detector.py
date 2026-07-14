from scanner.entropy import calculate_entropy


def detect_high_entropy_strings(text):

    findings = []

    words = text.split()

    for word in words:

        clean_word = word.strip()

        entropy = calculate_entropy(clean_word)

        if (
            len(clean_word) >= 12
            and entropy >= 3.0
        ):

            findings.append(
                {
                    "type": "POSSIBLE_SECRET",
                    "value": clean_word,
                    "entropy": round(entropy, 2),
                    "reason": "High randomness detected",
                    "risk": "High"
                }
            )

    return findings