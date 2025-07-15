def vote(forks):
    return max(forks, key=lambda f: f['performance'])
