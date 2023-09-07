#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:     Write a program to count the number of occurrences of each word
#              in the list(List entered by the user).
# Question No. : 9
# Created:     11-01-2023
#-------------------------------------------------------------------------------



input_string = str()

word_list = list()
input_string = str(input(" Enter words |(space separated): "))
for word in input_string.split(" "):
    if (word == ""):
        continue
    word_list.append(word)



word_dict = dict()

print("Number of time each item occurs in list: ")
for j in word_list:
    if j in word_dict:
        word_dict[j] += 1
    if j not in word_dict:
        word_dict[j] = 1

print(word_dict)