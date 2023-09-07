#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python function to check whether a string is a
#             pangram or not. Note: Pangrams are words or sentences containing
#             every letter of the alphabet at least once.
#             For example: "The quick brown fox jumps over the lazy dog"
# Question No. : 4
# Created:     20-01-2023
#-------------------------------------------------------------------------------


import string

def ispangram(sentence, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(sentence.lower())

print(ispangram(input('Sentence: ')))
