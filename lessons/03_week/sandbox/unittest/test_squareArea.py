#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.case import _AssertRaisesContext

from squareArea import squareArea

class TestSquareArea(unittest.TestCase):
    def test_area(self):
        """ check that the correct area is computed"""
        # test areas when radius >= 0
        self.assertAlmostEqual(squareArea(1), 1)
        self.assertAlmostEqual(squareArea(0), 0)
        self.assertAlmostEqual(squareArea(2.1), 2.1**2)
    # end of test_area() 

    def test_values(self):
        """
        Test to determine whether we are handling improper imputs?
        we make sure that values errors are raised as necessary. 
        For example, when negative numbers are entered."
        """
        self.assertRaises(ValueError, squareArea, -2)
        # note, since this test fails for -2 values, we add 
        # an exception handler to code
    #end of test_values()

    def test_types(self):
        """
        Test for strings or booleans.
        """
        self.assertRaises(TypeError, squareArea, "radius")
        self.assertRaises(TypeError, squareArea, 2+5j)
        self.assertRaises(TypeError, squareArea, True)
        # end of test_strings()

# run: python3 -m unittest test_squareArea.py
# run: python3 -m unittest # using test discovery