#!/usr/bin/python3

def uppercase(str):
    res = list(str)
    for i in range(len(res)):
        if (ord(res[i]) > 96 and ord(res[i]) < 123):
            res[i] = chr(ord(res[i]) - 32)
    print("{}".format("".join(res)))
