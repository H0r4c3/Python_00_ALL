'''
Created on Oct 3, 2020

@author: Horace.000
'''
import calendar

#Create a plain text calendar
calen = calendar.TextCalendar(calendar.MONDAY)
calendar_formatted = calen.formatmonth(2020, 1, 0, 0)
calendar_formatted2 = calen.formatmonth(2020, 2, 0, 0)
print(calendar_formatted)
print(calendar_formatted2)

#Calendar for 12 months
cal = calendar.TextCalendar(calendar.MONDAY)
for m in range(1,13):
    print(cal.formatmonth(2020, m, 0, 0))