#!/usr/bin/env python3
"""End to End Integration"""
import requests


BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register user"""
    response = requests.post(
        f"{BASE_URL}/users", data={"email": email, "password": password})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json() == {"email": email, "message": "user created"}, "Unexpected response payload"


def log_in_wrong_password(email: str, password: str) -> None:
    pass


def log_in(email: str, password: str) -> str:
    pass


def profile_unlogged() -> None:
    pass


def profile_logged(session_id: str) -> None:
    pass


def log_out(session_id: str) -> None:
    pass


def reset_password_token(email: str) -> str:
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    pass


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
