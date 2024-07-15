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
        # Get a key from the list of keys we have
        key = keys.pop()
        if key not in unlocked_boxes:
            # Mark the corresponding box as unlocked
            unlocked_boxes.add(key)
            # Add all keys found in this box to our list of keys
            for new_key in boxes[key]:
                if new_key < len(boxes) and new_key not in unlocked_boxes:
                    keys.append(new_key)

    # Check if we've unlocked all boxes
    return len(unlocked_boxes) == len(boxes)
