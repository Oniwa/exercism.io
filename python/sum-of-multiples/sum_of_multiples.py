def sum_of_multiples(limit, multiples):
    summation = 0

    for number in range(1, limit):
        for multiple in multiples:
            if number % multiple == 0:
                summation += number
                break

    return summation
