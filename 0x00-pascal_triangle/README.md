[Pascal's triangle solution](./0-pascal_triangle.py)

# Problem
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

# Solution - Brute Force Approach
For every row in a pascal's triangle for the indices between the first and the last calculate the value to insert by adding the previous row, current column (if exists) value with value in previous row, previous column. Otherwise for first, last and only indexes in a row insert 1

``` bash
1. Create empty array: triangle
2. if n == 0 return the empty array triangle
3. for row in range 0 to last index n - 1 add values to inner array: triangle_row
    1. append 1 in first index
    2. if n == 1 return only the one item
    3. else for range index 1 to second last index n - 2 \
        check if there is a previous row, \
        if it exists add values from current column index i and previous column index i - 1 \
        and append value to triangle_row
    4. append 1 in last index
    5. finally append inner array triangle_row into the triangle
    6. move to the next row
4. return final array triangle
```

Time complexity => O(n ^ 2)
Space complexity => O(n)

# Solution - Using Binomial Coefficient
``` bash
1. create empty array: triangle
2. if n == 0 return the empty array triangle
3. using rows in range 1 to n + 1 add values to inner array: triangle_row
    1. intialize our value, val to insert as 1
    2. using columns in range 1 to row + 1:
        1. Insert the current value: val into triangle_row
        2. calculate the next value using binomial coefficients using the previous val
            => triangle[row: col] = triangle[row: col - 1] * (row - col + 1) // col - 1
            => (val * (row - col + 1) // col - 1)
    3. Insert our triangle_row into the triangle array
4. return the final array triangle
```