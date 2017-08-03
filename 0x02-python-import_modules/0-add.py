#!/usr/bin/python3
add = __import__('add_0').add

if __name__ == "main":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
