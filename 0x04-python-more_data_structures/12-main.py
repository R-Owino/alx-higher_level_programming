#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "I"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "III"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 45
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
