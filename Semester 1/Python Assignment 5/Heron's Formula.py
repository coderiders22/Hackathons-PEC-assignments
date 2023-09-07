#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Program to calculate the area of a triangle using heron’s formula.
#              (check condition if the combination of sides is possible)
# Question No. : 3
# Created:     11-01-2023
#-------------------------------------------------------------------------------


import math

side_a = eval(input("Enter the first side of the triangle:"))
side_b = eval(input("Enter the second side of the triangle:"))
side_c = eval(input("Enter the third side of the triangle:"))

triangle_exists = False

if (side_a + side_b) > side_c:
    if(side_b + side_c) > side_a:
        if(side_a + side_c) > side_b:
            triangle_exists = True

if triangle_exists:
    semiperimeter = (side_a + side_b + side_c) / 2

    area = math.sqrt(semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c))

    print("Area of triangle is:", area)

else:
    print("Triangle does not exist!")