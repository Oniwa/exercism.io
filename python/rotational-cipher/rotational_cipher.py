def rotate(input_text, key):
    # Turn a number into its corresponding letter of the alphabet
    number_to_letter = {'1': 'a',
                        '2': 'b',
                        '3': 'c',
                        '4': 'd',
                        '5': 'e',
                        '6': 'f',
                        '7': 'g',
                        '8': 'h',
                        '9': 'i',
                        '10': 'j',
                        '11': 'k',
                        '12': 'l',
                        '13': 'm',
                        '14': 'n',
                        '15': 'o',
                        '16': 'p',
                        '17': 'q',
                        '18': 'r',
                        '19': 's',
                        '20': 't',
                        '21': 'u',
                        '22': 'v',
                        '23': 'w',
                        '24': 'x',
                        '25': 'y',
                        '26': 'z',
                        }

    # Turns a letter into its number position in the alphabet
    letter_to_number = {'a': 1,
                        'b': 2,
                        'c': 3,
                        'd': 4,
                        'e': 5,
                        'f': 6,
                        'g': 7,
                        'h': 8,
                        'i': 9,
                        'j': 10,
                        'k': 11,
                        'l': 12,
                        'm': 13,
                        'n': 14,
                        'o': 15,
                        'p': 16,
                        'q': 17,
                        'r': 18,
                        's': 19,
                        't': 20,
                        'u': 21,
                        'v': 22,
                        'w': 23,
                        'x': 24,
                        'y': 25,
                        'z': 26,
                        }

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
                if letter_to_number[letter] + key > 26:
                    new_letter = str(letter_to_number[letter] + key - 26)
                    cypher_text.append(number_to_letter[new_letter].upper())
                else:
                    new_letter = str(letter_to_number[letter] + key)
                    cypher_text.append(number_to_letter[new_letter].upper())
            else:
                if letter_to_number[letter] + key > 26:
                    new_letter = str(letter_to_number[letter] + key - 26)
                    cypher_text.append(number_to_letter[new_letter].lower())
                else:
                    new_letter = str(letter_to_number[letter] + key)
                    cypher_text.append(number_to_letter[new_letter].lower())
        else:
            cypher_text.append(letter)

    # Reconstruct the string output
    cypher_text = ''.join(cypher_text)

    return cypher_text
