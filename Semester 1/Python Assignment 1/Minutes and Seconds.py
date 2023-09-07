#-------------------------------------------------------------------------------
# Name:    Manav Rai
# Branch:  Computer Science Engineering (Data Science)
# Purpose: Write a program that asks the user for a number of seconds and prints
#           out how many minutes and seconds that is. For instance, 200 seconds
#           is 3 minutes and 20 seconds. [Hint: Use the //operator to get minutes
#           and the % operator to get seconds.]
# Question Number -: 3
#
# Created:     30-11-2022
#-------------------------------------------------------------------------------

x = int(input("enter number of seconds"))
a = x//60
b = x%60
print(a, "minutes",b,"seconds")