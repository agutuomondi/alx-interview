#!/usr/bin/python3

import sys

""" Python script that reads stdin line by line and computes metrics:
  - Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
  - After every 10 lines and/or a keyboard interruption (CTRL + C),
  print these statistics from the beginning:
    - Total file size: File size for all previous lines
    - Status codes: Status codes from all previous lines in ascending order
"""


def print_msg(dict_sc, total_file_size):

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


            total_file_size = 0
code = 0
counter = 0
dict_sc  {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (counter == 10):
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)
