#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    For a=56 and b=10 with the help of bitwise operators calculate
#             the following:
#             a. a&b
#             b. a|b
#             c. a^b
#             d. Left shift both a and b with 2 bits.
#             e. Right shift a with 2 bits and b with 4 bits
#
# Question No. : 3
#
# Created:     11-12-2022
#-------------------------------------------------------------------------------

a = 56
b = 10

print(a&b)

print(a|b)

print(a^b)

left_shift_a = a<<2
left_shift_b = b<<2
print(left_shift_a, left_shift_b)

right_shift_a = a>>2
right_shift_b = b>>4
print(right_shift_a, right_shift_b)