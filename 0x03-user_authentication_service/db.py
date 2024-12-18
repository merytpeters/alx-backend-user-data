#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

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
        """Add User"""
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise ValueError('Email and password required.')
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """takes in arbitrary keyword arguments and returns the first row
        found in the users table as filtered by the method's input arguments
        """
        if not kwargs:
            raise InvalidRequestError("Invalid")
        try:
            query = self._session.query(User).filter_by(**kwargs)
            user = query.one()
            return user
        except NoResultFound:
            raise NoResultFound("Not found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Uses find_user_by method to locate user to update"""
        try:
            user = self.find_user_by(id=user_id)

            for attr, value in kwargs.items():
                if hasattr(user, attr):
                    setattr(user, attr, value)
                else:
                    raise ValueError(f"Invalid attribute: {attr}")

            self._session.commit()

        except NoResultFound:
            raise ValueError(f"User with id {user_id} not found.")
        except InvalidRequestError as e:
            raise ValueError(f"Invalid request: {e}")
        except Exception as e:
            raise ValueError(f"An error occurred: {e}")
