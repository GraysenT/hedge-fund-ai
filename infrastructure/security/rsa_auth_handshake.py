import rsa
(pubkey, privkey) = rsa.newkeys(2048)

def sign(message):
    return rsa.sign(message.encode(), privkey, 'SHA-256')

def verify(message, signature):
    try:
        return rsa.verify(message.encode(), signature, pubkey)
    except:
        return False