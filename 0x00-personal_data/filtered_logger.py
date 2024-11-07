#!/usr/bin/env python3
"""Regex-ing"""
import re


def filter_datum(
        fields: list[str], redaction: str, message: str, seperator: str
) -> str:
    """Returns the log message obsfucated"""
    pattern = f"({
        '|'.join(re.escape(field) + r'=[^' + re.escape(seperator) + r']*'
                 for field in fields)})"
    return re.sub(
        pattern, lambda m: f"{m.group(1).split('=')[0]}={redaction}", message
    )
