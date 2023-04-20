#!/usr/bin/python3
"""Calculates minimum possible operations on a text file"""


def largest_prime_divisor(n: int) -> int:
    """
    Args:
            n (int): number to get its largest prime divisor
    Returns:
            d (int): the largest prime divisor of n
    """
    largest_divisor = 1

    # Use sieve of erastothenes to get all prime numbers less than
    # the largest possible divisor of n which is the sqrt(n)
    # sqrt = int(pow(n, 0.5))
    divisors = [True for _ in range(n + 1)]

    num = 2
    while (num * num) < (n + 1):
        if divisors[num] is True:
            for i in range(num * num, n + 1, num):
                divisors[i] = False
        num += 1

    # Get the largest prime number which is a divisor of n
    num = 2
    while (num * num) < (n + 1):
        if divisors[num] is True and n % num == 0:
            largest_divisor = num
        num += 1
    return largest_divisor


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
        p = largest_prime_divisor(n)
        if p == n:
            return n
        return p + (n // p)
