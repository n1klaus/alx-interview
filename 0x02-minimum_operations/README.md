# Minimum Operations
 
# Problem
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

Prototype: `def minOperations(n)`
Returns an integer
If n is impossible to achieve, return 0

Example:

n = 9

H => `Copy All` => `Paste` => HH => `Paste` =>HHH => `Copy All` => `Paste` => HHHHHH => `Paste` => HHHHHHHHH

Number of operations: 6

# [Solution](./0-minoperations.py)

### Requirements:
1. Provide confirmation if possible to achieve n
2. Return an integer that represents the smallest number of operations to achieve smallest number of copy operations of n number of H

1 - 0 (0)
2 - 2 (C, P)
3 - 3 (C, P, P)
4 - 4 (C, P, C, P)
5 - 5 (C, P, P, P, P)
6 - 5 (C, P, P, C, P)
7 - 7 (C, P, P, P, P, P, P)
8 - 6 (C, P, C, P, P, P)
9 - 6 (C, P, P, C, P, P)
10 - 7 (C, P, P, P, P, C, P)
12 - 7 (C, P, P, C, P, P, P)
18 - 9 (C, P, P, C, P, P, P, P, P)
20 - 9 (C, P, P, P, P, C, P, P, P)

### Procedure using divisors of n:
1. If `n` <= 1 return 0 as it does not require any new operation
2. If `n` == 2 return 2 for copying and pasting just the single character once
3. Find `p` - the smallest sum of its divisors `x` and `y` if `n` is not a prime number
	which are also prime numbers (cannot be subdivided further) where:
		-> `p` equals to the minimum number of operations to achieve `n`
		-> `x` equals the smallest divisor of `n` and `x` > 1 where you require minimum `x` `copyAll`
			and `Paste` operations of the single character to give `n` characters
		-> `y` equals the minimum number of operations to repeat `x` in order to achieve`n`
			achieved by recursively getting a new `p` for every subdivision of `y`
6. return `p`

Time complexity => O(log(n))
Space complexity => O(log(n))
