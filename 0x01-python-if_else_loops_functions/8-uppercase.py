#!/usr/bin/python3
def uppercase(string):
    for c in string:
        if ord('a') <= ord(c) <= ord('z'):
            uppercase_char = chr(ord(c) - ord('a') + ord('A'))
        else:
            uppercase_char = c
        print("{}".format(uppercase_char), end='')
    print()
