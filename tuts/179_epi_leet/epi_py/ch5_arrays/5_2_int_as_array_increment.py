"""
TRICK: 
STEP 1: START BY NAIVELY +=1 TO THE LAST ELEMENT.
STEP 2: CHECK FOR 10 ALL THE WAY FROM END TO INDEX 1 (REVERSED OBVIOUSLY)
STEP 3: FINAL CHECK IF INDEX A[0] == 10 ... IF YES, THEN CHANGE TO '1' AND APPEND AN EXTRA '0' TO THE END ... INDEX=0 MUST BE TREATED SEPARATELY.
        EDGE CASE - IF ALL ELEMENTS = 9, NEED TO INSERT AN EXTRA ELEMENT.
TRICK: "REVERSED" SO CAN START START AT THE END I.E. LSD.
"""

from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:

    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    else:
        if A[0] == 10:
            # There is a carry-out, so we need one more digit to store the result.
            # A slick way to do this is to append a 0 at the end of the array,
            # and update the first entry to 1.
            A[0] = 1
            A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
