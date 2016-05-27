from datetime import timedelta

def add_gigasecond(date):
    # Calculates the date 10**9 seconds from the given date
    return date + timedelta(seconds=10**9)

