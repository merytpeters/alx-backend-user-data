#!/usr/bin/env python3
"""Log Formatter"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns the log message obsfucated"""
    pattern = '|'.join([re.escape(field) + r'=[^' + re.escape
                        (separator) + r']*' for field in fields])
    return re.sub(r'(' + pattern + r')', lambda m:
                  f"{m.group(0).split('=')[0]}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialization"""
        self.fields = fields
        super().__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Format method"""
        message = super().format(record)
        return filter_datum(
                self.fields, self.REDACTION, message, self.SEPARATOR)


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
