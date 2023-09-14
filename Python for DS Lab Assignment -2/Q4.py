#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:    Given this nested dictionary grab the word "hello".
#              d = {'k1':[1,2,3,{'tricky':['oh','man','inception',
#             {'target':[1,2,3,'hello']}]}]}
#
#
# Question no. : 4
# Assignment:   2
#
#-------------------------------------------------------------------------------


def dict_indexing():
    d = {'k1':[1,2,3,{'tricky':['oh','man','inception',
    {'target':[1,2,3,'hello']}]}]}
    print(d ["k1"][3]["tricky"][3]["target"][3])

dict_indexing()