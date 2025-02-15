from cryptography.fernet import Fernet
from flask import session


def generate_encryption_key() -> bytes:
    return Fernet.generate_key()


def get_encryption_key():
    if not session.get("encryption_key", False):
        session['encryption_key'] = generate_encryption_key().decode()
    
    return Fernet(session["encryption_key"].encode())