def square_of_sum(number):
    # Generate list of numbers starting from 1 and going to input number
    numbers = list(range(1, number + 1))

    # Sums list and then squares
    return (sum(numbers))**2


def sum_of_squares(number):
    # Generates list of of numbers from 1 to input number and squares each
    # element
    numbers = [x**2 for x in range(1, number + 1)]

    # Sums the list of squares
    return sum(numbers)


def difference(number):
    # Find the difference of squares
    return square_of_sum(number) - sum_of_squares(number)
