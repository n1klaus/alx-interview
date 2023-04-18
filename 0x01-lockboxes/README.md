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

# [Solution](./0-lockboxes.py)
Requirements:
- move non-sequentially when opening a box given a key number (near instant access)
- record opened boxes
- record used and working keys
- handle used keys which have already opened a box (prevent loop when two boxes have keys to each other)
- handle keys which dont open a box or their box does not exist in our boxes (out of range of our indexes)
- handle when the are no more keys to try out or boxes to open
- check if all boxes have been opened and return the status

Procedure:
1. Define an object class for a class definition to hold records for properties including number of keys in the box, the box number and if it has been visited already
2. Create two sets to reduce duplicates, one for holding collected keys from boxes and another for holding keys already used to open a box
3. Create a list of box instances to allow indexing and reading properties from box instances from
   the provided boxes list argument since they already use indexes
4. Run an iteration to allow movement from one box to another trying out the keys and updating the used and working keys and the collected keys
4. Compare number of used keys with total number of boxes and return true if they are equal else return false
   as all used keys have not opened all the boxes

# Time Complexity
O(n)

# Space complexity
O(n)
