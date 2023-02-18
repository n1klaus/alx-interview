#!/usr/bin/python3
"""Log Parsing"""

import re
from sys import stdout, exit

_IP = r"^(((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4})$"
_DATE = r"^(2023\-(0|1)[0-2]-[0-3]\d\s+(2[0-3]|1\d|\d)(:[0-5]\d){2}.\d{6})$"
_STATUS_CODE = r"^(200|301|400|401|403|404|500)$"
_FILE_SIZE = r"^(10[0-2][0-4]|[1-9]\d{1,2}|[1-9])$"
PTTN = r"^({0})\s-\s[({1})]\s\"GET\s/projects/260\sHTTP/1.1\"\s({2})\s({3})$"\
    .format(_IP, _DATE, _STATUS_CODE, _FILE_SIZE)


def print_stats(file_size: int, status_codes: dict) -> None:
    """Print statistics from provided input arguments"""
    stdout.write("File size: {0}\n".format(file_size))
    [stdout.write("{0}: {1}\n".format(s, c)) for s, c in status_codes.items()]


if __name__ == "__main__":
    _STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]
    EXIT_CODE = 0
    line_count = 0
    file_size = 0
    status_codes = {}

    try:
        with open(0, encoding="utf-8",
                  errors="ignore", buffering=1) as stream:
            while True:
                line = str(stream.read().rstrip())
                if not line:
                    break
                if re.fullmatch(PTTN, line) is None:
                    continue
                file_size += int(list(line.split())[-1])
                status_code = int(list(line.split())[-2])
                if status_code in _STATUS_CODES:
                    count = status_codes.get(status_code, 0)
                    count += 1
                    status_codes.update({status_code: count})
                    status_codes.keys().sort()
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(file_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_stats(file_size, status_codes)
        EXIT_CODE = 1
    except BaseException:
        raise
        EXIT_CODE = 2
    finally:
        exit(EXIT_CODE)
