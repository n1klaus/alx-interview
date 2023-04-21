#!/usr/bin/python3
"""Check UTF-8 validation"""


def validUTF8(data) -> bool:
    """Checks if a given dataset represents a valid UTF-8 encoding"""
    try:
        if not data:
            return False
        for code_point in data:
            _binary = bin(code_point).replace("b", "")
            _hex = hex(code_point)
            # uses 1 byte (6 bits)
            if 0x0000 <= int(_hex, 16) < 0x007F:
                if _binary[0] != "0" or len(_binary) > 8:
                    return False
            # uses 2 bytes (6 bits, 6 bits)
            elif 0x0080 <= int(_hex, 16) < 0x07FF:
                if (_binary[0] != "1" or _binary[1] != "1") or \
                    (_binary[9] != "1" or _binary[10] != "0") or \
                        len(_binary) > 16:
                    return False
            # uses 3 bytes (6 bits, 6 bits, 6 bits)
            elif 0x0800 <= int(_hex, 16) < 0xFFFF:
                if (_binary[0] != "1" or _binary[1] != "1" or
                    _binary[2] != "1") or \
                    (_binary[9] != "1" or _binary[10] != "0") or \
                    (_binary[17] != "1" or _binary[18] != "0") or \
                        len(_binary) > 24:
                    return False
            # uses 4 bytes (6 bits, 6 bits, 6 bits, 6 bits)
            elif 0x10000 <= int(_hex, 16) < 0x10FFFF:
                if (_binary[0] != "1" or _binary[1] != "1" or
                    _binary[2] != "1" or _binary[3] != "1") or \
                    (_binary[9] != "1" or _binary[10] != "0") or \
                    (_binary[17] != "1" or _binary[18] != "0") or \
                    (_binary[25] != "1" or _binary[26] != "0") or \
                        len(_binary) > 36:
                    return False
        return True
    except BaseException:
        raise
