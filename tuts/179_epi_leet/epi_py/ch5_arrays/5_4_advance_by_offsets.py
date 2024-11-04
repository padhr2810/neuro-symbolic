"""
TRICK:
KEEP TRACK OF FURTHEST INDEX REACHED THUS FAR. 
TWO POINTERS: I) 'i' (ADD FROM HERE)
	      II) 'furthest_reach_so_far'
IF 'i' GOES BEYOND 'furthest_reach_so_far', GAME OVER, THEN RETURN
CAN TAKE FEWER STEPS IF YOU WANT, BUT NEVER MORE.
TRICK: 2x CHECKS. EACH ITERATION, CHECK THAT DIDN'T REACH THE LAST INDEX IN THE ARRAY. ALSO NEED TO CHECK THAT CURRENT INDEX IS NOT GONE BEYOND THE MAX REACHED THUS FAR.
"""

from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:

    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
