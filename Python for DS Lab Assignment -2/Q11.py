#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:  Concatenate two lists in the following order
#            list1 = ["Hello ", "take "]
#            list2 = ["Dear", "Sir"]
#            Expected Output: ['Hello Dear', 'Hello Sir','take Dear','take Sir']
# Question no. : 11
# Assignment:   2
# Created :   14-09-23
#-------------------------------------------------------------------------------

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]

print(result)
