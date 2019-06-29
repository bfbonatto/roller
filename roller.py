"""
This script is an arbitrary dice calculator
usage is to give any math expression
'1d20 + 5', '1d4 - 1' etc
"""

from random import randint
from sys import argv

atoms = argv[1:]

def roll(dice):
	n, d = dice.split('d')
	return str(sum([randint(1, int(d)) for _ in range(int(n))]))

def flatten(ss):
	ac = ""
	for s in ss:
		ac += s
	return ac

print(eval( flatten([ a if a.isnumeric() or a in ['+', '-', '*', '/'] else roll(a) for a in atoms ]) ))
