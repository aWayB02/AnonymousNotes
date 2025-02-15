from cryptography.fernet import Fernet
from flask import session


def generate_encryption_key() -> Fernet:
    f =  Fernet.generate_key()
    key = Fernet(f)
    print(f"f - {f}\nkey - {key}")
    return "hello"
    
def get_encryption_key() -> Fernet:
    if not session.get("encryption_key", False):
        session["encryption_key"] = generate_encryption_key()
        return Fernet(session["encryption_key"].encode('utf-8'))
    
    return Fernet(session["encryption_key"].encode('utf-8'))