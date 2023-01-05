#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a multiplication game program for kids. The program should
#              give the player ten randomly generated multiplication questions
#              to do. After each, the program should tell them whether they got
#              it right or wrong and what the correct answer is.
#             Question 1: 3 x 4 = 12
#                Right!
#             Question 2: 8 x 6 = 44
#                Wrong. The answer is 48.
#             ...
#             ...
#              Question 10: 7 x 7 = 49
#                Right.
# Question No. : 3
# Created:     11-12-2022
#-------------------------------------------------------------------------------

import random

i, correct_answers = 0, 0

while (i < 10):
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)

    print(number1, " * ", number2, " = ?")

    multiplication_answer = int(input())

    if (multiplication_answer == (number1 * number2)):
        print("Your answer is correct.")
        correct_answers += 1
    else:
        print("The answer is incorrect.")

    i += 1

print("The game is over! You scored: ", correct_answers, " / 10")
