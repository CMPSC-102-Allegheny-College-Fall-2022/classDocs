#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rich.console import Console
import typer
""" A program to create a sequence of numbber palindromes """

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(upperbounds: str = ""):
    """Driver function. Upperbounds is how high we go to create palendromes"""
    for i in infinite_sequence():
        pal = is_palindrome(i)
        if pal:
            # print(f"\t {count}, {pal}")
            print(f"{pal}")


# end of main()


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:  # return an int, not a float
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


# end of is_palindrome()


def infinite_sequence() -> None:
    """Infinite_sequence will eventually stop at an upperbounds"""
    num = 0
    count = 0
    while True:
        yield num
        num += 1


# end of infinite_sequence()
