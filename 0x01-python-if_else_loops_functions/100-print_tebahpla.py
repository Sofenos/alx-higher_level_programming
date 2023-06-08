#!/usr/bin/python3
def print_tebahpla():
    for i in range(ord('z'), ord('A') - 1, -1):
        print("{}".format(chr(i) if i % 2 == 0 else chr(i).lower()), end='')
print_tebahpla()
print("")
