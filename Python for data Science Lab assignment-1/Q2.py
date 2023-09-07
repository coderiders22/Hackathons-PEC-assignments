#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 2: Write a program that takes two lists as an input and appends them.
#             The second list could either be a single number or a list of
#             numbers.
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------

s=input()
list1=s.split()
s=input()
list2=s.split()
print(list1)
print(list2)
for i in list2:
    list1.append(i)

print(list1)