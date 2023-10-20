#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question: Create a function that grabs the email website domain from a string
#            in the form: user@domain.com
#
#
# Question no. : 5
# Assignment:   2
# Created :   14-09-23
#-------------------------------------------------------------------------------

def domain_extraction():
    input_email = input("Enter an email id:")
    domain = input_email.split(sep="@")[1]
    print(domain)

domain_extraction()