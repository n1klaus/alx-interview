#!/usr/bin/python3
"""Calculates minimum possible operations on a text file"""


def min_divisor(n: int) -> int:
    """
    Args:
            n (int): number to get the smallest sum of two of its divisors
    Returns:
            (int): the smallest sum from two divisors of n
                     which give n as a product
    """
    divisor = 1
    sqrt = int(pow(n, 0.5))
    # find all the divisors of n from 2 until its square root
    # first find the smallest divisor of n and use its other divisor
    # to recursively get a smaller subdvision of it
    # as a way to minimize the required number of operations needed
    # while adding up all the divisors
    for num in range(2, sqrt + 1):
        if n % num == 0:
            divisor = n // num
            return min_divisor(divisor) + num
    return n


def minOperations(n: int) -> int:
    """
    Args:
            n (int): desired final number of characters
    Returns:
            (int): the minimum possible `Copy All` and `Paste` operations
                     on a single character `H` in  a text file
                     to give n characters
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        return min_divisor(n)
