import secrets
import string

def generate_secret_key(length=24):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Generate a secret key
secret_key = generate_secret_key()
print(secret_key)
