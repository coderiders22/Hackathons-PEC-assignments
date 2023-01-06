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


if month in oddMonths:
    if month == 12 and date == 31:
        date = 1
        month = 1
        year += 1
    else:
        if date < 31:
            date += 1
        elif date == 31:
            date = 1
            month += 1

elif month not in oddMonths:

    if month != 2:
        if date == 30:
            date = 1
            month += 1
        elif date < 30:
            date += 1

    elif month == 2:
        
        if date < 28:
            date += 1

        elif date >= 28:

            leap_year = False
        
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        leap_year = True
                    else:
                        leap_year = False
                else:
                    leap_year = True
            else:
                leap_year = False

            if leap_year:
                if date == 29:
                    date = 1
                    month += 1
        
            elif not leap_year:
                if date == 28:
                    date = 1
                    month += 1


print("Next date is: ", date, "/", month, "/", year)