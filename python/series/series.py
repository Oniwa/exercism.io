def slices(number, slice_length):
    num_length = len(number)  # Number of digits in number
    number_of_slices = num_length - slice_length + 1  # Number of sub-strings to return
    slice_return = []  # Return list

    # Error guarding
    if number_of_slices > num_length:
        raise ValueError("Can't return sub-strings of length 0")
    elif slice_length > num_length:
        raise ValueError("Slice length is bigger than length of number to be "
                         "sliced")
    else:
        # Find the sub-strings.  Since the unittests wanted the sub-strings
        # themselves to be broken into lists of their digits the list
        # comprehension was added.
        for slice_range in range(number_of_slices):
            new_num = number[slice_range:(slice_range + slice_length)].split()
            new_num = [int(x) for x in str(new_num[0])]
            slice_return.append(new_num)

    return slice_return
