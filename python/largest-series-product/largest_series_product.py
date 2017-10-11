def largest_product(series, size):
    if size < 0:
        raise ValueError
    elif series.isupper() or series.islower():
        raise ValueError
    elif len(series) < size:
        raise ValueError

    if series == "":
        if size > 0:
            raise ValueError
        else:
            return 1
    else:
        if size == 0:
            return 1

    numbers = [int(d) for d in series]
    slices =  len(numbers) - size + 1

    multiple = 1
    max_multiple = 0
    count = 0

    for _ in range(1, slices + 1):
        for item in numbers[0 + count:size + count]:
            multiple *= item
        if multiple > max_multiple:
            max_multiple = multiple
        count += 1
        multiple = 1

    return max_multiple
