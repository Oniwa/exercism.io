def flatten(iterable):
    flattened_list = []

    flat = flattener(iterable)

    for item in flat:
        flattened_list.append(item)

    return flattened_list

def flattener(iterable):
    flattened = []

    for item in iterable:
        if type(item) is list:
            flat = flattener(item)
            for thing in flat:
                flattened.append(thing)
        else:
            if item or item == 0:
                flattened.append(item)

    return flattened