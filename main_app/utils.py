import base64

def encode_pk(pk):
    return base64.urlsafe_b64encode(str(pk).encode()).decode()

def decode_pk(pk):
    return int(base64.urlsafe_b64decode(pk.encode()).decode())
