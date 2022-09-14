#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Oliver Bonham-Carter
# Date: 12 Sept 2022

def main():
	""" Demo of using quadratic formular to solve ax^2 + bx + c = 0"""
	print("\t Quadratic solver. Enter a, b and c")
	print("Equation: f(x) = a*x^2 + b*x + c = 0")
	prmpt = "Enter a :"
	a_int = input(prmpt)
	prmpt = "Enter b :"
	b_int = input(prmpt)
	prmpt = "Enter c :"
	c_int = input(prmpt)
	print(f"Equation: f(x) = {a_int}*x^2 + {b_int}*x + {c_int} = 0")
	print("\f Finding roots...")
	x1, x2 = quadSolver(a_int,b_int,c_int)
	print(f"\tThe roots are: {x1} and {x2}")
#end of main()


def quadSolver(a,b,c):
	"""function to apply quadratic forumula to find roots"""
	a=int(a)
	b=int(b)
	c=int(c)
	print(f"\tReceived a={a}, b={b}, c={c}")
	D = (b * b - 4 * a * c) ** 0.5 # sqrt of discriminant
	x_one = (-b + D) / (2 * a) # first root
	x_two = (-b - D) / (2 * a) # second root
	return x_one, x_two
# end of quadSolver()



main() # begin the program
