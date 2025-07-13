def evaluate_business_idea(idea: dict) -> float:
    """
    Score a business idea based on unmet need, uniqueness, and scalability.
    """
    need = idea.get("need_score", 0)
    uniqueness = idea.get("uniqueness", 0.5)
    scalability = idea.get("scalability", 0.5)

    score = 0.4 * (-need) + 0.3 * uniqueness + 0.3 * scalability
    return round(score, 3)