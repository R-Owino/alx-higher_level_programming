#!/usr/bin/python3

import os


def print_to_stdout(*a):
    print(*a, file=sys.stdout)


if __name__ == "__main__":
    print_to_stdout('#pythoniscool')
