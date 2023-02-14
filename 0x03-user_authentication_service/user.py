#!/usr/bin/env python3
""" Script containing the user class model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """
        Class for User models

        Class Args:
            :params: @id, the integer primary key
            :params: @email, a non-nullable string
            :params: @hashed_password, a non-nullable string
            :params: @session_id, a nullable string
            :params: @reset_token, a nullable string
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
