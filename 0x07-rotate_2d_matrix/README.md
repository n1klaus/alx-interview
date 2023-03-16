# Rotate 2D Matrix

## Problem
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: `def rotate_2d_matrix(matrix):`
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.

## Requirements
1. Given a list of list of integers, find a way to rotate and edit in-place
2. Create a working copy so that i can reference the original
3. Have row index counter and column index counter variables for iterating the matrix

## Procedure
- top row moves => right
    - where the right has **column index == len(row) - 1**
    - copying columns from right to left of the row
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
    - copy column values from bottom (len(matrix) - 1) to top (0) of the matrix
      (**decrementing the row index** when moving from left to right in each row)
      and inserting them from left (0) to right (len(row) - 1) in each row
      (**incrementing the column index** when moving from top to bottom)

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
