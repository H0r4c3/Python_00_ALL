'https://www.w3schools.com/python/python_datetime.asp'

'''
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.
'''

from datetime import datetime

x = datetime(2020, 5, 17)
print(x)

x = datetime.now()
print(x)


my_date_time = datetime(2015, 1, 12, 10, 0, 10)
print(my_date_time)
print(my_date_time.ctime())


# calculate the delta time, in seconds
dt1 = datetime(2015, 1, 12, 10, 0 , 0)
dt2 = datetime(2015, 1, 12, 10, 10 , 10)
time_delta = (dt2 - dt1).total_seconds()
print(time_delta)


def timeConversion(s):
    s1 = datetime.strptime(s, "%I:%M:%S%p")
    
    return datetime.strftime(s1, "%H:%M:%S")

s = '06:00:00PM'

result = timeConversion(s)
print(result)