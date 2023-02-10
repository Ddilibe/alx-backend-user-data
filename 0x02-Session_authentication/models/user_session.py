#!/usr/bin/env python3
""" Script containing the new user session models """
from models.base import Base


class UserSession(Base):
	""" Class for the new usersession """
	def __init__(self, *args: list, **kwargs: dict):
		""" Initialization class for user sessions """
		super().__init__(*args, **kwargs)
		self.user_id: str = kwargs.get("user_id")
		self.session_id: str = kwargs.get("session_id")
