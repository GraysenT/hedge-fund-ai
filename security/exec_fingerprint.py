import hashlib
def fingerprint(code):
    return hashlib.sha256(code.encode()).hexdigest()