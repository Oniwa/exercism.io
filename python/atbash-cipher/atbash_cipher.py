from string import ascii_lowercase


def encode(plain_text):
    plain_text = list(plain_text)
    cypher_text = []

    for letter in plain_text:
        if letter.isalpha():
            cypher_letter_index = -1 * (ascii_lowercase.index(letter.lower()) - 25)
            cypher_letter = ascii_lowercase[cypher_letter_index]
            cypher_text.append(cypher_letter)
        elif letter.isdigit():
            cypher_text.append(letter)

    return ''.join(grouping(cypher_text, 5))


def grouping(cyphertext, size):
    grouped_text = []
    count = 1

    for item in cyphertext:
        grouped_text.append(item)
        if size % count == 0 and count != 1:
            grouped_text.append(' ')
            count = 1
        else:
            count += 1

    if grouped_text[len(grouped_text) - 1] == ' ':
        grouped_text = grouped_text[:-1]

    return grouped_text


def decode(cypher_text):
    cypher_text = list(cypher_text)
    plain_text = []

    for letter in cypher_text:
        if letter.isalpha():
            plain_letter_index = -1 * (ascii_lowercase.index(letter.lower()) - 25)
            plain_letter = ascii_lowercase[plain_letter_index]
            plain_text.append(plain_letter)
        elif letter.isdigit():
            plain_text.append(letter)

    return "".join(plain_text)
