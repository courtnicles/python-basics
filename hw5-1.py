"""
DATA 200 Fall 2019 Homework 5
Courtney Nguyen
18OCT19
hw5-1.py

"""

import calendar
from datetime import *

def find_thanksgiving(year):
    thanks = calendar.monthcalendar(year, 11) ## calender of november for any input year
    d = date(year, 11, 1)

    thanks_week = thanks[0] ## week 1
    ## if week 1 does not contain a Thurs, the fourth Thurs is in week 5
    thanks_week2 = thanks[4]

    ## check if there is a thurs is week 1, if yes then week 4 contains the 4th thurs
    if thanks_week[calendar.THURSDAY]:
        thanks_week4 = thanks[3]
        thanks_day = thanks_week4[calendar.THURSDAY]
    else:
        thanks_day = thanks_week2[calendar.THURSDAY]

    print(f'November {thanks_day}, {year}')

    ## Assignment was to return the result as Date Object
    date_obj = d.replace(day=thanks_day)
    print(date_obj)
    print(type(date_obj))
    print()

## loop to call years between 2010 and 2020
for i in range(2010, 2021):
    find_thanksgiving(i)