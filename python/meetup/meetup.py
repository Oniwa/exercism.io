import datetime as dt
from calendar import monthrange


def meetup_day(year, month, day, descriptor):
    days_of_week = {"Monday": 0,
                    "Tuesday": 1,
                    "Wednesday": 2,
                    "Thursday": 3,
                    "Friday": 4,
                    "Saturday": 5,
                    "Sunday": 6}

    for weekday in range(7):
        first_weekday = dt.date(year, month, weekday + 1)
        if first_weekday.weekday() == days_of_week[day]:
            first_day = weekday + 1
            break

    if descriptor == '1st':
        day = first_day
    elif descriptor == '2nd':
        day = first_day + 7
    elif descriptor == '3rd':
        day = first_day + 14
    elif descriptor == '4th':
        day = first_day + 21
    elif descriptor == '5th':
        day = first_day + 28
    elif descriptor == 'teenth':
        if first_day + 7 >= 13:
            day = first_day + 7
        else:
            day = first_day + 14
    elif descriptor == 'last':
        if first_day + 28 <= int(monthrange(year, month)[1]):
            day = first_day + 28
        else:
            day = first_day + 21

    return dt.date(year, month, day)

if __name__ == "__main__":
    pass
