#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = -last_digit

print("Last digit of {:d} is {:d} and is ".format(number, last_digit), end='')
if last_digit == 0:
    print('0')
elif last_digit < 6:
    print('less than 6 and not 0')
else:
    print('greater than 5')
