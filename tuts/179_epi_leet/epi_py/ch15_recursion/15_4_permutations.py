
################# GEEKS FOR GEEKS. -- https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/


# RECURSIVE - PERMUTATIONS - Print permutations of a given list
def permutation(L1):

    # EDGE CASE: If L1 is empty then there are no permutations
    if len(L1) == 0:
        return []
 
    # BASE CASE: If there is only one element in L1 then, only
    # one permutation is possible
    if len(L1) == 1:
        return [L1]
 
    # RECURSIVE CASE = INSIDE 2 LOOPS.
    # Find the permutations for L1 if > 1 chars.

    current_perm = [] # empty list that will store current permutation
 
    # Iterate the input(L1) and calculate the permutation
    for i in range(len(L1)):
       this_one = L1[i]
 
       # Extract L1[i] or m from the list.  remLst is
       # remaining list
       remLst = L1[:i] + L1[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           current_perm.append([this_one] + p)
    return current_perm
 
 
# Driver program to test above function
inputs = list('123')
result = permutation(inputs)
for p in result:
    print (p)
print(f"Num perms = {len(result)}")




################# EPI 

from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        # Try every possibility for A[i].
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            # Generate all permutations for A[i + 1:].
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result: List[List[int]] = []
    directed_permutations(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
