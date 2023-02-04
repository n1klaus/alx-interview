#!/usr/bin/python3
"""
Algoritms to check if a number of locked boxed can all be opened
given each box numbered sequenctially from 0 to n - 1 and each box may
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
    my_boxes = [Box(index, boxes[index]) for index in range(len(boxes))]
    boxNum = 0
    my_keys = set()
    used_keys = set()
    while True:
        if boxNum not in used_keys:
            curr_box = my_boxes[boxNum]
            my_keys.update(curr_box.keys)
            curr_box.visited = True
            used_keys.add(boxNum)
        if boxNum in my_keys and boxNum in used_keys:
            my_keys.discard(boxNum)
        if len(my_keys) == 0:
            break
        boxNum = next(iter(my_keys))
    visited_boxes = filter(
                    lambda x: x.visited is True,
                    my_boxes
                    )
    [print((b.index, b.keys, b.visited)) for b in visited_boxes]
    return True if len(used_keys) == len(my_boxes) else False
