#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python function to check whether a number is perfect or
#             not. According to Wikipedia : In number theory, a perfect number
#              is a positive integer that is equal to the sum of its proper
#              positive divisors, that is, the sum of its positive divisors
#              excluding thenumber itself (also known as its aliquot sum).
#              Equivalently, a perfect number is a number that is half the sum
#              of all of its positive divisors (including itself).
# Question No. : 1
# Created:     20-01-2023
#-------------------------------------------------------------------------------


n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")