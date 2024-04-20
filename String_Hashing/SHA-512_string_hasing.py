# Hashing is irreversible
# only way to know which string was used is to brute force
import hashlib


def hash_string(input_string):
    sha_signature = hashlib.sha512(input_string.encode()).hexdigest()
    return sha_signature


# Test the function
print(hash_string("Hello World"))
