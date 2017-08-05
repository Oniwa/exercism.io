def is_isogram(word):
    data = word.split()
    letters = {}
    isogram = True

    for item in data:
        if item in letters:
            letters[item] += 1
        else:
            letters[item] = 1

    for key in letters:
        if letters[key] > 1:
            isogram = False

    return isogram
