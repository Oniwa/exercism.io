def is_isogram(word):
    data = list(word.lower())
    letters = {}
    isogram = True

    # Create a dictionary in which every key is a character and every value
    # is the number of times that character is in the word
    for item in data:
        if item in letters:
            letters[item] += 1
        else:
            letters[item] = 1

    # Checks each alphabetical key to see if it is greater than 1.
    # If it is then the word is not an isogram
    for key in letters:
        if key.isalpha():
            if letters[key] > 1:
                isogram = False
                break

    return isogram
