
import bisect
from typing import List


def search_first_of_k(A: List[int], k: int) -> int:

    left, right, result = 0, len(A) - 1, -1
    # A[left:right + 1] is the candidate set.
    
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right of mid can be solution.
        else:  # A[mid] < k.
            left = mid + 1
    return result


# Pythonic solution
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


A = [0,1,1,1,2,2,3,4,4,4,5,6,7,8]
k = 4

if __name__ == "__main__":
    x = search_first_of_k(A, k)
    print(x)

