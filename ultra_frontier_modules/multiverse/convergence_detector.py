def detect_convergence(universes):
    """
    Detect clusters of universes showing converging macro patterns.
    """
    clusters = []
    for i in range(len(universes)):
        base = universes[i]
        group = [base.name]
        for j in range(i + 1, len(universes)):
            comp = universes[j]
            score = (
                abs(base.inflation - comp.inflation) +
                abs(base.tech_adoption - comp.tech_adoption) +
                abs(base.war_risk - comp.war_risk) +
                abs(base.liquidity - comp.liquidity)
            )
            if score < 2.5:
                group.append(comp.name)
        if len(group) > 1:
            clusters.append(group)
    return clusters