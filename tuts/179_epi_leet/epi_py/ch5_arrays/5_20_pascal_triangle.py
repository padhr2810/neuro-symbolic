"""
TRICK
INITIALISE THE TRIANGLE WITH ALL VALUES = 1.
NESTED LOOP OVER THE TRIANGLE. I.E. EVERY ROW / THEN COLUMN.
BUT ALWAYS SKIP THE FIRST & LAST COLUMN IN EACH ROW. I.E. FOR COLUMNS, "range(1,i)" INSTEAD OF "range(0,i+1)"
THEN JUST A MATTER OF ADDING THE 2 VALUES ABOVE IN THE PREVIOUS ROW.
"""

from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:

    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries.
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
