#!/usr/bin/env python3
""" Script that handles all routes for the session
Authentication """
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=True)
def auth_session_login() -> str:
	""" POST /auth_session/login
	Handles auth session login
	"""
	email = request.form.get('email')
	if not email:
		return jsonify({"error": "email missing"}), 400
	password = request.form.get('password')
	if not password:
		return jsonify({"error": "password missing"}), 400
	user = User.search({"email": email})
	if not user:
		return jsonify({
			"error": "no user found for this email"
		}), 404
	for i in user:
		if i.is_valid_password(password):
			from api.v1.app import auth
			sesid = auth.create_session(i.id)
			users = jsonify(i.to_json())
			sesna = os.getenv("SESSION_NAME")
			users.set_cookie(sesna, sesid)
			return users
		return jsonify({"error": "wrong password"}), 401
@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=True)
def session_logout():
	""" Logout Function
	"""
	from api.v1.app import auth
	if auth.destroy_session(request):
		return jsonify({}), 200
	abort(404)
	return False
