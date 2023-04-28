# Rotate 2D Matrix

## Problem
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: `def rotate_2d_matrix(matrix):`
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.

## Requirements
1. Given a list of list of integers, find a way to rotate and modify in-place
2. Create a working copy so that i can reference the original
3. Have row index pointer and column index pointer variables for iterating the matrix

### [Brute-Force Procedure - Calculating rotation movement pattern](./_0-rotate_2d_matrix.py)
- top row moves => right
    - where the right has **column index == len(row) - 1**
    - copying columns from right to left of the current row
      and placing them from bottom row (len(matrix) - 1) to top row (0)
      (**incrementing the row index** when moving from left to right)
- right row moves => bottom
    - where the bottom has **row index == len(matrix) - 1**
    - copying columns from bottom to top of the side
      and placing them from left (0) to right (len(row) - 1)
      (**decrementing the column index** when moving from top to bottom)
- bottom row moves => left
    - where the left has **column index == 0**
    - copying columns from left to right of the row
      and placing them from top row (0) to bottom row (len(matrix) - 1)
      (**incrementing the row index** when moving from left to right)
- left row moves => top
    - where the top has **row index == 0**
    - copying columns from top to bottom of the side
      and placing them from right (len(row) - 1) to left (0)
      (**decrementing the column index** when moving from top to bottom)
- middle rows moves =>
    - to the column index == **(previous used column index - 1)**
    - copying columns from left to right of the row
      and placing them in fitting positions
      (**incrementing the row index** when moving from left to right)
- Therefore to fill values from the first row, first column to the last row, last column =>
    - starting from left (column index 0) until right (column index len(row) - 1)
    - copy column values from bottom row (len(matrix) - 1) to top row (0) of the matrix
      (**decrementing the row index** when copying from left to right in each row)
      and inserting them from left (0) to right (len(row) - 1) in each row
      (**incrementing the column index** when moving from top to bottom)

Space Complexity => O(n)
Time Complexity => O(n)

## Examples
### 2 x 2 Matrix
```
[[1, 2],
 [3, 4]]

-- top => right
0, 0 => 0, 1
0, 1 => 1, 1
-- bottom => left
1, 0 => 0, 0
1, 1 => 1, 0

-- Therefore
1, 0 => 0, 0
0, 0 => 0, 1
1, 1 => 1, 0
0, 1 => 1, 1
```

### 3 x 3 Matrix
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

-- top => right
0, 0 => 0, 2
0, 1 => 1, 2
0, 2 => 2, 2
-- middle => prev_column - 1
1, 0 => 0, 1
1, 1 => 1, 1
1, 2 => 2, 1
-- bottom => left
2, 0 => 0, 0
2, 1 => 1, 0
2, 2 => 2, 0
--

-- Therefore
2, 0 => 0, 0
1, 0 => 0, 1
0, 0 => 0, 2
2, 1 => 1, 0
1, 1 => 1, 1
0, 1 => 1, 2
2, 2 => 2, 0
1, 2 => 2, 1
0, 2 => 2, 2
```

### 4 x 4 Matrix
```
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]]

-- top => right
0, 0 => 0, 3
0, 1 => 1, 3
0, 2 => 2, 3
0, 3 => 3, 3
-- 2nd => prev_column - 1
1, 0 => 0, 2
1, 1 => 1, 2
1, 2 => 2, 2
1, 3 => 3, 2
-- 3rd => prev_column - 1
2, 0 => 0, 1
2, 1 => 1, 1
2, 2 => 2, 1
2, 3 => 3, 1
-- bottom => left
3, 0 => 0, 0
3, 1 => 1, 0
3, 2 => 2, 0
3, 3 => 3, 0

-- Therefore
3, 0 => 0, 0
2, 0 => 0, 1
1, 0 => 0, 2
0, 0 => 0, 3
3, 1 => 1, 0
2, 1 => 1, 1
1, 1 => 1, 2
0, 1 => 1, 3
3, 2 => 2, 0
2, 2 => 2, 1
1, 2 => 2, 2
0, 2 => 2, 3
3, 3 => 3, 0
2, 3 => 3, 1
1, 3 => 3, 2
0, 3 => 3, 3
```

## Requirements
1. Given a list of list of integers, find a way to rotate and modify in-place
2. Use xor bit manipluation to swap values in two different locations
3. Use row index pointer and column index pointer variables for iterating the matrix

### [Transposing the matrix then reversing each row](./0-rotate_2d_matrix.py)
1. Transpose each row r from the first row with column c from the first column in matrix
    - set row_index = 0
    - set col_index = 0
    - Loop each row from col_index until end of row
      - swap the value in current location with its reverse location: matrix[r][c] swaps with matrix[c][r]
    - Continue off in the next row starting from the last value of col_index
2. Reverse each row
    - Iterating each row swap values from left with right until the midpoint:
      - matrix[r][index] swaps with matrix[r][row_size - 1 - index]

Space Complexity => O(1)
Time Complexity => O(n)

### 2 x 2 Matrix
```
[[1, 2],
 [3, 4]]

- Transpose row n with column n
[[1, 3],
 [2, 4]]

- Reverse each row
[[3, 1],
 [4, 2]]

```

### 3 x 3 Matrix
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

- Transpose row n with column n
[[1, 4, 7],
 [2, 5, 8],
 [3, 6, 9]]

- Reverse each row
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

### 4 x 4 Matrix
```
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]]

- Transpose row n with column n
[[1, 5, 9, 13],
 [2, 6, 10, 14],
 [3, 7, 11, 15],
 [4, 8, 12, 16]]

- Reverse each row
[[13, 9, 5, 1],
 [14, 10, 6, 2],
 [15, 11, 7, 3],
 [16, 12, 8, 4]]
```