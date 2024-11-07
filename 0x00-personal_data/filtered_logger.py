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
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, ";")
