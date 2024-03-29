#!/usr/bin/python3
"""Log Parsing"""

import re
from sys import stdout, stdin, exit

_IP = r"(((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4})"
_YEAR = r"(20([0-1]\d|2[0-3])"
_DATE = _YEAR + r"\-(0|1)\d\-[0-3]\d\s+(2[0-3]|1\d|\d)(:[0-5]\d){2}\.\d{6})"
_STATUS_CODE = r"(200|301|400|401|403|404|405|500)"
_FILE_SIZE = r"(10([0-2][0-4]|[0-1]\d)|[1-9]\d{1,2}|[1-9])"
_REQUEST = r"\"GET\s+\/projects\/260\s+HTTP\/1.1\""
PTTN = r"{0}\s+\-\s+\[{1}\]\s+{2}\s+{3}\s+{4}" \
    .format(_IP, _DATE, _REQUEST, _STATUS_CODE, _FILE_SIZE)


def print_stats(file_size: int, status_codes: dict) -> None:
    """Print statistics from provided input arguments"""
    stdout.write("File size: {0}\n".format(file_size))
    [
        stdout.write("{0}: {1}\n".format(code, status_codes[code]))
        for code in sorted(status_codes)
        if status_codes.get(code, 0) > 0
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
        500: 0
    }

    try:
        for stream in stdin:
            line = str(stream.rstrip())
            if not line or len(list(line.split())) < 2:
                continue
            # Get the file size and status code from the line
            try:
                file_size += int(list(line.split())[-1])
                status_code = int(list(line.split())[-2])
            except BaseException:
                continue
            # If status code is valid update the count
            if status_code in status_codes.keys():
                count = status_codes.get(status_code, 0)
                count += 1
                status_codes.update({status_code: count})
            line_count += 1
            # Confirm all other requirements are met
            if re.fullmatch(PTTN, line) is None:
                continue
            # Print after reading every 10 lines
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        EXIT_CODE = 1
    finally:
        print_stats(file_size, status_codes)
        exit(EXIT_CODE)
