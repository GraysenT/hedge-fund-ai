def route_to_strategy(data):
    if data.get('sentiment', 0) > 0:
        return 'long'
    return 'short'