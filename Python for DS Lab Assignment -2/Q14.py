#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:  Check if a value 200 exists in a dictionary
#            d1 = {'a': 100, 'b': 200, 'c': 300}
# Question no. : 14
# Assignment:   2
# Created :   14-09-23
#-------------------------------------------------------------------------------

def check_dict_val():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    if list(d1.values()).count(200) != -1:
        print("200 exists in the dictionary")

check_dict_val()
