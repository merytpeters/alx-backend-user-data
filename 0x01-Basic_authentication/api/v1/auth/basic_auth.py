#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
    ) -> str:
        """Returns the decoded value"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
