def route(order, latency):
    if latency < 1:
        return 'fastest_path'
    return 'safe_path'