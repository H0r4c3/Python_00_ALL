'''Calculate the working days for every month in a year'''

import calendar
import datetime

ROMANIAN_HOLIDAYS = {
                    (1, 1): "Anul Nou (New Year's Day)",
                    (1, 2): "A doua zi de Anul Nou (Day after New Year's Day)",
                    (1, 24): "Ziua Unirii Principatelor Române (Union of the Romanian Principalities)",
                    (1, 6): "Epiphany (Boboteaza)",
                    (1, 7): "Saint John the Baptist Day (Sfântul Ioan Botezătorul)",
                    (13, 1): "Vinerea Mare (Good Friday)",  # The date for Good Friday varies; example for 2023
                    (13, 2): "Paștele Ortodox (Orthodox Easter Sunday)",  # Example for 2023
                    (0, 0): "A doua zi de Paște (Orthodox Easter Monday)",  # Example for 2023
                    (5, 1): "Ziua Muncii (Labor Day)",
                    (6, 1): "Ziua Copilului (Children's Day)",
                    (0, 0): "Rusaliile (Pentecost Sunday)",  # Example for 2023
                    (0, 0): "A doua zi de Rusalii (Pentecost Monday)",  # Example for 2023
                    (8, 15): "Adormirea Maicii Domnului (Assumption of the Virgin Mary)",
                    (11, 30): "Sfântul Andrei (Saint Andrew's Day)",
                    (12, 1): "Ziua Națională a României (Romania's National Day)",
                    (12, 25): "Crăciunul (Christmas Day)",
                    (12, 26): "A doua zi de Crăciun (Second Day of Christmas)"
                    }

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
    #current_year = 2025
    working_days = dict()
    
    for month in range(1, 13):
        working_days[calendar.month_name[month]] = get_working_days_in_month(current_year, month)
    
    return current_year, working_days

def orthodox_easter(year):
    """
    Calculate the date of Orthodox Easter for a given year.
    
    :param year: int - The year for which to calculate Orthodox Easter.
    :return: str - The date of Orthodox Easter in the format 'YYYY-MM-DD'.
    """
    # Calculate the "Golden Number"
    a = year % 19
    # Determine the century
    b = year % 4
    c = year % 7
    d = (19 * a + 15) % 30
    e = (2 * b + 4 * c + 6 * d + 6) % 7

    # Calculate the Julian calendar date of Orthodox Easter
    julian_easter_day = 22 + d + e

    # Adjust if Easter falls in April in the Julian calendar
    if julian_easter_day > 31:
        julian_easter_day -= 31
        julian_easter_month = 4
    else:
        julian_easter_month = 3

    # Convert Julian date to Gregorian date
    from datetime import date, timedelta

    # Julian Easter date
    julian_easter = date(year, julian_easter_month, julian_easter_day)

    # Difference between Julian and Gregorian calendars
    gregorian_easter = julian_easter + timedelta(days=13)

    return gregorian_easter.strftime("%Y-%m-%d")

def add_movable_holidays(year):
    date_of_Orthodox_Easter = orthodox_easter(year)
    month, day = int(date_of_Orthodox_Easter.split('-')[1]), int(date_of_Orthodox_Easter.split('-')[2])
    #ROMANIAN_HOLIDAYS[month, day] = "Paștele Ortodox (Orthodox Easter Sunday)"
    #ROMANIAN_HOLIDAYS[month, day+1] = "A doua zi de Paște (Orthodox Easter Monday)"
    ROMANIAN_HOLIDAYS[(month, day)] = ROMANIAN_HOLIDAYS.pop((13, 1))
    ROMANIAN_HOLIDAYS[(month, day+1)] = ROMANIAN_HOLIDAYS.pop((13, 2))
    '''
    # Rusaliile (la 50 de zile după Paște)
    rusalii = data_paste + timedelta(days=49)
    # A doua zi de Rusalii
    a_doua_zi_rusalii = rusalii + timedelta(days=1)
    '''
    

def is_weekend(year, month, day):
    """
    Check if a given day (month, day) is a weekend.
    """
    
    try:
        # Create a date object
        date = datetime.date(year, month, day)
        # Check if it's Saturday (5) or Sunday (6)
        return date.weekday() >= 5
    except ValueError:
        # Handle invalid dates
        print(f"Invalid date: {(month, day)}")
        return False

def check_national_holidays(year, month):
    days_off_holiday = 0
    for (holiday_month, holiday_day), name in ROMANIAN_HOLIDAYS.items():
        if holiday_month == month:
            if is_weekend(year, holiday_month, holiday_day):
                print(f'The National Holiday from date {year}.{holiday_month}.{holiday_day}, <{name}>, falls on a weekend!')
            else:
                print(f'The National Holiday from date {year}.{holiday_month}.{holiday_day}, <{name}>, falls on a weekday!')
                days_off_holiday += 1
    print(f'National Holidays in weekdays = {days_off_holiday}.')
    return days_off_holiday
    
    

def conclusion():
    # Calculate working days for every month of the current year
    current_year, working_days = working_days_in_current_year()
    
    # Print the results
    print(f'Year: {current_year}')
    
    # Orthodox Easter date
    date_of_Orthodox_Easter = orthodox_easter(current_year)
    print(f'The date of Orthodox Easter is {date_of_Orthodox_Easter}')
    
    add_movable_holidays(current_year)
    print(ROMANIAN_HOLIDAYS)
    
    for month, days in working_days.items():
        print(f'{month}: {days} working days')
    
    print()
        
    return current_year, working_days
        

def specific_conclusion():
    current_year, working_days = conclusion()

    actual_month = int(input("What month do you want to calculate the working days and the MUST office days for? "))
    days_off = int(input("How many day off will you take in this month? "))
    print()
    
    days_off_holiday = check_national_holidays(current_year, actual_month)
    
    current_month = list(working_days.keys())[actual_month-1]
    current_month_working_days = list(working_days.values())[actual_month-1]
    remaining_working_days = current_month_working_days - days_off - days_off_holiday
    MUST_office_days = round(0.4 * remaining_working_days, 2)
    
    print(f'In year {current_year}, month {current_month}, there are {current_month_working_days} working days.')
    print(f'You will take additional {days_off} days off.')
    print(f'So, remain {remaining_working_days} working days.')
    print(f"Conclusion: There are {MUST_office_days} MUST office days.")
      


def main():
    specific_conclusion()


if __name__ == '__main__':
    main()