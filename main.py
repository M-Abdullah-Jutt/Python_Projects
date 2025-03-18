
from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    # Get today's date and time
    today = datetime.now()

    # Calculate year difference
    year_diff = today.year - birth_year

    # Calculate month difference
    month_diff = today.month - birth_month

    # Calculate day difference
    day_diff = today.day - birth_day

    # Adjust if the current day is before the birth day (in negative)
    if day_diff < 0:
        month_diff -= 1
        # Add the number of days in the previous month to the day difference.
        if today.month == 1:
            prev_month_days = 31  # December has 31 days
        else:
            prev_month_days = (today.replace(month=today.month - 1, day=1) - today.replace(month=today.month - 1, day=1)).days
        day_diff += prev_month_days

    # Adjust if the current month is before the birth month
    if month_diff < 0:
        year_diff -= 1
        month_diff += 12

    return year_diff, month_diff, day_diff

# Input from user
birth_year = int(input("Enter your year of birth: "))
birth_month = int(input("Enter your month of birth: "))
birth_day = int(input("Enter your day of birth: "))

# Calculate age
years, months, days = calculate_age(birth_year, birth_month, birth_day)

# Output the result
print(f"Your age is {years} years, {months} months, and {days} days.")