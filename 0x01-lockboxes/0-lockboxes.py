#!/usr/bin/python3
"""
Interview questions: Lockboxes
"""


def canUnlockAll(boxes):
    """
    Function checks if all lockboxes have keys
    """
    # Set to keep track of unlocked boxes
    unlocked_boxes = set()
    # List to keep track of keys we have
    keys = [0]

    while keys:
        key = keys.pop()
        if key not in unlocked_boxes:
            unlocked_boxes.add(key)
            # Add all keys found in the current box to the keys list
            keys.extend(boxes[key])

    # Check if we have unlocked all boxes
    return len(unlocked_boxes) == len(boxes)
