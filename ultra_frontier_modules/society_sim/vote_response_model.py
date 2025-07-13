def estimate_public_response(happiness, corruption, education, tax):
    """
    Estimate likelihood of public support or revolt based on basic parameters.
    """
    revolt_score = 1 - happiness + corruption * 0.3 - education * 0.2 + tax * 0.2
    support_score = happiness + education * 0.3 - corruption * 0.2
    return {
        "Revolt Probability": round(min(max(revolt_score, 0), 1), 3),
        "Support Probability": round(min(max(support_score, 0), 1), 3)
    }