#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Sub class of Auth"""
    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        """Base64 Authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        """if not authorization_header.startswith('Basic'):
            return None
        return authorization_header.split(" ", 1)[1]"""
        parts = authorization_header.split(" ", 1)
        if len(parts) != 2:
            return None
        if not parts[0] == "Basic":
            return None
        return parts[1]
