'https://data-flair.training/blogs/python-calendar-module/'

'''
class calendar.Calendar(firstweekday=0)

This creates a Calendar object with whichever day of the week we want it to begin at. By default, it starts at Monday with a parameter value of 0.

Like we said earlier, Sunday is 6. With the methods of this class, we prepare a calendar for formatting.

An instance of Calendar will have the following methods:
'''


# monthdatescalendar(year,month) – List of weeks in month 
# 
# This gives us a list of full weeks in the month we want. Each week is a list of seven datetime.date objects.

from calendar import Calendar
firstweekday = 0
year = 2020
month = 2
my_month = Calendar(firstweekday=firstweekday).monthdatescalendar(year, month)
for week in my_month:
    print(week)

my_day_nr = my_month[0][0].day
print(my_day_nr)