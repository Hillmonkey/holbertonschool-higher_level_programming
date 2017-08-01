#!/usr/bin/python3

for i in range(10):
    for j in range(i, 10):
        if j > i:
            print("{:d}{:d}".format(i, j), end='')
            if i * 10 + j == 89:
                print('')
            else:
                print(', ', end='')
