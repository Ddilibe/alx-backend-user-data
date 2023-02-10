#!/usr/bin/env python3
""" Script containing session authtication script """
from api.v1.auth.auth import Auth
from models.user import User
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
                self.user_id_by_session_id[key] = user_id
                return key
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            Instance method that returns a user id based on Session ID
            Args:
                :params: session_id[str] - Session Arguments
            Return:
        """
        if session_id:
            if isinstance(session_id, str):
                return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """
            Instance method that returns a user instance based on cookie
            value
            Args:
                :params: @request[flask_object] - First Argument
            Return:
        """
        if cookie := self.session_cookie(request):
            if id := self.user_id_for_session_id(cookie):
                return User.get(id)
        return None

    def destroy_session(self, request=None):
        """
            Instance method that deletes the user session and logs out
            Args:
                :params: @request[Flask_Object] - First Argument
            Return:
                True if logout successful and false if log out not
                successful
        """
        if request:
            if user := self.session_cookie(request):
                if self.user_id_for_session_id(user):
                    del self.user_id_by_session_id[user]
                    return True
        return False
