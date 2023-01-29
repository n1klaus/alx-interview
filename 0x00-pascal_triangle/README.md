[Pascal's triangle solution](./0-pascal_triangle.py)

# Problem
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer


# Solution
For every row in a pascal's triangle if the index is not the first or the last which is universally 1, the value is calculated by adding the previous row (if exists) value in current index position with value in index -1 position.
Hence for that specific range you have to iterate through the list and add the values

``` bash
1. Create empty array: triangle
2. if n == 0 return the empty array triangle 
3. for row in range 0 to last index n - 1 add values to inner array: my_array
    1. append 1 in first index
    2. if n == 1 return only one item
    3. else for range index 1 to second last index n - 2 \
        check if there is a previous row, \
        if it exists add value at current index i and previous index i - 1 \
        and insert value to my_array
    4. append 1 in last index
    5. add inner array my_array in triangle
    6. go to the next row
4. return final array triangle
```