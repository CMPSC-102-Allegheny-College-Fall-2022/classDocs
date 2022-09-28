#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Driver function to demonstrate how to call sciKitDemo.py from main.py """

import sciKitDemo as sd # import another file and refer to it as "sd"


def startAnalysis(myName: str) -> None:
    """ driver function to input a string to print before running another function """
    print(f"Hi {myName}! This is startAnalysis()")
    print(" Welcome to the driver function!")
    sd.main() # run the analysis in thew imported file
# end of startAnalysis()

