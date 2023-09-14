
#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question: Create a function that counts the number of times the word "dog"
#           occurs in a string.
# Question no. : 7
# Assignment:   2
#
#-------------------------------------------------------------------------------

def count_dogs():
    input_str = ("Enter a string to check how many dog is in it:")
    if "dog" or "Dog" not in input_str:
        print("No 'dog' or 'Dog' found")
        return
    count = input_str.count( "dog" or "Dog")
    print("Found" , count, "number of dogs")

count_dogs()