#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 3: Write a program with a function that inputs a string and the
#              output has to be a new string with first letter of every word
#              capitalized. For instance, if the sentence is “Hello how are
#              you." the output should be “Hello How Are You"
#
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------

s=input()
list1=s.split()
s=""
for i in list1:
    t=chr(ord(i[0])-ord('a')+ord('A'))
    s+=t+i[1:]+" "

print(s)
