# Minimum Operations
 
# Problem

# Solution

### Requirements:
1. Provide confirmation if possible to achieve n
2. Return an integer that represents the smallest number of operations

1 - 0 (0)
2 - 2 (C, P)
3 - 3 (C, P, P)
4 - 4 (C, P, P, P)
5 - 5 (C, P, P, P, P)
6 - 6 (C, P, P, C, P)
7 - 7 (C, P, P, P, P, P, P)
8 - 6 (C, P, C, P, P, P)
9 - 6 (C, P, P, C, P, P)
10 - 7 (C, P, P, P, P, C, P)
12 - 7 (C, P, P, C, P, P, P)
18 - 9 (C, P, P, C, P, P, P, P, P)
20 - 9 (C, P, P, P, P, C, P, P, P)

### Procedure:
1. If n <= 1 return 0 as it does not require any new operation
2. If n == 2 return 2 for copying and pasting the new character
3. Find `p` - the largest divisor of `n` which is a prime number (cannot be divided further) where:
		-> `p` equals to the maximum number of unique times `n` can be divided
		-> `p` * `x` equals `n` and `x` >= 1
4. Check if result of `p` * `x` equals `n` number of characters and return 0 if failed
5. Calculate and return `p` + `x` if `p` != n where
		-> `p` == 1 copyAll operation of the single character +
				  `p` - 1 paste operations of the single character to provide the maximim number of unique operations for n characters
		-> `x` == 1 copyAll of the `p` characters + 
				  `x` - 1 operations to paste the group of `p` characters resulting in `n` number of characters
6. Otherwise return `n` where:
		-> `n` == 1 copyAll operation of the single character +
				  `n` - 1 paste operations of the single character to provide the maximim number of unique operations for n characters
 
