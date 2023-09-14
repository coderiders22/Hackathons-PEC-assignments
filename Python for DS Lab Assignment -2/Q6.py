#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question: Create a basic function that returns True if the word 'dog' is
#           contained in the input string.
#
# Question no. : 6
# Assignment:   2
#
#-------------------------------------------------------------------------------

def dog():
    if "dog" or "Dog" in input("Enter a string to check if dog is in it:"):
            print("True")
            return True
    else:
        print("False")
        return False

dog()