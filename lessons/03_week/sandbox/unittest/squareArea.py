#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Function with exceptions

# def squareArea(s: float ) -> float: 
#     """
#     Function to calculate the area of square
#     with input (s). Exceptions are handled
#     """
#     if type(s) not in [int, float]:
#         raise TypeError("\tSides must be a number.")
#     if s < 0:
#         raise ValueError("\tSides cannot be negative numbers.")
#     return s*s # area of square is s*s
# # end of squareArea()


# Function without exceptions

def squareArea(s: float ) -> float:
    """
    Function to calculate the area of square
    with input (s). No exceptions are handled
    """
    return s*s # area of square is s*s
# end of squareArea()



def main(in_str):
    # passes
    sideLength = 5
    print(f"Length {sideLength}, Area: {squareArea(sideLength)}")

    # does not pass since some values are not ints or floats
    testValues_list =[2,0,-3,2 + 5j, True, "radius"]
    for val in testValues_list:
        print(f"Length: {val}, Area: {squareArea(val)}")

# end main()

import sys
if __name__ == '__main__':
	main(sys.argv[1:])

# to run the tests, we need to comment out this line.
#main() 
