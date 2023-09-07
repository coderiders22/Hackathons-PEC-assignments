#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    A school has following rules for grading system:
#             a. Below 25 - F
#             b. 25 to 45 - E
#             c. 45 to 50 - D
#             d. 50 to 60 - C
#             e. 60 to 80 - B
#             f. Above 80 - A
#            Ask user to enter marks and print the corresponding grade.
#
# Question No. : 1
# Created:     04-01-2023
#-------------------------------------------------------------------------------


x=int(input("enter marks"))
if(x<25):
    print(" Grade F")
elif(x<45):
    print(" Grade E")
elif(x<50):
    print(" Grade D")
elif(x<60):
    print(" Grade C")
elif(x<80):
    print(" Grade B")
elif(x>=80):   #else:
    print(" Grade A")