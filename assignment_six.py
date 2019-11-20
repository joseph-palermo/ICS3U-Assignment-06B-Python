#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program calculates the volume of an icosahedron

import math


def volume():
    # This function calculates the volume of an icosahedron

    # input
    sl_string = input("Enter side length of the icosahedron: ")

    # process and output
    try:
        sl = float(sl_string)

        volume = (5*(3+math.sqrt(5))/12)*sl**3

        # output
        print("")
        print("The volume of the icosahedron is {:,.2f} units"
              .format(volume))

    except ValueError:
        print("")
        print("Please insert a valid number.")


def main():
    # this function calls other functions

    # call function
    volume()


if __name__ == "__main__":
    main()
