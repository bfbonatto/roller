"""
This is an advanced version of the roller script,
it functions as an arbitrary dice calculator
but it can also store and use character information in
its calculations
"""

from random import randint

import json

import click

import re

diceMatcher = re.compile('\d\d*d\d\d*')

def toString(tup):
	return ' '.join(list(tup))

def save(char):
	with open(char['name']+'.json', 'w') as f:
		json.dump(char, f)

def load(charName):
	with open(charName+'.json', 'r') as f:
		return json.load(f)

def isDice(dice):
	return diceMatcher.match(dice) is not None

def rollDie(die):
	return randint(1, die)

def rollDice(dice):
	n, d = dice.split('d')
	return sum( [ rollDie(int(d)) for _ in range(int(n)) ] )

def filterDice(expression):
	return " ".join([ str(rollDice(e)) if isDice(e) else e for e in expression.split() ])

def filterAttributes(expression):
	def f(e):
		name, att = e.split('.')
		try:
			char = load(name)
			return char[att]
		except:
			click.echo('invalid character name')

	return " ".join([f(e) if '.' in e else e for e in expression.split()])


@click.group()
def cli():
	pass

@cli.command()
@click.argument('name')
def create(name):
	save({'name': name})

@cli.command()
@click.argument("att")
@click.argument("value", nargs=-1)
def modify(att, value):
	try:
		name, attribute = att.split('.')
		char = load(name)
		char[attribute] = eval(filterDice(filterAttributes(toString(value))))
		save(char)
	except:
		click.echo('error')

@cli.command()
@click.argument("expression", nargs=-1)
def roll(expression):
	click.echo(eval(filterDice(filterAttributes(toString(expression)))))

cli()
