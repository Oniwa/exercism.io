import re


def abbreviate(phrase):
    # Use the regular expression library to split the phrase up into its
    # individual words using spaces and hyphens as the delimiter.
    phrase = re.split(' |-', phrase)
    acronym = []

    # Look at each word in the phrase and take the first letter of it.
    # Append an upper cased version of the letter to acronym list
    for word in phrase:
        acronym.append(word[0].upper())

    # Turn the list into a string and return
    return ''.join(acronym)
