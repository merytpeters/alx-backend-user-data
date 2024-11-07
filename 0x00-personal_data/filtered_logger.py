#!/usr/bin/env python3
"""Log Formatter"""
import logging
import os
import re
from typing import List
import mysql.connector


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """


    def __init__(self, fields: List[str]):
        """Initialization"""
        self.fields = fields
        super().__init__()

    def format(self, record: logging.LogRecord) -> str:
        """Format method"""
        record.msg = self.filter_datum(record.msg)
        return super().format(record)

    def filter_datum(self, message):
        for field in self.fields:
            message = message.replace(field, "****")
        return message


class StreamHandler(logging.StreamHandler):
    """StreamHandler class"""
    def __init__(self, stream=None):
        """Initialization"""
        super().__init__(stream)
        self.setFormatter(RedactingFormatter(fields=PII_FIELDS))


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Returns a logging.logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = StreamHandler()
    logger.addHandler(handler)
    return logger


def get_db():
    """Get database credentials from environment variables or set defaults"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    if not database:
        return None

    # Connect to the database
    try:
        connection = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
