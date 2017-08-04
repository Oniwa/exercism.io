from __future__ import unicode_literals


def encode(data):
    data = list(data)  # Data to encode
    check = data[0]  # Check to see if letter is repeated
    count = 0  # Number of times letter is repeated
    encoded_data = ""  # Encoded data

    # Encodes the data
    for item in data:
        if check == item:
            count += 1
            check = item
        else:
            if count == 1:
                encoded_data += "{}".format(check)
            else:
                encoded_data += "{}{}".format(count, check)
            count = 1
            check = item

    if count == 1:
        encoded_data += "{}".format(check)
    else:
        encoded_data += "{}{}".format(count, check)

    return encoded_data


def decode(data):
    data = list(data)  # Incoming data
    letter = ''  # Current letter that we are working with
    decoded_data = ""  # Decoded data
    data_to_decode = []  # Corrected data set to decode
    temp_data = []  # Temporary data holder

    # We nee to check for things with more than 9 letters in a row.  If there
    # are we need to construct a new list with the bigger numbers.
    # IE 12Wb3d turns into ['12', 'W', 'b', '3', 'd'] instead of
    # the incorrect list of ['1', '2', 'W', 'b', '3', 'd']
    for index in range(len(data)):
        if data[index].isdigit():
            temp_data.append(data[index])
        else:
            temp_data = ''.join(temp_data)
            if temp_data != '':
                data_to_decode.append(temp_data)
            temp_data = []
            data_to_decode.append(data[index])

    # Decodes the data
    for i, item in enumerate(data_to_decode):
        if item.isdigit():
            count = int(item)
            letter = data_to_decode[i + 1]
            decoded_data += "{}".format(count * letter)
        else:
            new_letter = item
            if new_letter != letter:
                letter = new_letter
                decoded_data += "{}".format(letter)

    return decoded_data
