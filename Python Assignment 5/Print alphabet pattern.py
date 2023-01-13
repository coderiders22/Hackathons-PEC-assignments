#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a python program to print a triangular pattern of the
#              alphabet (user input the number of rows) Example: Input the
#              number of rows = 5, then the pattern should come out as given below.
#              If the count of the alphabet gets exhausted, repeat the alphabet
#              from A.
#              A
#              BC
#              DEF
#              GHIJ
#              KLMNO
#
#
# Question No. : 5
# Created:     11-01-2023
#-------------------------------------------------------------------------------

rows = int(input("Enter number of rows to be input:"))

count = 0

for i in range(0, rows):
    for j in range(0, i + 1):
        if (count >= 26):
            count = 0
        print(chr(65 + count), end = '')
        count += 1
    print("")









