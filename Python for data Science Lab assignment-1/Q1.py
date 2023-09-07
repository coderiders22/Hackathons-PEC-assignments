#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 1: Write a program that asks the user to input marks of three
#              subjects and computes the average for it. The average should
#              then be compared 40, and the output display should be Pass/Fail
#             depending upon whether the marks are greater/lesser than 40.
#
#
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------


a = int(input())
b = int(input())
c = int(input())
avg= (a+b+c)/3
print("The average is ",avg)
print(["fail","pass"] [avg>=40])



