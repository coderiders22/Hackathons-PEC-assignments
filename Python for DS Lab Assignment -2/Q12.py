#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:  Add item 7000 after 6000 in the following Python List
#            list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Question no. : 12
# Assignment:   2
# Created :   14-09-23
#-------------------------------------------------------------------------------

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]


nested_list = list1[2][2]

nested_list.append(7000)

print(list1)
