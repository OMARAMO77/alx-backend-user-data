#!/usr/bin/env python3
"""A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using a random salt.
    """
    encoded = password.encode('utf-8')
    salted = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded, salted)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks is a hashed password was formed from the given password.
    """
    encoded = password.encode('utf-8')
    result = bcrypt.checkpw(encoded, hashed_password)
    return result
