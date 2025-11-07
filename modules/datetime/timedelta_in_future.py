from datetime import datetime, timedelta

# Let's start with a specific date as an example
start_date = datetime(2024, 4, 20)  # April 20, 2024

# Add 50 days
future_date = start_date + timedelta(days=50)
future_date = start_date + timedelta(weeks=7)

# Get the resulting month and day
result_month = future_date.month
result_day = future_date.day

# Format the date nicely for display
formatted_date = future_date.strftime("%B %d") 

print(f"Starting date: {start_date.strftime('%B %d')}")
print(f"Date after 50 days: {formatted_date}")