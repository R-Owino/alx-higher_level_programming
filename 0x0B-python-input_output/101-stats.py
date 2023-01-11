#!/usr/bin/python3
'''
Reads fron stdin and computes metrics

After each 10 lines and keyboard interrupts(CTRL+C), print the statistics
since the beginning of the file:
    - total file size
    - Number of lines by status code
'''
import sys


def stats():
    '''
    Prints the statistics from the beginning of the file
    '''

    counter = 0
    size = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for line in sys.stdin:
        line = line.split()
        try:
            size += int(line[-1])
            code = line[-2]
            status_codes[code] += 1
        except (IndexError, ValueError):
            continue
        if counter == 9:
            print("File size: {}".format(size))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            counter = 0
        counter += 1
    if counter < 9:
        print("File size: {}".format(size))
        for key, val in sorted(status_codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    stats()
