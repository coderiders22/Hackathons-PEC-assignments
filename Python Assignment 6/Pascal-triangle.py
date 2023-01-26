#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python function that prints out the first n rows of
#             Pascal's triangle. Note:Pascal's triangle is an arithmetic and
#             geometric figure first imagined by Blaise Pascal.
# Question No. : 3
# Created:     20-01-2023
#-------------------------------------------------------------------------------


n = 5

for i in range(n):
    # adjust space
    print(' '*(n-i), end='')

    # compute power of 11
    print(' '.join(map(str, str(11**i))))
