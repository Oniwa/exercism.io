def is_pangram(sentence):
    """
    This function checks to see if a sentence is a pangram.

    :param sentence:  System to check
    :return:  True if it is a pangram; False if it is not
    """
    # Disctionary of all letters to track occurences of each letter in sentence
    letters = {'a': 0,
               'b': 0,
               'c': 0,
               'd': 0,
               'e': 0,
               'f': 0,
               'g': 0,
               'h': 0,
               'i': 0,
               'j': 0,
               'k': 0,
               'l': 0,
               'm': 0,
               'n': 0,
               'o': 0,
               'p': 0,
               'q': 0,
               'r': 0,
               's': 0,
               't': 0,
               'u': 0,
               'v': 0,
               'w': 0,
               'x': 0,
               'y': 0,
               'z': 0,
               }

    # Remove all whitespace and special characters while making each letter lowercase
    sentence = ''.join(e.lower() for e in sentence if e.isalnum())

    # Iterates through sentence and increments the dictionary value of each letter
    for letter in sentence:
        letters[letter] += 1

    # If any letter is equal to 0 then the sentence is not a pangram
    for key in letters:
        if(letters[key] == 0):
            return False

    return True