#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python function that checks whether a passed string is
#             palindrome or not. Note: A palindrome is a word, phrase, or
#             sequence that reads the same backward as forward,e.g., madam
#             or nurses run.
# Question No. : 2
# Created:     20-01-2023
#-------------------------------------------------------------------------------

x = "malayalam"

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")
