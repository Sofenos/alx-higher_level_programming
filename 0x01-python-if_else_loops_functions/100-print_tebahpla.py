#!/usr/bin/python3

def print_tebahpla():
    for i in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(i) if i % 2 == 1 else chr(i).upper()), end='')

print_tebahpla()
print("")
