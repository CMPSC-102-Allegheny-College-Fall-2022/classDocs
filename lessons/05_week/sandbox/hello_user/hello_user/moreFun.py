#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console


def giveMoreFun(myText: str) -> None:
    """ Function to send an extra part of the greeting"""
    # create a console for rich text output
    console = Console()
    console.print(f"\n\t This is the giveMoreFun() function sending a huge hello to : {myText}")
# end of giveMoreFun()
