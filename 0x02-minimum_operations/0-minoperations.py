#!/usr/bin/python3
"""Calculates minimum possible operations on a text file"""

def prime_divisor(n: int) -> int:
	"""
	Args:
		n (int): number to check
	Returns:
		d (int): the largest prime divisor of n
	"""
	d = 2
	divisors = []
	isPrime = True

	while d < (n // 2) + 1:
		if n % d == 0:
			isPrime = False
			divisors.append(d)
		d += 1

	if isPrime:
		return n

	non_primes = []
	for i in range(len(divisors)):
		for k in range(2, divisors[-1] + 1):
			if k != divisors[i] and divisors[i] % k == 0:
				non_primes.append(divisors[i])
	
	if len(non_primes) > 1:
		j = divisors.index(non_primes[0]) - 1
		return divisors[j]
	return divisors[-1]

def minOperations(n: int) -> int:
	"""
	Args:
		n (int): desired final number of characters
	Returns:
		x (int): the minimum possible `Copy All` and `Paste` operations
			 on  asingle character `H` in  a text file
	"""
	if n <= 1:
		return 0
	elif n == 2:
		return 2
	else:
		p = prime_divisor(n)
		if p == n:
			return n
		return p + (n // p)
