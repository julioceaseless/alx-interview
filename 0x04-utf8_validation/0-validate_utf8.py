#!/usr/bin/env python3
"""
Interview question
"""


def validUTF8(data):
    """
    Checks if the given data set represents a valid UTF-8 encoding.

    :param data: List[int] - A list of integers representing bytes of data.
    :return: bool - True if the data is a valid UTF-8 encoding, else False.
    """

    num_bytes = 0

    # Masks to check the leading bits of a byte
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    # Iterate through each byte in the data
    for byte in data:
        # Create a mask to isolate the most significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            # UTF-8 character should be between 1 and 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
