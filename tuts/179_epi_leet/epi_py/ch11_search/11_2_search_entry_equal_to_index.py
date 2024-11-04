
import functools
from typing import List



def distinct_search_entry_equal_to_its_index(A: List[int]) -> int:
    """
    NO DUPLICATES ALLOWED!! 
    SO WE ONLY LOOK TO THE LEFT IF VALUE > INDEX.
    """
    print(f"\n\n\n\n\n\n#######################################################################")
    print(f"array: {A}")
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"\nleft, right, mid = {left}, {right}, {mid}")
        difference = A[mid] - mid
        print(f"A[mid], mid, difference = {A[mid]}, {mid}, {difference}")
        # A[mid] == mid if and only if difference == 0.
        if difference == 0:
            return mid
        elif difference > 0:
            print("          #####LOOK ON LEFT SIDE!!!")
            right = mid - 1
        else:  # difference < 0.
            print("          #####LOOK ON RIGHT SIDE!!!")
            left = mid + 1
    return -1

### LOOK LEFT:
A = [-1,0,1,3,6,7,8,9,11,12,14,15,16,17]
x = distinct_search_entry_equal_to_its_index(A)
print(x)

### LOOK RIGHT:
A = [-1,0,1,2,3,4,5,6,7,8,10,12,13,14]
x = distinct_search_entry_equal_to_its_index(A)
print(x)
