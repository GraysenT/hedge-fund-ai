def resolve_conflict(civ1, civ2):
    power1 = civ1.tech * (1 + civ1.resources / 100)
    power2 = civ2.tech * (1 + civ2.resources / 100)

    if power1 > power2:
        civ1.resources += civ2.resources * 0.3
        civ2.resources *= 0.7
        winner = civ1.name
    else:
        civ2.resources += civ1.resources * 0.3
        civ1.resources *= 0.7
        winner = civ2.name

    return {
        "Winner": winner,
        "Civ1 Resources": round(civ1.resources, 2),
        "Civ2 Resources": round(civ2.resources, 2)
    }