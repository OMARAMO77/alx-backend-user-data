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
