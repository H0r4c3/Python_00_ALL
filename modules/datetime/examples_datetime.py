'''
Created on Oct 3, 2020

@author: Horace.000
'''

#Import the classes from the standard module "datetime"
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today()
print("Today is: ", today)

#Date components
print("Date components: ", today.year, today.month, today.day)

#Retriev today's weekday (0=Monday, 6=Sunday)
print("Today is weekday nr. ", today.weekday())

#Using the datetime class
now = datetime.now()
print("Now, date and time are: ", now)
print("Now, the time is: ", datetime.time(now))

#Formatting
#%Y for year 4 digits, %y for year 2 digits
print(now.strftime("The current year is: %Y"))

#Formatting date (%A for weekday - 4 digits, %d for the day of the month, %B for month - 4 digits, %y for year)
print(now.strftime("%A, %d %B, %Y"))

#Formatting time ("%I, %M, %S, %p)
print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("24h-time: %H:%M"))

#Using timedelta
print("One year and 2 hours from now will be: ", now + timedelta(days=365, hours=2))

#Calculate the number of days till a special date
special_date = date(year = 2020, month = 12, day = 31)
print("Till the special date, there are", special_date - today, " days left")

