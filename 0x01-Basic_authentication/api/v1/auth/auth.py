#!/usr/bin/env python3
"""Authentication module for the API
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requires authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user.
        """
        return None
