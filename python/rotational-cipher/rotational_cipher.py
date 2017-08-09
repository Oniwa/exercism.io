# ascii_lowercase contains a string of all the lowercase letters.  By using
# the index method I can find the number of any letter and by using list
# notation I can find the letter of any number.  This change was suggested
# by gield and allowed me to remove 2 dictionaries that were 26 items long.
from string import ascii_lowercase


def rotate(input_text, key):
    text = list(input_text)  # Text to encrypt
    cypher_text = []  # Cypher text to return

    # For each letter convert it into a number and then add the key.  If the
    # resulting number is larger than 26 subtract 26 from it.  This will give
    # the position of the new cypher letter.  Do not transform things that are
    # not letters just  leave them as they were before.
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
                if ascii_lowercase.index(letter) + key >= 26:
                    new_letter = ascii_lowercase.index(letter) + key - 26
                    cypher_text.append(ascii_lowercase[new_letter].upper())
                else:
                    new_letter = ascii_lowercase.index(letter) + key
                    cypher_text.append(ascii_lowercase[new_letter].upper())
            else:
                if ascii_lowercase.index(letter) + key >= 26:
                    new_letter = ascii_lowercase.index(letter) + key - 26
                    cypher_text.append(ascii_lowercase[new_letter].lower())
                else:
                    new_letter = ascii_lowercase.index(letter) + key
                    cypher_text.append(ascii_lowercase[new_letter].lower())
        else:
            cypher_text.append(letter)

    # Reconstruct the string output
    cypher_text = ''.join(cypher_text)

    return cypher_text
