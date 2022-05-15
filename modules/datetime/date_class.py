
# Python3 program to find number of days between two given dates

from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     
# Driver program
date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(numOfDays(date1, date2), "days")


'https://www.geeksforgeeks.org/weekday-function-of-datetime-date-class-in-python/'

'''
# The weekday() of datetime.date class function is used to return the integer value corresponding to the specified day of the week.

Syntax: weekday()

Parameters: This function does not accept any parameter.

Return values: This function returns the integer mapping corresponding to the specified day of the week. 
Below table shows the integer values corresponding to the day of the week:

Index	Weekday
0	Monday
1	Tuesday
2	Wednesday
3	Thursday
4	Friday
5	Saturday
6	Sunday
'''

import datetime
 
# Specifying some date and time values
dateTimeInstance1 = datetime.datetime(2021, 8, 1, 00, 00, 00)
dateTimeInstance2 = datetime.datetime(2021, 8, 2, 00, 00, 00)
dateTimeInstance3 = datetime.datetime(2021, 8, 3, 00, 00, 00)
 
# Calling the weekday() functions over the
# above dateTimeInstances
dayOfTheWeek1 = dateTimeInstance1.weekday()
dayOfTheWeek2 = dateTimeInstance2.weekday()
dayOfTheWeek3 = dateTimeInstance3.weekday()
 
# Getting the integer value corresponding
# to the specified day of the week
print(dayOfTheWeek1)
print(dayOfTheWeek2)
print(dayOfTheWeek3)