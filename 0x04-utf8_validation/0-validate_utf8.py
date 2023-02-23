#!/usr/bin/python3
"""Check UTF-8 validation"""

from typing import Any, List


def validUTF8(data: List[Any]) -> bool:
    """Checks if a given dataset represents a valid UTF-8 encoding"""
    for i in data:
        v = hex(i)
        # print(f"{i} => {v}")
        if v > "0xFF":
            return False
    return True
