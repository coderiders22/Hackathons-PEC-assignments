#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 10: Write a program that takes an integer as an input and generates
#              its binary equivalent.
#
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------

n=int(input())
bin=0
list1=[]
while(n>0):
    list1.append(n%2)
    n=int(n/2)
for i in reversed(list1):
    bin=bin*10+i
print(bin)

