#!/usr/bin/python3
"""
determines if all the boxes can be opened.box is unlocked.
"""


def canUnlockAll(boxes):
    """
    returns True if all boxes can be opened, else return False
    """
    n = len(boxes)
    opened = set([0])
    unopened = set(boxes[0]).difference(set([0]))
    while len(unopened) > 0:
        box_index = unopened.pop()
        if not box_index or box_index >= n or box_index < 0:
            continue
        if box_index not in opened:
            unopened = unopened.union(boxes[box_index])
            opened.add(box_index)
    return n == len(opened)
