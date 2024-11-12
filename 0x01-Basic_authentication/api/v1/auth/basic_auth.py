#!/usr/bin/env python3
"""Basic Authentication"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Returns User credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        separator = ':'
        if separator not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(separator, 1)
        if len(credentials) != 2:
            return None, None
        username, password = credentials
        return username, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """User Object"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
