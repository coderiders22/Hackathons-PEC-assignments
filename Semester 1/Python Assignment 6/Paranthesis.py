#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python class to find validity of a string of parentheses,
#             '(', ')', '{', '}', '[' and ']. These brackets must be close in the
#             correct order, for example "()" and "()[]{}" are valid but "[)",
#             "({[)]" and "{{{" are invalid.
# Question No. : 9
# Created:     20-01-2023
#-------------------------------------------------------------------------------


class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))
