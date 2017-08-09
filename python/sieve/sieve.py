def sieve(limit):
    primes = list(range(2, limit + 1))

    for number in primes:
        multiple = 0
        count = 2

        while multiple < limit:
            multiple = number * count
            if multiple in primes:
                primes.remove(multiple)
            count +=1

    return primes
