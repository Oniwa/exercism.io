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

power_3 = {0: '',
           1: 'thousand',
           2: 'million and',
           3: 'billion and'
           }

def say(number):
    number = int(number)
    number_to_say = number_splitter(number)
    number_of_digits = len(str(number))
    verbal_number = []
    count = 0
    if number_of_digits == 1 and number_to_say == [0]:
        return ones[0]
    for item in reversed(number_to_say):
        verbal_number.append(say_number(item, count))
        count += 1

    return ' '.join(reversed(verbal_number))


def say_number(number, count):
    number_digits = str(number)
    verbal_number = None

    if number == 0:
        verbal_number = power_3[count + 1]
    elif 0 <= number < 10:
        verbal_number = ones[number]
    elif 10 <= number < 20:
        verbal_number = teens[number]
    elif 20 <= number < 100:
        if int(number_digits[1]) > 0:
            verbal_number = '{}-{}'.format(tens[int(number_digits[0])],
                                           ones[int(number_digits[1])])
        else:
            verbal_number = tens[int(number_digits[0])]
    elif 100 <= number < 1000:
        if int(number_digits[1]) == int(number_digits[2]) == 0:
            verbal_number = "{} hundred{}".format(ones[int(number_digits[0])],
                                           power_3[count])
        else:
            two_digits = '{}{}'.format(number_digits[1], number_digits[2])
            two_digits = int(two_digits)
            verbal_number = "{} hundred and {}".format(ones[int(number_digits[0])],
                                                       say_number(two_digits, 0))

    return verbal_number


def number_splitter(number):
    number = str(number)
    tmp_list = []
    split_numbers = []
    while len(number):
        tmp_list.insert(0, number[-3:])
        number = number[:-3]

    for item in tmp_list:
        item = int(item)
        split_numbers.append(item)
    return split_numbers
