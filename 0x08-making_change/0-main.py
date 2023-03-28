#!/usr/bin/python3
"""
Main file for testing
"""

from random import randint


makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

coins = [
        randint(1, 100),
        randint(1, 100),
        randint(1, 100),
        randint(1, 100),
        randint(1, 100)
    ]

print(makeChange(coins, randint(15, 100)))
