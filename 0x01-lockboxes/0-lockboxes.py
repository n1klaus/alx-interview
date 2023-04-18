#!/usr/bin/python3
"""
Algorithm to check if a number of locked boxed can all be opened
given each box numbered sequentially from 0 to n - 1 and each box may
contain keys to other boxes
"""


class Box:
    """"Class definition for box item"""
    keys = []
    index = None
    visited = False

    def __init__(self, index: int, keys: list) -> None:
        """Initialize a box instance"""
        self.index = index
        self.keys = keys


def canUnlockAll(boxes: list) -> bool:
    """Returns True if all boxes can be opened, otherwise return False"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return None

    # Create our boxes
    my_boxes = [Box(index, boxes[index]) for index in range(len(boxes))]
    # Start with the first opened box
    boxIndex = 0
    # collection of all keys
    usable_keys = set()
    # collection of all used keys
    used_keys = set()
    try:
        while True:
            # Open the box if not already opened as the key matches the box
            curr_box = None
            if boxIndex not in used_keys:
                # Check if the key can be used to open a box
                if boxIndex < len(my_boxes):
                    curr_box = my_boxes[boxIndex]
                # if the key can't open a box discard the key and try another
                # one
                if curr_box is None:
                    usable_keys.discard(boxIndex)
                    boxIndex = next(iter(usable_keys))
                    continue
                # Otherwise add it to our used keys and get all the keys
                # inside the box to add to our usable keys collection
                # while also setting the box as visited
                usable_keys.update(curr_box.keys)
                used_keys.add(boxIndex)
                curr_box.visited = True
            # If key is already added to the used collection
            # remove it from usable keys
            if boxIndex in usable_keys and boxIndex in used_keys:
                usable_keys.discard(boxIndex)
            # if there are no more keys to use
            if len(usable_keys) == 0:
                break
            # otherwise get the next key to try out
            boxIndex = next(iter(usable_keys))
    except StopIteration:
        pass
    # [print((b.index, b.keys, b.visited)) for b in my_boxes]
    return True if len(used_keys) == len(my_boxes) else False
