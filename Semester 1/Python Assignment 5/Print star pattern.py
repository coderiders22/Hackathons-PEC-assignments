#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python program to construct the following pattern, using a nested for loop.
# Question No. : 4
# Created:     11-01-2023
#-------------------------------------------------------------------------------

for i in range(1,5):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(5,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')