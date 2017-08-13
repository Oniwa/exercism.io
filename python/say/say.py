ones = {0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
        }

tens = {2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'sevent',
        8: 'eighty',
        9: 'ninety'
        }

teens = {10: 'ten',
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen',
         14: 'fourteen',
         15: 'fifteen',
         16: 'sixteen',
         17: 'seventeen',
         18: 'eighteen',
         19: 'nineteen'
         }


def say(number):
    number_digits = str(number)
    verbal_number = None

    if 0 <= number < 100:
        verbal_number = say_two_digits(number)
    elif 100 <= number < 1000:
        verbal_number = say_three_digits(number)
    elif 1000<= number < 10000:
        verbal_number = say_four_digits(number)

    return verbal_number


def say_two_digits(number):
    number_digits = str(number)
    verbal_number = None

    if 0 <= number < 10:
        verbal_number = ones[number]
    elif 10 <= number < 20:
        verbal_number = teens[number]
    elif 20 <= number < 100:
        if int(number_digits[1]) > 0:
            verbal_number = '{}-{}'.format(tens[int(number_digits[0])],
                                           ones[int(number_digits[1])])
        else:
            verbal_number = tens[int(number_digits[0])]

    return verbal_number


def say_three_digits(number):
    number_digits = str(number)

    if int(number_digits[1]) == int(number_digits[2]) == 0:
        verbal_number = "{} hundred".format(ones[int(number_digits[0])])
    else:
        two_digits = '{}{}'.format(number_digits[1], number_digits[2])
        two_digits = int(two_digits)
        verbal_number = "{} hundred and {}".format(ones[int(number_digits[0])],
                                                   say_two_digits(two_digits))

    return verbal_number


def say_four_digits(number):
    number_digits = str(number)

    if int(number_digits[1]) == int(number_digits[2]) == \
            int(number_digits[3]) ==  0:
        verbal_number = "{} thousand".format(ones[int(number_digits[0])])
    else:
        three_digits = int(number_digits[-3:])
        verbal_number = "{} thousand {}".format(ones[int(number_digits[0])],
                                                    say_three_digits(three_digits))

    return verbal_number
