#!/usr/bin/python3
'''Defines a function write_file'''

def write_file(filename="", text=""):
    '''Writes a string to a text file

    Returns: Number of characters written
    '''

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)

'''
    with open(filename, encoding='utf-8') as f:
        while True:
            line = f.readline()

            if not line:
                break

            wordlist = line.split()

            # counting the characters
            c = 0
            for word in wordlist:
                for c in word:
                    c += 1
                print(c)
'''
