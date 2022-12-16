#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    For any three lengths, there is a simple test to see if it is
#             possible to form a triangle. If any of the three lengths is
#             greater than the sum of the other two,then you cannot form a
#             triangle. Otherwise, Enter three sides of a triangle,converts them
#             to integers, and to check whether the given input lengths can
#             form a triangle or not (Print : “Yes” or “No”)
#
# Question No. : 6
#
# Created:     11-12-2022
#-------------------------------------------------------------------------------

side_a = eval(input("Enter the first side of the triangle:"))
side_b = eval(input("Enter the second side of the triangle:"))
side_c = eval(input("Enter the third side of the triangle:"))

if(side_a + side_b) > side_c:
    if(side_b + side_c) > side_a:
        if(side_a + side_c) > side_b:
            print("Yes")
        else:
                print("No")
    else:
        print("No")
else:
    print("No")