"""
TRICK
"DICTIONARY ORDERING" OF PERMUTATIONS - IF ALL VALUES OF ARRAY ARE IN DECREASING ORDER (IE MAX VALUE), THIS IS THE FINAL PERMUTATION.
E.G. INPUT = (1,0,3,2) ---> RETURN (1,2,0,3) 
E.G. INPUT = (3,2,1,0) ---> RETURN ()   ... COZ REACHED THE END OF THE "DICTIONARY ORDERING" 

FOUR STEPS IN THE PROCESS;
STEP 1: IN REVERSE FROM THE END, FIND FIRST VALUE THAT IS NOT >+ THE NEXT VALUE. THIS IS INVERSION POINT.
STEP 2: IN THE SUFFIX (I.E. AFTER INVERSION POINT) FIND THE SMALLEST VALUE THAT EXCEEDS THE INVERSION POINT VALUE.
STEP 3: SWAP VALUES 1 & 2 ABOVE.
STEP 4: REVERSE THE SUFFIX (I.E. ALL NUMBERS AFTER INVERSION POINT)
"""

from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:

    # Find the first entry from the right that is smaller than the entry
    # immediately after it.
    inversion_point = len(perm) - 2
    while (inversion_point >= 0
           and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []  # perm is the last permutation.

    # Swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm are decreasing after
    # inversion_point, if we search in reverse order, the first entry that is
    # greater than perm[inversion_point] is the entry to swap with.
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # Entries in perm must appear in decreasing order after inversion_point,
    # so we simply reverse these entries to get the smallest dictionary order.
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
