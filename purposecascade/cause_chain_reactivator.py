def reactivate_historical_goals(memory_log):
    """
    Pulls out past cause-effect sequences that led to successful or aligned alpha
    and re-inserts their purpose into the active strategy belief pool.
    """
    reactivated = []
    for log in memory_log:
        if "purpose" in log and "success" in log.get("result", ""):
            reactivated.append(log["purpose"])
    return list(set(reactivated))