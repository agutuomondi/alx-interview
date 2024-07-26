#!/usr/bin/python3

import sys


def print_statistics(total_file_size, status_codes):
    """
    Print metrics including total file size and status code counts.
    """
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line):


    parts = line.split()  # split line into components
    # check if parts matches the expected format
    if len(parts) >= 7:
        file_size_str = parts[-1]
        code_str = parts[-2]
        # check if the status code(code_str) is in the allowed list
        # of strings (status_codes)
        if code_str in status_codes:
            try:
                # convert file_size to integer or try to, lol
                file_size = int(file_size_str)
                return file_size, code_str
            except ValueError:
                # Handle case where file size is not an integer
                return None, None
    return None, None


# initialize variables to store metrics
total_file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

line_count = 0

try:
    # loop over each line in stdin
    for line in sys.stdin:
        # increment line count to track when to print statistics
        line_count += 1
        file_size, code = parse_line(line)

        if file_size is not None and code in status_codes:
            total_file_size += file_size
            status_codes[code] += 1

        if line_count % 10 == 0:
            print_statistics(total_file_size, status_codes)
            line_count = 0

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_statistics(total_file_size, status_codes)
    sys.exit(0)

finally:
    # Ensure statistics are printed at the end of input
    print_statistics(total_file_size, status_codes)
