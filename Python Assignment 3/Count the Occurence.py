#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python program to count the number of occurrences of each
#             word or character in the string entered by the user. (Count the
#              Number of Occurrences of each character only if the single word
#              is entered by the user).
#
# Question No. : 1
#
# Created:     11-12-2022
#-------------------------------------------------------------------------------

input_string = str(input("Enter a string: "))
if input_string.find(" ") != -1:
    string_to_find = str(input("Enter the string to find: "))
else:
    string_to_find = str(input("Enter a letter to find:"))

print(input_string.count(string_to_find))