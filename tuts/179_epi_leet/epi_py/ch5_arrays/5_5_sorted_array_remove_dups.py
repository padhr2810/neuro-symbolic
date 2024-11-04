"""
TRICK #1: EDGE CASE, IF EMPTY ARRAY, RETURN 0

TRICK #2: = 2 POINTERS, 'write_index' AND 'i' BOTH INIT = 1
    "write_index" OK TO START AT VALUE OF 1, COZ OBVIOUSLY AT LEAST 1 UNIQUE VALUE (COZ ACCOUNTED FOR EDGE CASE ABOVE)

TRICK #3: ONLY NEED TO RETURN 'write_index' BECAUSE IT'S THE NUMBER OF UNIQUE VALUES IN ARRAY.

TRICK #4: SINGLE PASS. LOOP OVER "i" INDEX. THEN AT EACH STEP, CHECK IF: [write_index-1] == [i] ... 
    I.E. NEED TO COMPARE THE "i" POINTER VERSUS THE VALUE PRECEDING THE "write_index" POINTER ... I.E. CHECK IF FOUND A NEW VALUE.
    IF YES, INCREMENT THE "write_index" POINTER. 
    BUT IF NO, DON'T INCREMENT "write_index" POINTER. I.E. THE GAP WIDENS BETWEEN THE 2 POINTERS 
"""

import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
