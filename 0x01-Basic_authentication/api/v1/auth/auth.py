#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that enforces authentication"""
        if path is None or excluded_paths is None:
            return True
        if not path.endswith('/'):
            # Ensure that path is slash tolerant
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User"""
        return None
