from string import ascii_lowercase


def encode(plain_text):
    plain_text = list(plain_text)  # Listify the string
    cypher_text = []  # Encoded cypher text

    # For each item in string if it is a letter then get the encoded letter and
    # append it to the cypher text.  If it is a number then append the number.
    # Skip punctuation.
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

    # For every size (number) of letters add a space
    for item in cyphertext:
        grouped_text.append(item)
        if size % count == 0 and count != 1:
            grouped_text.append(' ')
            count = 1
        else:
            count += 1

    # If the last character is a space trim it
    if grouped_text[len(grouped_text) - 1] == ' ':
        grouped_text = grouped_text[:-1]

    return grouped_text


def decode(cypher_text):
    cypher_text = list(cypher_text)
    plain_text = []

    # For each item in string if it is a letter then get the decoded letter and
    # append it to the plain text.  If it is a number then append the number.
    # Skip punctuation.
    for letter in cypher_text:
        if letter.isalpha():
            plain_letter_index = -1 * (ascii_lowercase.index(letter.lower()) - 25)
            plain_letter = ascii_lowercase[plain_letter_index]
            plain_text.append(plain_letter)
        elif letter.isdigit():
            plain_text.append(letter)

    return "".join(plain_text)
