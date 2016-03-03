import os


def gen_secret_key(length):
    secret = []
    while len(secret) < length:
        secret += [x for x in os.urandom(length) if 33 <= x <= 126]
    return ''.join(map(chr, secret[:length]))


def get_secret_key(secretkey_file, length=64):
    if os.path.exists(secretkey_file):
        with open(secretkey_file) as f:
            secret_key = f.read().strip()
    else:
        secret_key = gen_secret_key(length)
        with open(secretkey_file, 'w') as f:
            f.write(secret_key)
    return secret_key
