import datetime as dt
from calendar import monthrange


def meetup_day(year, month, day, descriptor):
    # Converts the day into the datetime modules format for weekday
    days_of_week = {"Monday": 0,
                    "Tuesday": 1,
                    "Wednesday": 2,
                    "Thursday": 3,
                    "Friday": 4,
                    "Saturday": 5,
                    "Sunday": 6}

    # Finds the first date of the month that is the given day of the week
    for weekday in range(7):
        # Add 1 to weekday since it starts at 0 and months start at 1
        first_weekday = dt.date(year, month, weekday + 1)
        if first_weekday.weekday() == days_of_week[day]:
            first_date = weekday + 1
            break

    # Depending on descriptor you will need to add some multiple of 7 to the
    # first date.  If the descriptor is teenth it will be the second or 3rd
    # occurrence of the month.  For last it will be the 4th or 5th occurrence
    # of the month.
    if descriptor == '1st':
        day = first_date
    elif descriptor == '2nd':
        day = first_date + 7
    elif descriptor == '3rd':
        day = first_date + 14
    elif descriptor == '4th':
        day = first_date + 21
    elif descriptor == '5th':
        day = first_date + 28
    elif descriptor == 'teenth':
        if first_date + 7 >= 13:
            day = first_date + 7
        else:
            day = first_date + 14
    elif descriptor == 'last':
        if first_date + 28 <= int(monthrange(year, month)[1]):
            day = first_date + 28
        else:
            day = first_date + 21

    return dt.date(year, month, day)

