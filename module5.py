#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a python program to check if the word “name” is present in
#             the string entered by the user (Print : “Yes” or “No”).
#
# Question No. : 5
#
# Created:     11-12-2022
#-------------------------------------------------------------------------------

input_string = input("Input a string:")

input_name = input("Enter a name:")

if input_name in input_string:
    print("Yes")

else:
    print("No")
