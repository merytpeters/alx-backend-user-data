#!/usr/bin/env python3
"""User authentication"""
import bcrypt


def _hash_password(password) -> bytes:
    """Hashed password"""
    if not password:
        raise ValueError("Password is required")

    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password
