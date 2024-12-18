#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set is a valid UTF-8 encoding.
    """
    def byte_num(num):
        """
        Determine the number of bytes needed to represent a given number.
        """
        byte_parse = 1 << (8 - 1)
        i = 0
        while num & byte_parse:
            byte_parse >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        j = byte_num(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = byte_num(data[i])
            if cur != 1:
                return False
            i += 1
    return True
