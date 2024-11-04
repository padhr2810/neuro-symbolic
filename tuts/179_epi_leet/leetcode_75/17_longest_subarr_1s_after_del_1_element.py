
"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


class Solution:
    def longestSubarray(self, nums) -> int:
        ### TRICK: CREATE 2 ARRS OF ZEROS FOR 'LEFT' AND 'RIGHT'
        ###     THEN DO THE CUMULATIVE '1s' FROM EACH EXTREME - SUCH THAT THEY CONVERGE ON THE SAME 'ZEROS'
        ###         I.E. A LAG OF 1 SPOT IN THE CUMULATIVE COUNT.
        ###         THEN GET THE MAX OF THE INTERSECTION OF LAGGED LEFT AND RIGHT COUNTS.
    
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):  
            if nums[i - 1] == 1:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right[i] = right[i + 1] + 1
        return max(a + b for a, b in zip(left, right))
        
soln = Solution() 
assert soln.longestSubarray(nums = [1,1,0,1]) == 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.


assert soln.longestSubarray(nums = [0,1,1,1,0,1,1,0,1]) == 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].


assert soln.longestSubarray(nums = [1,1,1]) == 2
# Explanation: You must delete one element.
