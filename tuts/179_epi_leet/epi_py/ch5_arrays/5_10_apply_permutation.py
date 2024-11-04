"""
TRICK
DON'T CALCULATE ALL PERMUTATIONS. JUST NEED TO APPLY ONE PARTICULAR PERMUTATION TO YOUR ARRAY.
INPUT = ONE ARRAY ... OUTPUT = ONE ARRAY. 
E.G. IF P = (2,0,1,3) MOVE FIRST ELEMENT TO INDEX 2; MOVE SECOND TO INDEX 0; MOVE THIRD TO INDEX 1; LAST REMAINS WHERE IT IS.
DOUBLE PASS OVER ARRAY. AND DO TWO (2) SWAPS AT EACH STEP. I.E. FIRST UPDATE THE INPUT ARRAY, AND THEN UPDATE THE PERMUTATION ARRAY IN THE SAME MANNER.
WHEN AN ELEMENT IS AT ITS CORRECT POSITION, MOVE TO THE NEXT ELEMENT / INDEX IN THE INPUT ARRAY ... I.E. "WHILE perm[i] != i:"
"""

from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:

    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
