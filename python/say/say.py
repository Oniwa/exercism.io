NAMES = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine',

    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen',

    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety',
}

POWERS_OF_TEN = {3: 'thousand', 6: 'million', 9: 'billion'}
MAX_POWER_OF_TEN = max(POWERS_OF_TEN) + 3


def _less_than_a_hundred(number):
    """
    Helper function for _less_than_a_thousand().  Handles numbers from 1 to 99
    (and raises an exception for anything outside that range).
    """
    if number in NAMES:
        return NAMES[number]
    tens, ones = divmod(number, 10)
    return '%s-%s' % (NAMES[tens * 10], NAMES[ones])


def _less_than_a_thousand(number, force_and=False):
    """
    Helper function for say().  Handles numbers from 1 to 999 (for numbers
    outside this range, this function will return unreliable results or raise
    an exception).
    """
    hundreds, rest = divmod(number, 100)
    return_list = []
    if hundreds:
        return_list.extend((NAMES[hundreds], 'hundred'))
    if (hundreds or force_and) and rest:
        return_list.append('and')
    if rest:
        return_list.append(_less_than_a_hundred(rest))
    return ' '.join(return_list)


def say(number):
    if not 0 <= number < 10 ** MAX_POWER_OF_TEN:
        raise AttributeError('Why is this an AttributeError?')
    if number == 0:
        return 'zero'

    representation = []
    power_of_ten = 0
    while number:
        number, this_portion = divmod(number, 1000)
        if this_portion:
            if power_of_ten in POWERS_OF_TEN:
                representation.append(POWERS_OF_TEN[power_of_ten])
            # To handle things like "one million and two", we need to tell the
            # helper function that it must include "and" just in case this
            # portion is the under-1000 part of the number *and* there's a part
            # of the number over 1000.
            force_and = (power_of_ten == 0 and number)
            representation.append(_less_than_a_thousand(this_portion,
                                                        force_and=force_and))
        power_of_ten += 3
    return ' '.join(reversed(representation))