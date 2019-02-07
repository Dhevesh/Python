#-------------------------------------------------------------------------------
# Name:        AgeCalculator
# Purpose:
#
# Author:      Dhevesh
#
# Created:     07/02/2019
# Copyright:   (c) Dhevesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

##This module takes in 2 date ranges and determines the number of days that have
##passed between them.
##It takes into account leap years.
#-------------------------------------------------------------------------------

def is_leap_year(year):
    '''Determines whether the year is a leap year'''
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4 == 0:
        return True

print is_leap_year(1996)

def get_days_per_month(year,month):
    '''returns 29 for Feb if leap year'''
    if is_leap_year(year):
        days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month

def is_date_before(year1,month1,day1,year2,month2,day2):
    '''checks whether the first date is before the second date'''
    if year1<year2:
        return True
    if yaer1 == year2:
        if month1<month2:
            return True
        if month1 == month2:
            return day1<day2
    return False



def get_days_between_dates(year1,month1,day1,year2,month2,day2):
    '''Main method that returns the number of days passed'''
    days = 0
    return days

