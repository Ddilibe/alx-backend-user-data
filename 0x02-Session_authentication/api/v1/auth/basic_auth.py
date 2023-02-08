#!/usr/bin/env python3
""" Script for basic authentication """
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """ Class for basic authentication """

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """
            Method that extracts authorization header
            Args:
                :params: @authorization_header [str] - First argument
            Return:
        """
        if authorization_header:
            if type(authorization_header) is str:
                authorization_header = authorization_header.split(' ')
                if len(authorization_header) > 1:
                    if authorization_header[0] == "Basic":
                        return authorization_header[1]
        return None

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """
            Method to decode base64 authorization header
            Args:
                :params: base64_authorization_header [str] - First Argument
            Return"
        """
        if base64_authorization_header:
            if type(base64_authorization_header) is str:
                try:
                    base64_authorization = base64_authorization_header.\
                      encode('utf-8')
                    code = base64.b64decode(base64_authorization)
                    return code.decode('utf-8')
                except Exception as e:
                    return None
        return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """
            Method that extracts users credentials
            Args:
                :params: decoded_base64_authorization_header[str]: The first
                argument
            Return:
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                if ":" in decoded_base64_authorization_header:
                    where = decoded_base64_authorization_header.find(":")
                    email = decoded_base64_authorization_header[:where]
                    password = decoded_base64_authorization_header[where+1:]
                    return (
                        email, password
                    )
        return (None, None)

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        """
            Method that returns the users instance based on email and password
            Args:
                :params: @user_email[str] - The users email argument
                :params: @user_pwd[str] - The users password argument
            Return:
                Returns an instance of users
        """
        if user_email and user_pwd:
            unit_user = User.search({"email": user_email})
            if unit_user:
                for i in unit_user:
                    if i.is_valid_password(user_pwd):
                        return i
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Method fir requesting the current User
            Args:
                :params: @request[Flask] - Flask Object
            Return:
        """
        if not request:
            return None
        author = self.authorization_header(request)
        if author:
            author = self.extract_base64_authorization_header(author)
            if author:
                author = self.decode_base64_authorization_header(author)
                if author:
                    author = self.extract_user_credentials(author)
                    if author:
                        author = self.user_object_from_credentials(*author)
                        if author:
                            return author
        return None
