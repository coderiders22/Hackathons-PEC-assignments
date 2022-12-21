#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Given the sets below, write python statement to:
#             Set1= {1, 2, 3, 4, 5}
#             Set2= {2, 4, 6, 8}
#             Set3= {1, 5, 9, 13, 17}
#             a. Create a new set of all elements that are in Set1 and Set2 but
#                  not both.
#             b. Create a new set of all elements that are in only one of the
#                three sets Set1, Set2 and Set3.
#             c. Create a new set of elements that are exactly two of the sets
#                Set1, Set2 and Set3.
#             d. Create a new set of all integers in the range 1 to 10 that are
#                 not in Set1.
#              e. Create a new set of all integers in the range 1 to 10 that are
#                 not in Set1,Set2 and Set3.
#
# Question No. : 8
# Created:     11-12-2022
#-------------------------------------------------------------------------------


set1 = set([1, 2, 3, 4, 5])
set2 = set([2, 4, 6, 8])
set3 = set([1, 5, 9, 13, 17])

print(set1.intersection(set2))

print(set1.intersection(set2.intersection(set3)))

print(set1.intersection(set2).union(set2.intersection(set3).union(set3.intersection(set1))))

print(set([1,2,3,4,5,6,7,8,9,10]).difference(set1))

print(set([1,2,3,4,5,6,7,8,9,10]).difference(set1.union(set2.union(set3))))