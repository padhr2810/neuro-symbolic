"""
TRICK #1: PICKING A NUMBER IN THE RANGE OF 0-3 JUST NEEDS 2 CALLS TO THE RANDOM NUMBER GENERATOR.
TRICK #2: DISCARD AND START ALL OVER AGAIN IF RESULT GIVES A NUMBER EXCEEDING THE ACCEPTABLE RANGE. (ONLY RELEVANT FOR SOME RANGES)
"""

import functools
import random


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound: int, upper_bound: int) -> int:

    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            # zero_one_random() is the provided random number generator.
            result = (result << 1) | zero_one_random()
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


print(uniform_random(0,5))
