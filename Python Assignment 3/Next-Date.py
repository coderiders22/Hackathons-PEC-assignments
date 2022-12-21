#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a python script to print next date of input date. It must
#             meet following conditions(use if-elif)
#             C1:1<=month<=12
#             C2:1<=day<=31
#             C3:1800<=year<=2025
#             E.g.:
#                  Input: Day - 28
#                  Month -02
#                  Year -1999
#                  Output: Next Date is: 1/03/1999
#
# Question No. : 2
#
# Created:     11-12-2022
#-------------------------------------------------------------------------------


date = int(input("Enter date: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

oddMonths = [1, 3, 5, 7, 8, 10, 12]

if date >= 1 and month >= 1 and year >= 1800:
    if date <= 31 and month <= 12 and year <= 2025:
        date += 1

if date > 28 and month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        date = 1
        month += 1

if date > 29 and month == 2:
    date = 1
    month += 1

elif date > 30 and oddMonths.index(month) is not int:
    date = 1
    month += 1

elif date > 31:
    date = 1
    month += 1
    if month == 12:
        date = 1
        month = 1
        year += 1

print("Next date is: ", date, "/", month, "/", year)