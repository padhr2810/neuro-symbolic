"""
TRICK 1: SINGLE PASS.

TRICK 1.2: USE "PIVOT" TO PARTITION THE NUMBERS.

TRICK 2:
"LARGER" STARTS AFTER THE END OF THE ARRAY. I.E. INDEX=N. DON'T MAKETHE MISTAKE OF N-1.

TRICK 3:
ONLY COMPARE A[EQUAL] VS PIVOT. IGNORE A[LARGER] AND A[SMALLER]

TRICK #4:
3 ITERATORS FOR: I) END OF NUMS SMALLER THAN PIVOT. II) END OF NUMS EQUAL TO PIVOT. III) START OF NUMS LARGER THAN PIVOT.
INITIALISED TO: 0, 0, LEN(ARRAY)
ALWAYS COMPARE ARRAY[EQUAL] TO PIVOT, IN LOOP UNTIL 'LARGER' & 'EQUAL' CONVERGE THEN EXIT.

TRICK #5:
3 POSSIBLE OUTCOMES FOR EACH ITERATION:
I: IF SMALLER, PUSH TOWARDS FRONT. II: IF SAME SIZE, DON'T MOVE ANYWHERE. III: IF BIGGER, PUSH TO BACK.
[IF SMALLER, INCREMENT BOTH EQUAL & SMALLER INDICES. IF EQUAL, ONLY INCREMENT EQUAL INDEX. IF LARGER, DECREMENT THE LARGER INDEX.

"""

import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:

    pivot = A[pivot_index]
    print(f"pivot INdex: {pivot_index}; Value: {pivot}")
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    
    smaller, equal, larger = 0, 0, len(A)			# I.E. SMALLER = END OF THE SMALLER SECTION
    								# I.E. EQUAL = END OF THE EQUAL SECTION
    								# I.E. 'LARGER' = START OF THE LARGER GROUP.
    
    # Keep iterating as long as there is an unclassified element.
    iter=1
    while equal < larger:			
    								# A[equal] is the incoming unclassified element.
        							# ALWAYS COMPARE 'A[equal]' VS 'PIVOT' ABS VALUE
        if A[equal] < pivot:					
            A[smaller], A[equal] = A[equal], A[smaller]		# 1: PUSH 'SMALLER' TOWARDS FRONT -- I.E. SWAP SMALLER & EQUAL.
            smaller, equal = smaller + 1, equal + 1		# INCREMENT BOTH SMALLER & EQUAL.
            
        elif A[equal] == pivot:					# 2: DON'T PUSH ANYWHERE.
            equal += 1						# INCREMENT ONLY 'equal'. --- IF EQUAL TO THE PIVOT.
            
        else:  # A[equal] > pivot.				# 3: PUSH 'LARGER' TO THE BACK.
            larger -= 1						# DECREMENT LARGER. --- IF GREATER THAN PIVOT.
            A[equal], A[larger] = A[larger], A[equal]		# THEN SWAP 'EQUAL' AND 'LARGER'
        print(f"Iter # {iter}: A")
        iter+=1 
    print(f"bottom group = {A[:smaller]}")
    print(f"middle group = {A[smaller: equal]}")
    print(f"unclassified group = {A[equal: larger]}")  # TARGET - MAKE THIS GAP = ZERO.
    print(f"top group = {A[larger:]}")
    
dutch_flag_partition(2, [0,1,2,1,1,1,5,5,5])
dutch_flag_partition(3, [0,1,2,1,1,1,5,5,5])
exit() 

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
