#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 6: Write a program which takes email IDs of n students and stores in
#              a tuple. Two new tuples are to be created from it- first one
#              having the user names of the email IDs and the second one having the domain names only. The
#              the domain names only. Thefinal output should display all three
#              tuples.
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------

print("Enter the number of students")
n=int(input())
list1=[]
username=[]
domains=[]
for i in range (0,n):
    s=input()
    list2=s.split('@')
    username.append(list2[0])
    domains.append(list2[1])

print(username)
print(domains)