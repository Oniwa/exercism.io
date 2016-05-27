def is_leap_year(year):
    """
    Determines whether a given year is a leap year.

    :param year:  Year to check
    :return: Boolean
    """
    # Check for leap century
    if year % 400 == 0:
        return True
    # Check for regular century
    elif year % 100 == 0:
        return False
    # Check for leap year
    elif year % 4 == 0:
        return True
    # Every other year
    else:
        return False