#!/usr/bin/python3

# returns value of each roman symbol
def value(roman_symbol):
    if roman_symbol == 'I':
        return 1
    if roman_symbol == 'V':
        return 5
    if roman_symbol == 'X':
        return 10
    if roman_symbol == 'L':
        return 50
    if roman_symbol == 'C':
        return 100
    if roman_symbol == 'D':
        return 500
    if roman_symbol == 'M':
        return 1000
    return 0


def roman_to_int(roman_string):
    res = 0
    i = 0

    while (i < len(roman_string)):
        # getting value of symbol roman_string[i]
        s1 = value(roman_string[i])

        if (i + 1 < len(roman_string)):
            s2 = value(roman_string[i + 1])

            if s1 >= s2:
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res
