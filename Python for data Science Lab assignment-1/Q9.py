#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 9: Write a program in python that takes a string as input to setup a
#             password. Your entered password must meet the following
#             requirements:
#              The password must be at least five characters long.
#              It must contain the symbol “&”.
#              It must contain at least one uppercase and one lowercase letter.
#
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------

s=input()
ampersand=0
upper=0
lower=0
for i in s:
    if('a'<=i<='z' or 'A'<=i<='Z'):
        if('a'<=i<='z'):
            lower+=1
        else:
            upper+=1
    elif(i=='&'):
        ampersand+=1
if(len(s)<5):
    print("password must contain at least 5 character")
if(ampersand<1):
    print("password must contain at least one '&' character")
if(upper<1):
    print("password must contain at least 1 uppercase letter")
if(lower<1):
    print("password must contain at least 1 lowercase letter")
