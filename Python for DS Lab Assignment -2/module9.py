
#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question: You are driving a little too fast, and a police officer stops you.
#            Write a function to return one of 3 pos sible results: "No Challan",
#           "Small Challan", or "Heavy Challan". If your speed is 60 or less,
#           the result is "No Challan". If speed is between 61 and 80 inclusive,
#           the result is "Small Challan". If speed is 81 or more, the result is
#           "Heavy Challan". Unless it is your birthday (encoded as a Boolean
#           value in the parameters of the function) -- on your birthday, your
#           speed can be 5 higher in all cases.
# Question no. : 9
# Assignment:   2
#
#-------------------------------------------------------------------------------

def caught_speeding(speed,bday):
    if bday:
        n=5
    else:
        n=0
    if speed<=60+n:
        return "No challan"
    elif speed>=61+n and speed<=80+n:
        return "small challan"
    else:
        return "heavy challan"
print(caught_speeding(81,False))