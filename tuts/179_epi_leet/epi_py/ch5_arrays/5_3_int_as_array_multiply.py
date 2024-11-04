"""
TRICK #1: NUMBERS TOO BIG TO MULTIPLY WITH INT TYPE. SO BREAK IT INTO LOTS OF SMALL MULTIPLICATIONS.

TRICK #2: 'NESTED FOR LOOP' GOES THROUGH BOTH ARRAYS.

TRICK #3: USE '^' TO DETERMINE THE SIGN OF THE RESULT

TRICK #4: SIZE OF THE RESULT IS THE SUM OF THE LENGTHS OF 2 ARRAYS.

TRICK #5: FOR EACH LITTLE MULTIPLICATION = [i + j + 1], AND THEN [i+j], AND THEN BACK TO [i + j + 1]
"""

from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:

    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeroes.
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
