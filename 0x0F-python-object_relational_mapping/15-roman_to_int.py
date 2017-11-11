#!/usr/bin/python3
'''module: 15-roman_to_int
'''

def roman_to_int(roman_string):
	'''function: roman_to_int
	accepts: string representation of roman number (all uppercase) (1 - 3,999)
	returns: an int
	'''
	roms = {"M":0 , "D":1, "C":2, "L":3, "X":4, "V":5, "I":6}
	ints = [1000, 500, 100, 50, 10, 5, 1]

	total = 0

	for roman_char in roman_string:
		total += ints[roms[roman_char]]

	return total
		

