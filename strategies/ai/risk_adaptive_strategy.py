def adjust_risk(vol):
    if vol > 30:
        return 0.2
    return 1.0