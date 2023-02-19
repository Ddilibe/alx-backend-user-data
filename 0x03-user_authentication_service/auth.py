#!/usr/bin/env python3
""" Script that encourages authentication """
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