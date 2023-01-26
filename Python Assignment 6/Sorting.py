#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python function that accepts a hyphen-separated sequence
#             of words as input and prints the words in a hyphen-separated
#             sequence after sorting them alphabetically.
#             Sample Items : green-red-yellow-black-white
#             Expected Result : black-green-red-white-yellow
# Question No. : 5
# Created:     20-01-2023
#-------------------------------------------------------------------------------


print("Enter words separated by Hyphens : ")
list = [word for word in input().split("-")]
list.sort()
print('-'.join(list))