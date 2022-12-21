#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python program to create a list of tuples with the first
#             element as the number and Second element as the square of the
#             number.
#             E.g. list = [3, 9, 10]
#             Output: [(3, 9), (9, 81), (10, 100)]
#
# Question No. : 3
# Created:     11-12-2022
#-------------------------------------------------------------------------------


list_of_numbers = [3, 9, 10]

list_of_tuples = [""] * len(list_of_numbers)

for i in range(0, len(list_of_numbers)):
    list_of_tuples[i] = "(" + str(list_of_numbers[i]) + "," + \
        str(list_of_numbers[i] * list_of_numbers[i]) + ")"

print(list_of_tuples)