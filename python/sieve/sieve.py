def sieve(limit):
    # Creates list of numbers to check for primacy starting at two and going
    # to limit
    primes = list(range(2, limit + 1))

    # For each number in list
    for number in primes:
        multiple = 0
        count = 2

        # find it's multiples starting with number times 2 until the
        # result is greater than the limit.  Remove from the list of primes
        # (mark composite) each answer; i.e. for 2 you would remove
        # 4, 6, 8,... for 3 you would remove 6, 9, 12, ...
        while multiple < limit:
            multiple = number * count
            if multiple in primes:
                primes.remove(multiple)
            count +=1

    # The leftover list of numbers is the list of primes up to the limit
    return primes
