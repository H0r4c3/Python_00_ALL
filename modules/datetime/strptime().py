'https://www.geeksforgeeks.org/python-datetime-strptime-function/'

'''
strptime() is another method available in datetime which is used to format the time stamp which is in string format to date-time object.

Syntax: datetime.strptime(time_data, format_data)

Parameter:

time_data is the time present in string format
format_data is the data present in datetime format which is converted from time_data using this function.

This function takes two arguments, a string in which some time is given and a format code, 
to change the string into, the string is changed to the DateTime object as per the list of codes given below.

%a	Abbreviated weekday name	Sun, Mon
%A	Full weekday name 	Sunday, Monday
%w	Weekday as decimal number	0…6
%d	Day of the month as a zero-padded decimal	01, 02
%-d	day of the month as decimal number	1, 2..
%b 	Abbreviated month name	Jan, Feb
%m	month as a zero padded decimal number	01, 02
%-m	month as a decimal number	1, 2
%B 	Full month name	January, February
%y	year without century as a zero padded decimal number	99, 00 
%-y	year without century as a decimal number	0, 99
%Y	year with century as a decimal number	2000, 1999
%H	hour(24 hour clock) as a zero padded decimal number	01, 23
%-H	hour(24 hour clock) as a decimal number	1, 23
%I	hour(12 hour clock) as a zero padded decimal number	01, 12
%-I	hour(12 hour clock) as a decimal number	1, 12
%p	locale’s AM or PM	AM, PM
%M	Minute as a zero padded decimal number	01, 59
%-M	Minute as a decimal number	1, 59
%S	Second as a zero padded decimal number	01, 59
%-S	Second as a decimal number	1, 59
%f	microsecond as a decimal number, zero padded on the left side	000000, 999999
%z	UTC offset in the form +HHMM or -HHMM	 
%Z	Time zone name	 
%j	day of the year as a zero padded decimal number	001, 365
%-j	day of the year as a decimal number	1, 365
%U	Week number of the year (Sunday being the first)	0, 6
%W	Week number of the year	00, 53
%c	locale’s appropriate date and time representation	Mon Sep 30 07:06:05 2013
%x	locale’s appropriate date representation	11/30/98
%X	locale’s appropriate time representation	10:03:43
%%	A literal ‘%’ character	%
'''

# import datetime module from datetime
from datetime import datetime
 
# consider the time stamp in string format
# DD/MM/YY H:M:S.micros
time_data = "25/05/99 02:35:5.523"
 
# format the string in the given format :
# day/month/year hours/minutes/seconds-micro
# seconds
format_data = "%d/%m/%y %H:%M:%S.%f"
 
# Using strptime with datetime we will format string into datetime
date = datetime.strptime(time_data, format_data)
print(date)
 
# display mili second
print(date.microsecond)
 
# display hour
print(date.hour)
 
# display minute
print(date.minute)
 
# display second
print(date.second)
 
# display date
print(date)