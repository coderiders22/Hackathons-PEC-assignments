#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Sid:         22106028
#
# Question:    Given the variables
#              planet = "Earth"
#              diameter = 12742
#              Use .format() to print the following string:
#              The diameter of Earth is 12742 kilometers.
#
# Question no. : 2
# Assignment:   2
#
#-------------------------------------------------------------------------------

def format_string():
    planet = "Earth"
    diameter = 12742
    output_string = "The diameter of the {planet} is {Diameter} Kilometers"
    print(output_string.format(planet=planet, Diameter=diameter))

format_string()