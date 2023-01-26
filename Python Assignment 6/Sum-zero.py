#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python class to find the three elements that sum to zero
#             from a set of n real numbers.
#             Input array: [-25, -10, -7, -3, 2, 4, 8, 10]
#              Output: [[-10, 2, 8], [-7, -3, 10]]
# Question No. : 8
# Created:     20-01-2023
#-------------------------------------------------------------------------------


input_array = [-25, -10, -7, -3, 2, 4, 8, 10]

class set_of_number:

    def __init__(self, _input_array):
        output_array = []

        for i in _input_array:
            for j in _input_array:
                for k in _input_array:
                    if i + j + k == 0:
                        _ijklist = [i, j, k]
                        output_array.append(_ijklist)

        print(output_array)


set1 = set_of_number(input_array)
