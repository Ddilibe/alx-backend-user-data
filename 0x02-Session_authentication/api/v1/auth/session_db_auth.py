#!/usr/bin/env python3
""" Script containing the class for a new database authentication class """
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
	""" Class for Authtication for database """
	def create_session(self, user_id=None):
		"""Method for creating a session id for a user_id"""
		if session_id := super().create_session(user_id):
			val = {
				"user_id": user_id,
				"session_id": session_id
			}
			user = UserSession(**val)
			user.save()
			return session_id
		return None

	def user_id_for_session_id(self, session_id=None):
		""" Method for returning a user_id based in a session_id """
		if user_id := UserSession.search({
				"session_id": session_id
			}):
			return user_id
		return None

	def destroy_Session(self, request=None):
		""" Method for destroying a UserSession based on a session_id
		from a request cookie """
		if request:
			if session_id := self.session_cookie(request):
				if us := UserSession.search({"session_id": sess}):
					us[0].remove()
					return True
		return False
