'https://www.geeksforgeeks.org/python-datetime-timedelta-class/'

'''
Timedelta class is used for calculating differences between dates and represents a duration. The difference can both be positive as well as negative.

Syntax:

class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
'''

from datetime import datetime, timedelta
  
# Creating datetime objects
date1 = datetime(2020, 1, 3)
date2 = datetime(2020, 2, 3)
  
# Difference between dates
diff = date2 - date1
print("Difference in dates:", diff)
print("Difference in days:", diff.days)
  
# Adding days to date1
date1 += timedelta(days = 4)
print("date1 after 4 days:", date1)
  
# Subtracting days from date1
date1 -= timedelta(15)
print("date1 before 15 days:", date1)