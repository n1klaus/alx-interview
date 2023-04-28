#!/usr/bin/python3
"""Check UTF-8 validation"""


def valid_byte(byte, number):
    """Checks if the number of bytes provided meet the UTF8 binary format"""

    if number == 1:
        # check the 1 byte ([0xxxxxxx] 7 bits)
        if len(byte) > 8 or \
                (len(byte) == 8 and byte[0] != 0):
            return False
    elif number == 2:
        # check the 2 bytes ( [110xxxxx 10xxxxxx] 5 bits , 6 bits)
        if (len(byte) == 8 and byte[0] != "1") \
            or \
            (8 < len(byte) < 16 and (byte[0] != "1" or byte[1] != "1")) \
            or \
            (len(byte) == 16 and
             (byte[0] != "1" or byte[1] != "1") and
             (byte[8] != "1" or byte[9] != "0")):
            return False
    elif number == 3:
        # check the 3 bytes (4 bits, 6 bits, 6 bits)
        # ([1110xxxx 10xxxxxx 10xxxxxx])
        if (len(byte) == 16 and (byte[0] != "1" or byte[1] != "1")) \
            or \
            (16 < len(byte) < 24 and
             (byte[0] != "1" or byte[1] != "1" or byte[2] != "1")) \
            or \
            (len(byte) == 24 and
             (byte[0] != "1" or byte[1] != "1" or byte[2] != "1") or
             (byte[8] != "1" or byte[9] != "0") or
             (byte[16] != "1" or byte[17] != "0")):
            return False
    elif number == 4:
        # check the 4 bytes (3 bits, 6 bits, 6 bits, 6 bits)
        # ([11110xxx 10xxxxxx 10xxxxxx 10xxxxxx])
        if (len(byte) == 24 and
            (byte[0] != "1" or byte[1] != "1" or byte[2] != "1")) \
            or \
            (24 < len(byte) < 36 and
             (byte[0] != "1" or byte[1] != "1" or
             byte[2] != "1" or byte[3] != "1")) \
            or \
            (len(byte) == 36 and
             (byte[0] != "1" or byte[1] != "1" or
              byte[2] != "1" or byte[3] != "1") or
             (byte[8] != "1" or byte[9] != "0") or
             (byte[16] != "1" or byte[17] != "0") or
             (byte[24] != "1" or byte[25] != "0")):
            return False
    return True


def validUTF8(data):
    """Checks if a given dataset represents a valid UTF-8 encoding"""
    if data is None:
        return True

    for code_point in data:
        _binary = bin(code_point).removeprefix("0b")
        # uses 1 byte ([0xxxxxxx] 7 bits)
        if 0x0000 <= code_point <= 0x007F and not valid_byte(_binary, 1):
            return False
        # uses 2 bytes ([110xxxxx 10xxxxxx] 5 bits , 6 bits)
        elif 0x0080 <= code_point <= 0x07FF and not valid_byte(_binary, 2):
            return False
        # uses 3 bytes (4 bits, 6 bits, 6 bits)
        # ([1110xxxx 10xxxxxx 10xxxxxx])
        elif 0x0800 <= code_point <= 0xFFFF and not valid_byte(_binary, 3):
            return False
        # uses 4 bytes (3 bits, 6 bits, 6 bits, 6 bits)
        # ([11110xxx 10xxxxxx 10xxxxxx 10xxxxxx])
        elif 0x10000 <= code_point <= 0x10FFFF and not valid_byte(_binary, 4):
            return False
    return True
