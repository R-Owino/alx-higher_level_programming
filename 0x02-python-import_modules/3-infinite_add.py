#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg = len(argv) - 1

    if arg == 0:
        print('{:d}'.format(arg))
    else:
        result = []

        for i in range(1, arg + 1):
            result.append(int(argv[i]))
        print('{}'.format(sum(result)))
