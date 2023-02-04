# Lockboxes

# Problem
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False

# Solution
Requirements:
- move non-sequentially when opening a box given a key number (near instant access)
- record opened boxes
- record used and working keys
- handle used keys which have already opened a box (prevent loop when two boxes have keys to each other)
- check if all boxes have been opened and return the status

Procedure:
1. Define a class to hold records for properties including keys in a box, box number and if it has been visited
2. Create two sets to reduce duplicates, one for holding collected keys and another for holding used keys
3. Create a list of box instances to allow instant access using indexing and reading properties from box instances from
   the boxes argument since they are already sequentially sorted
4. Run a loop to allow movement from one box to another trying out the keys and updating the used and working keys
4. Compare used keys list with total number of boxes and return true if a match else return false

# Time Complexity
O(n)

# Space complexity
O(n)
