"""
Usage:
	python3 basic.py roll1 roll2 ...
	gives the sum of every roll
"""

from random import randint
from sys import argv

if len(argv) == 1:
	print(randint(1, 20))
else:
	args = argv[1:]

	total = 0

	for dice in args:
		print(dice, end=':\n')
		subtotal = 0
		n, d = dice.split('d')
		number, size = int(n), int(d)
		for _ in range(number):
			result = randint(1, size)
			print(f"	{result}")
			subtotal += result
		print(f"subtotal = {subtotal}")
		print(10*'-')
		total += subtotal

	print(f"TOTAL = {total}")
