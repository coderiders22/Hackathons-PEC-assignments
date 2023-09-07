#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 7: Write a program that inputs a string and print following
#             information about that string:
#            Number of alphabets
#            Number of digits
#            Number of symbols
#            Number of uppercase alphabets
#            Number of lowercase alphabets
#
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------

s=input()
alphabets=0
digits=0
symbols=0
upper=0
lower=0
for i in s:
    if('a'<=i<='z' or 'A'<=i<='Z'):
        alphabets+=1
        if('a'<=i<='z'):
            lower+=1
        else:
            upper+=1
    elif('0'<=i<='9'):
        digits+=1
    elif(i!=' '):
        symbols+=1

print("alphabets:",alphabets)
print("digits:",digits)
print("symbols:",symbols)
print("upper:",upper)
print("lower:",lower)