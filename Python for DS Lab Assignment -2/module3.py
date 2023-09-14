#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:    Given this nested list, use indexing to grab the word "hello"
#              lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
#
#
# Question no. : 3
# Assignment:   2
#
#-------------------------------------------------------------------------------


def list_indexing():
    lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
    print(lst[3][1][2][0])

list_indexing