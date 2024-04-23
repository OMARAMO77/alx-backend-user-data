#!/usr/bin/env python3
"""
End to end integration testing
"""
import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """Tests registering a user.
    """
    pass


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests logging in with a wrong password.
    """
    pass


def log_in(email: str, password: str) -> str:
    """Tests logging in.
    """
    pass


def profile_unlogged() -> None:
    """Tests retrieving profile information whilst logged out.
    """
    pass


def profile_logged(session_id: str) -> None:
    """Tests retrieving profile information whilst logged in.
    """
    pass


def log_out(session_id: str) -> None:
    """Tests logging out of a session.
    """
    pass


def reset_password_token(email: str) -> str:
    """Tests requesting a password reset.
    """
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests updating a user's password.
    """
    pass


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
