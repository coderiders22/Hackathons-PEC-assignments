#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Program to reverse the string
#
# Question No. : 1
#
# Created:     11-01-2023
#-------------------------------------------------------------------------------

input_string = str(input("Enter a string:"))

reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print("The reversed string is:", reversed_string)