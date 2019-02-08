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
    '''Determines whether the year is a leap year based on first leap year of 1752'''
    if year < 1752:
        return False
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4 == 0:
        return True


def get_days_per_month(year,month):
    '''returns 29 for Feb if leap year'''
    if is_leap_year(year):
        days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month-1]


def is_valid_date(year,month,day):
    '''checks if the input date is valid based on the gregorian calendar start 1582'''
    if year < 1582:
        return False
    if year == 1582:
        if month < 10:
            return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > get_days_per_month(year,month):
        return False
    return True


def is_date_before(year1,month1,day1,year2,month2,day2):
    '''checks whether the first date is before the second date'''
    if year1<year2:
        return True
    if year1 == year2:
        if month1<month2:
            return True
        if month1 == month2:
            return day1<day2
    return False


def get_days_between_dates(year1,month1,day1,year2,month2,day2):
    '''Main method that returns the number of days passed'''
    days = 0

    assert is_valid_date(year1,month1,day1)
    assert is_valid_date(year2,month2,day2)
    assert is_date_before(year1,month1,day1,year2,month2,day2)

    while is_date_before(year1,month1,day1,year2,month2,day2):
        year1,month1,day1 = get_next_day(year1,month1,day1) ##TODO write get_next_day function
        days += 1
    return days


