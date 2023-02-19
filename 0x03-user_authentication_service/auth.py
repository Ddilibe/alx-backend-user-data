#!/usr/bin/env python3
""" Script that encourages authentication """
from db import DB
from user import User
import bcrypt


def _hash_password(password: str) -> bcrypt.hashpw:
	"""
		Function that takes in a string and returns bytes
		Args:
			:params: @password - string first argument
		Return:
			Returns bytes
	"""
	return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
    	"""
    		Method that registers a user object
    		Args:
    			:params: @email - Email of the to be registered user
    			:params: @password - Password of the to registered user
    		Return:
    			Returns a user object
    	"""
    	new_user = {
    		"email": email,
    		"password": password
    	}
    	try:
    		self._db.find_user_by(**new_user)
    	except Exception as e:
    		new_password = _hash_password(password)
    		user = self._db.add_user(email, password)
    		return user
    	info = "User {} already exists".format(email)
    	raise ValueError(info)
