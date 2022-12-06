#!/usr/bin/python3

def multiple_returns(sentence):
    count = len(sentence)
    if count > 0:
        first_char = sentence[0]
    else:
        return ('None')

    sentence_tuple = count, first_char
    return sentence_tuple


if __name__ == "__main__":
    multiple_returns()
