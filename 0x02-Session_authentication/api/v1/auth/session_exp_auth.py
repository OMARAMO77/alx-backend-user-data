#!/usr/bin/env python3
"""Session authentication with expiration module for the API.
"""
from os import getenv
from flask import request
from datetime import datetime, timedelta

from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session authentication class with expiration.
    """

    def __init__(self) -> None:
        """Initializes a new SessionExpAuth instance.
        """
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Creates a session id for the user.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """Retrieves the user id of the user associated with
        a given session id.
        """
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if "created_at" not in session_dict.keys():
            return None
        if self.session_duration <= 0:
            return session_dict.get("user_id")
        created_at = session_dict.get("created_at")
        sess_dur = timedelta(seconds=self.session_duration)
        exp_time = created_at + sess_dur
        if exp_time < datetime.now():
            return None
        return session_dict.get("user_id")
