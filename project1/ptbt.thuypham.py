years_to_months = 12
months_to_days = 30
days_to_hours = 24
hours_to_minutes = 60
minutes_to_seconds = 60
seconds_to_milliseconds = 1000
milliseconds_to_microseconds = 1000

def convert_years_to_months(years):
    return years * years_to_months

def convert_months_to_days(months):
    return months * months_to_days

def convert_days_to_hours(days):
    return days * days_to_hours

def convert_hours_to_minutes(hours):
    return hours * hours_to_minutes

def convert_minutes_to_seconds(minutes):
    return minutes * minutes_to_seconds

def convert_seconds_to_milliseconds(seconds):
    return seconds * seconds_to_milliseconds

def convert_milliseconds_to_microseconds(milliseconds):
    return milliseconds * milliseconds_to_microseconds

years = 2

months = convert_years_to_months(years)
days = convert_months_to_days(months)
hours = convert_days_to_hours(days)
minutes = convert_hours_to_minutes(hours)
seconds = convert_minutes_to_seconds(minutes)
milliseconds = convert_seconds_to_milliseconds(seconds)
microseconds = convert_milliseconds_to_microseconds(milliseconds)

print(f"{years} years is {months} months")
print(f"{months} months is {days} days")
print(f"{days} days is {hours} hours")
print(f"{hours} hours is {minutes} minutes")
print(f"{minutes} minutes is {seconds} seconds")
print(f"{seconds} seconds is {milliseconds} milliseconds")
print(f"{milliseconds} milliseconds is {microseconds} microseconds")

# Noice :3 Clean code

