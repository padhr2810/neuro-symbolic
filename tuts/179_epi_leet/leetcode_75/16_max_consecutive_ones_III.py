
"""
Given a binary array "nums" and an integer "flips_allowed" , return the maximum number of 
consecutive 1's in the array if you can flip at most 'flips_allowed' 0's.
"""

class Solution(object):
    def longestOnes(self, nums, flips_allowed):

        """
        :type nums: List[int]
        :type flips_allowed: int
        :rtype: int
        """
        
        ### TRICK: INITIALISE 2 POINTERS - FAST & SLOW AT THE START OF ARRAY.
        ###    MAIN LOOP SIMPLY ITERATES THROUGH 'fast_index' 
        ###    WHEN REACH THE "count_flips" LIMIT, THE 'slow_index' ADVANCES PAST THE NEXT '0'
    
        ans = 0
        count_flips = slow_index = 0
        
        for fast_index, val in enumerate(nums):
        
            if val == 0:            ### FLIP.
                count_flips += 1
            
            while count_flips > flips_allowed:  ##### THIS ONLY TRIGGERED WHEN NUM FLIPS EXCEEDS 'flips_allowed'
                if nums[slow_index] == 0:                ##### B START OF SEQUENCE
                    count_flips -= 1
                slow_index += 1
            print(f"\n### Iter fast_index = {fast_index}; .... slow_index = {slow_index}; .... ans = {ans}; .... fast_index - slow_index + 1 = {fast_index - slow_index + 1}")
            ans = max(ans, fast_index - slow_index + 1)
        return ans
        
soln = Solution()
assert soln.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], flips_allowed = 2) == 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


assert soln.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], flips_allowed = 3) == 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
