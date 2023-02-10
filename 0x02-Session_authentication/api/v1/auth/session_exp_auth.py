#!/usr/bin/env python3
""" Script for creating an expiration date for the
authenticated system """
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """ Class for Expiration date Authtication system """
    def __init__(self):
        """ Method for initializing an instance """
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except Exception as e:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Method for creating session ID """
        if not (session_id := super().create_session(user_id)):
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Instance method for returning session id for user id """
        if session_id:
            if session := self.user_id_by_session_id.get(session_id):
                if self.session_duration <= 0:
                    return session.get("user_id")
                if session.get("created_at"):
                    created_at = session.get("created_at")
                    time = created_at + timedelta(
                        seconds=self.session_duration
                    )
                    if time < datetime.now():
                        return None
                    return session.get("user_id")
        return None
