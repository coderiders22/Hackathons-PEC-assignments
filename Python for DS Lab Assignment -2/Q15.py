#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:  Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# Question no. : 15
# Assignment:   2
# Created :   14-09-23
#-------------------------------------------------------------------------------

def series_sum():
    n = int(input("Enter value of n:"))
    sum = 0
    for i in range(1,n+1):
        for j in range(i):
            sum += 2*(10**j)
            print(sum)
series_sum()
