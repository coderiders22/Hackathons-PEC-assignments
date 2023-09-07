#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:      CSE(Data Science)
# SID :        22106028
#
# Question 5: Write a program to input a string of numbers separated by a
#             space “ “. Generate a list of numbers from this string and
#             sort the list using selection sort.
#
#
# Created:     01-09-2023
#-------------------------------------------------------------------------------


s=input()
list1=s.split()
list2=[]
for i in list1:
    list2.append(int(i))
sorted_list=[]
while(len(list2)>0):
    next=list2[0]
    for i in list2:
        next=min(next,i)
    list2.remove(next)
    sorted_list.append(next)

print(sorted_list)