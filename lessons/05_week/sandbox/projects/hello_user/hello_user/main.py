#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console

import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(first: str = "", middle: str = "", last: str = ""):
    """Say hello to the person having a name of first, middle and last name"""
    console = Console()
    console.print("Hello to;")
    console.print(f"   first = {first}")
    console.print(f"   middle = {middle}")
    console.print(f"   last = {last}")


# end of main()
