def slices(number, slice_length):
    num_length = len(number)
    number_of_slices = num_length - slice_length + 1
    slice_return = []

    if number_of_slices > num_length:
        raise ValueError("Can't return sub-strings of length 0")
    elif slice_length > num_length:
        raise ValueError("Slice length is bigger than length of number to be "
                         "sliced")
    else:
        for slice_range in range(number_of_slices):
            new_num = number[slice_range:(slice_range + slice_length)].split()
            new_num2 = [int(x) for x in str(new_num[0])]
            slice_return.append(new_num2)

    return slice_return
