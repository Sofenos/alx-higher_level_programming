#!/usr/bin/python3
def uppercase(string):
    uppercase_str = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        uppercase_str += uppercase_char
    print(uppercase_str)
