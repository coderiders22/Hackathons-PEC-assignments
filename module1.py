#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    For a given input string “Python is a case sensitive language”.
#              Write python code for the following:
#
#             a. Find the length of the input string.
#             b. Reverse the order of the string in one line code.
#             c. Using Slice function store “a case sensitive” in new string.
#             d. Replace “a case sensitive” with “object oriented”.
#             e. Find index of substring “a” in the given input string.
#             f. Remove the white spaces from the given input string.
#
# Question No. : 1
#
# Created:     11-12-2022
#-------------------------------------------------------------------------------

given_string = "Python is a case sensitive language"

print("Length of string:", len(given_string))

print("String Reversed:", given_string [::-1])

sliced_string = given_string [slice(10,27)]
print("Sliced String is:", sliced_string)

replaced_string = given_string.replace("a case sensitive", "object oriented")
print("String replaced 'a case sensitive' with 'object oriented' is:", replaced_string)

print("Index of substring 'a':",given_string.index("a"))

removed_whitespaces_string = given_string.replace(" ","")
print("String with removed whitespaces:",removed_whitespaces_string)