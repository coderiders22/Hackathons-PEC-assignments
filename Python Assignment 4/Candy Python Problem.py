#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    A jar of Halloween candy contains an unknown amount of candy
#             you win all the candy. You ask the person in charge the following:
#             If the candy is divided evenly among 5 people,how many pieces
#             would be left over? The answer is 2 pieces. You then ask about
#             dividing the candy evenly among 6 people, and the amount
#             left over is 3 pieces. Finally, you ask about dividing the candy
#             evenly among 7 people, and the amount left over is 2 pieces.
#             By looking at the bowl, you can tell that there are less than
#             200 pieces. Write a program to determine how many pieces are
#             in the bowl .
# Question No. : 4
# Created:     04-01-2023
#-------------------------------------------------------------------------------

x=200

for i in range(x):

    if i % 5 == 2:
       if i % 6 == 3:
          if i % 7 == 2:
             print(i, 'candies are in the bowl!')

