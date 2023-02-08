#!/usr/bin/env python3
""" Script containing session authtication script """
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Class for creating a new authentication mechanism
        Class Vari:
            user_id_by_session_id - Class attribute initialized
            by an empty dictionary
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            Instance method that creates a session ID for a user_id
            Args:
                :params: user_id [str] - User id for the first argument
            Return:
        """
        if user_id:
            if isinstance(user_id, str):
                key = str(uuid4())
                SessionAuth.user_id_by_session_id[key] = user_id
                return key
        return None
