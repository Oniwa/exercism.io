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
    return data