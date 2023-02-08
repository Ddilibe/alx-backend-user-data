#!/usr/bin/env python3
""" Script containing session authtication script """
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Class for creating a new authentication mechanism """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        pass
