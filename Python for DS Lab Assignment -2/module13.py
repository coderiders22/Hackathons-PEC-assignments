#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:  Given a Python list, remove all occurrence of 20 from the list
#            list1 = [5, 20, 15, 20, 25, 50, 20]
# Question no. : 13
# Assignment:   2
#
#-------------------------------------------------------------------------------


list1 = [5, 20, 15, 20, 25, 50, 20]
result = [x for x in list1 if x != 20]

print(result)
