def sum_of_multiples(limit, multiples):
    summation = 0  # Sum of all the multiples

    # For every non zero positive number below limit check to see if it is a
    # multiple of any of the numbers in the list multiples.  If it is then
    # add that number to summation and check the next number.
    for number in range(1, limit):
        for multiple in multiples:
            if number % multiple == 0:
                summation += number
                break

    return summation
