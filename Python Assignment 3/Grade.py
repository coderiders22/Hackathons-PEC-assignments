#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a program to prompt the user for a grade between 4 and 10.
#              If the grade is out of range print error message. If the grade is
#              between 4 and 10 Print the grade and the performance using the
#              following:
#              Letter Grade Performance Grade Points
#                A+ Outstanding 10
#                A Excellent 9
#                B+ Very Good 8
#                B Good 7
#                C+ Average 6
#                C Below Average 5
#                D Poor 4
#
#                E.g.: For Grade 9 Output is:
#                Your Grade is ‘A’ and Excellent Performance.
# Question No. : 4
# Created:     11-12-2022
#-------------------------------------------------------------------------------


grade_input = int(input("Enter a grade from 4 to 10: "))

if grade_input == 4:
    print("Your Grade is 'D' and Poor Performance")

elif grade_input == 5:
    print("Your Grade is 'C' and Below Average Performance")

elif grade_input == 6:
    print("Your Grade is 'C+' and Average Performance")

elif grade_input == 7:
    print("Your Grade is 'B' and Good Performance")

elif grade_input == 8:
    print("Your Grade is 'B+' and Very Good Performance")

elif grade_input == 9:
    print("Your Grade is 'A' and Excellent Performance")

elif grade_input == 10:
    print("Your Grade is 'A+' and Outstanding Performance")

else:
    print("The grade entered is not valid.")
