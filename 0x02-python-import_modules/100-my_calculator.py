#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    argc = len(argv)
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    result = ops[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))
