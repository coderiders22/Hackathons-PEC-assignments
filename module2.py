#-------------------------------------------------------------------------------
# Name:    Manav Rai
# Branch:  Computer Science Engineering (Data Science)
# Purpose: Write a Python programme to compute a person's income tax.
#           Assume following tax laws:
#           . All taxpayers are charged a flat tax rate of 20%
#          . All taxpayers are allowed to $10,000 standard deduction
#           . Gross income must be entered to the nearest penny.
#           . Gross Income and the number of dependents must be asked from
#             the user.
#             .Hint:
#            Taxable income = GrossIncome - Standard deduction -
#            (Dependent deduction* No. of dependents)
#            .Tax = Taxable Income * Tax Rate
#
# Question Number -: 2
#
# Created:     30-11-2022
#-------------------------------------------------------------------------------

x = float(input("Please enter your gross index"))
y = float(input("Please enter your no. of dependents"))
print("flat tax amount",x/5)
print("standard deduction $10000")
print("additional tax due to number of dependents",3000*y)
print("Total taxable income",x-10000-(3000*y))
