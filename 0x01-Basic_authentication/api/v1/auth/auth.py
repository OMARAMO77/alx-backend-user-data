#!/usr/bin/env python3
"""Authentication module for the API.
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication.
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        if not path.endswith('/'):
            path = "{}/".format(path)
        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Gets the authorization header field from the request.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user.
        """
        return None
