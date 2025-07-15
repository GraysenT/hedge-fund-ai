def approve_change(change):
    return 'approved' if 'params' in change else 'rejected'