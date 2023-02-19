#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method for adding a user to the database """
        new_user = User(email=email, hashed_password=hashed_password)
        if not self.__session:
            self._session
        self.__session.add(new_user)
        self.__session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Method used to find user by the keyword arguments """
        userall = self.__session.query(User).all()
        for key, value in kwargs.items():
            if key not in User.__table__.columns:
                raise InvalidRequestError
            for i in userall:
                if getattr(i, key) == value:
                    return i
        raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Method for updating user instance """
        variable = {"id": user_id}
        old_user = self.find_user_by(**variable)
        string = update(User)
        string = string.values(**kwargs)
        string = string.where(old_user.id == user_id)
        self.__session.execute(string)
