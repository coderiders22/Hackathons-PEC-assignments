#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a python program to print following pattern.
#             ABCDEFGHIJK
#             ABCDEFGHI
#             ABCDEFG
#             ABCDE
#             ABC
#
# Question No. : 5
# Created:     11-12-2022
#-------------------------------------------------------------------------------

input_string = str("ABCDEFGHIJK")

for i in range(0, 6):
    print(" " * i, input_string[0: (11 - (2*i))])



















