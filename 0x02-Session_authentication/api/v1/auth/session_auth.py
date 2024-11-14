#!/usr/bin/env python3
"""Session Authentication"""
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session Auth Class"""
