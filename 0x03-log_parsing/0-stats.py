#!/usr/bin/python3
"""Log Parsing"""

import re
from sys import stdout, stdin, exit

_IP = r"(((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4})"
_YEAR = r"(20([0-1]\d|2[0-3])"
_DATE = _YEAR + r"\-(0|1)\d\-[0-3]\d\s+(2[0-3]|1\d|\d)(:[0-5]\d){2}\.\d{6})"
_STATUS_CODE = r"(200|301|400|401|403|404|405|500)"
_FILE_SIZE = r"(10([0-2][0-4]|[0-1]\d)|[1-9]\d{1,2}|[1-9])"
_PROJECT = r"\"GET\s+\/projects\/260\s+HTTP\/1.1\""
PTTN = r"{0}\s+\-\s+\[{1}\]\s+{2}\s+{3}\s+{4}" \
    .format(_IP, _DATE, _PROJECT, _STATUS_CODE, _FILE_SIZE)


def print_stats(file_size: int, status_codes: dict) -> None:
    """Print statistics from provided input arguments"""
    stdout.write("File size: {0}\n".format(file_size))
    [
        stdout.write("{0}: {1}\n".format(status_code, count))
        for status_code, count in status_codes.items()
    ]


if __name__ == "__main__":
    EXIT_CODE = 0
    line_count = 0
    file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}

    try:
        for stream in stdin:
            # while True:
            line = str(stream.rstrip())
            # print(line)
            if not line:
                break
            # print(re.fullmatch(PTTN, line))
            if re.fullmatch(PTTN, line) is None:
                continue
            file_size += int(list(line.split())[-1])
            status_code = int(list(line.split())[-2])
            if status_code in status_codes.keys():
                count = status_codes.get(status_code, 0)
                count += 1
                status_codes.update({status_code: count})
            line_count += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        # stdout.write("KeyboardInterrupt | EOFError Error\n")
        print_stats(file_size, status_codes)
        EXIT_CODE = 2
    finally:
        exit(EXIT_CODE)
