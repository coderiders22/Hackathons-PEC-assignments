#-------------------------------------------------------------------------------
# Name:    Manav Rai
# Branch:  Computer Science Engineering (Data Science)
# Purpose: Write a program that prints out the sine and cosine of the angles
#           ranging from 0 to 345◦ in 15◦ increments. Each result should be
#           rounded to 4 decimal places.
# Question Number -: 5
#
# Created:     30-11-2022
#-------------------------------------------------------------------------------


#Find sine and cosine of angles in degrees.

import math

for i in range(0, 345, 15):
    sine = round(math.sin(math.radians(i)),4)
    cosine = round(math.cos(math.radians(i)),4)
    print(i, " --- ", sine, cosine)