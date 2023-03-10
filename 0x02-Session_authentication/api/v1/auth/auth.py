#!/usr/bin/env python3
""" Script containing the API authentication management """
from typing import List, TypeVar
from flask import request
import os


class Auth:
    """
        Class to manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Method for the requirement of authentication
            Args:
                :params: @path[str] - First Argument
                :params: @excluded_paths[List[str]] - Second argument
            Return:
                True - @path is None
                True - if @excluded_path is None
                True - if @path is not in @excluded_path
                False - if @path is in @excluded_path
        """
        if path:
            if excluded_paths or len(excluded_paths) != 0:
                if list(path)[len(list(path))-1] != "/":
                    path = list(path)
                    path.append('/')
                    path = "".join(path)
                if path in excluded_paths:
                    return False
                return True
            return True
        return True

    def authorization_header(self, request=None) -> str:
        """
            Method for authorizing the header
            Args:
                :params: @request[Flask] - Flask Object
            Return:
        """
        if request is None:
            return None
        if request.headers.get("Authorization"):
            return request.headers.get("Authorization")
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Method fir requesting the current User
            Args:
                :params: @request[Flask] - Flask Object
            Return:
        """
        return None

    def session_cookie(self, request=None):
        """
            Method that returns a cookie value from a request
            Args:
                :params: @request[Flask_object] - First
                argument
            Return:
        """
        if request:
            session_name = os.getenv("SESSION_NAME")
            return request.cookies.get(session_name)
        return None
