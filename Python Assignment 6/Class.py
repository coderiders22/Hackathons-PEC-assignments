#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a Python program to create two empty classes, Student and
#             Marks. Now create some instances and check whether they are
#             instances of the said classes or not. Also, check whether the
#             said classes are subclasses of the built-in object class or not.
# Question No. : 7
# Created:     20-01-2023
#-------------------------------------------------------------------------------


def student_list(_sid, _name, _class, student_id = False, student_name = False, student_class = False):
    if student_id:
        print(_sid)
    if student_name:
        print(_name)
    if student_class:
        print(_class)

student_list(22106028, "MANAV RAI", "CSE DS", student_id = True)
student_list(22106028, "MANAV RAI", "CSE DS", student_name = True)
student_list(22106028, "MANAV RAI", "CSE DS", student_class = True)