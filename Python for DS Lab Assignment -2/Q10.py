#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:  Concatenate two lists index-wise
#            list1 = ["M", "na", "i", "She"]
#           list2 = ["y", "me", "s", "lly"]
#          Expected Outcome: ['My', 'name', 'is', 'Shelly']
# Question no. : 10
# Assignment:   2
#
#-------------------------------------------------------------------------------

list1 = ["M", "na", "i", "She"]
list2 = ["y", "me", "s", "lly"]

result = [x + y for x, y in zip(list1, list2)]

print(result)
