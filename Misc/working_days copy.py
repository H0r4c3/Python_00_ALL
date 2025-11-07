'''Calculate the working days for every month in a year'''

import calendar
import datetime

def get_working_days_in_month(year, month):
    # Get the number of days in the month
    _, num_days = calendar.monthrange(year, month)
    
    # Generate all dates in the month
    days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    
    # Filter out weekends (Saturday and Sunday)
    working_days = [day for day in days if day.weekday() < 5]
    
    return len(working_days)

def working_days_in_current_year():
    current_year = datetime.date.today().year
    working_days = dict()
    
    for month in range(1, 13):
        working_days[calendar.month_name[month]] = get_working_days_in_month(current_year, month)
    
    return working_days

# Calculate working days for every month of the current year
working_days = working_days_in_current_year()

# Print the results
for month, days in working_days.items():
    print(f'{month}: {days} working days')