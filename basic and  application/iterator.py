import math
import itertools


def primes():
    value = 2
    while True:
        if (math.factorial(value - 1) + 1) % value == 0:
            yield value
        value += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
