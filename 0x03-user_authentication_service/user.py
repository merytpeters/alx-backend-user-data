#!/usr/bin/env python3
"""User Authentication"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), default=None)
    reset_token = Column(String(250), default=None)