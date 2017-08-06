def square_of_sum(number):
    numbers = list(range(1, number + 1))

    return (sum(numbers))**2


def sum_of_squares(number):
    numbers = [x**2 for x in range(1, number + 1)]

    return sum(numbers)


def difference(number):
    return square_of_sum(number) - sum_of_squares(number)
