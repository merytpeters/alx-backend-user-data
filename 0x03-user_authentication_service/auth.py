#!/usr/bin/env python3
"""User authentication"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
import uuid
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashed password"""
    if not password:
        raise ValueError("Password is required")

    password_bytes = password.encode()

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Constructor"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user"""
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)

        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        try:
            user = self._db.find_user_by(email=email)
            stored_password = user.hashed_password
            return bcrypt.checkpw(password.encode(), stored_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Get Session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)

            return session_id
        except NoResultFound:
            None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Find User By Session ID"""
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy Session"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generates reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                reset_password_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=reset_password_token)
                return reset_password_token
        except Exception:
            raise ValueError(
                "User not found or unable to generate reset password token")
