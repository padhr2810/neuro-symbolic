
"""
- You are given an integer array nums and an integer k.
- In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
- Return the maximum number of operations you can perform on the array.
"""

class Solution:
    def maxOperations(self, nums, k: int) -> int:
    
        ### TRICK: SORT ARRAY.
        ###        THEN: USE 2x POINTERS @ LEFT / RIGHT.
        ###         CHECK IF THE 2 POINTERS ADD TO TARGET NUMBER.
        ###             IF YES: ADVANCE BOTH POINTERS 
        ###             IF NO: JUST ADVANCE 1 POINTER.
        
        nums.sort()
        left, right, result = 0, len(nums) - 1, 0
        while left < right:
            added = nums[left] + nums[right]
            if added == k:
                result += 1
                left += 1 
                right -= 1
            elif added > k:    #### ANALAGOUS TO BIN SEARCH BUT START FROM THE 2 ENDS.
                right -= 1
            else:
                left += 1
        return result
        
soln = Solution() 
assert  soln.maxOperations(nums=[1,2,3,4], k=5) == 2
assert  soln.maxOperations(nums=[4,1,2,3], k=5) == 2
assert  soln.maxOperations(nums=[1,3,4,2], k=5) == 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

assert  soln.maxOperations([3,1,3,4,3], k = 6) == 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
