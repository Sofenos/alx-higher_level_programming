#!/usr/bin/python3
def print_tebahpla():
    for i in range(ord('z'), ord('A') - 1, -1):
        if i % 2 == 0:
            print('{}'.format(chr(i)), end='')
        else:
            print('{}'.format(chr(i).lower()), end='')
print_tebahpla()
print("")
