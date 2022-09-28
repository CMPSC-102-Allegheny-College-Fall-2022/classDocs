#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console


def giveMoreFun(myText: str) -> None:
    """ Function to send an extra part of the greeting"""
    # create a console for rich text output
    console = Console()
    console.print(f"Sending more fun from giveMoreFun(): {myText}")
# end of giveMoreFun()
