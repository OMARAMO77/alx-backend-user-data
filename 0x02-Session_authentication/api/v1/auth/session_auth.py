#!/usr/bin/env python3
"""Session authentication module for the API.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session authentication class.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id for the user.
        """
        if type(user_id) != str:
            None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
