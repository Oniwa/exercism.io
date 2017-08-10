import re


def abbreviate(phrase):
    phrase = re.split(' |-', phrase)
    acronym = []

    for word in phrase:
        acronym.append(word[0].upper())

    return ''.join(acronym)
