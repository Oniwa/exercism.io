from __future__ import unicode_literals

def encode(data):
    data = list(data)
    check = data[0]
    count = 0
    encoded_data = ""

    for item in data:
        if(check == item):
            count += 1
            check = item
        else:
            if(count == 1):
                encoded_data = encoded_data + "{}".format(check)
            else:
                encoded_data = encoded_data + "{}{}".format(count, check)
            count = 1
            check = item

    if(count == 1):
        encoded_data = encoded_data + "{}".format(check)
    else:
        encoded_data = encoded_data + "{}{}".format(count, check)

    return encoded_data

def decode(data):
    data = list(data)
    count = 0
    letter = ''
    decoded_data = ""

    for i, item in enumerate(data):
        if item.isdigit():
            count = int(item)
            letter = data[i + 1]
            decoded_data = decoded_data + "{}".format(count * letter)
        else:
            new_letter = item
            if(new_letter != letter):
                decoded_data = decoded_data + "{}".format(letter)

    return decoded_data