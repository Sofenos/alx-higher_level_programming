#!/usr/bin/python3
def print_tebahpla():
    for i in range(ord('z'), ord('a') - 1, -1):
        if i % 2 == 0:
            print("{}".format(chr(i).upper()), end='')
        else:
            print("{}".format(chr(i)), end='')
print_tebahpla()
print("")
