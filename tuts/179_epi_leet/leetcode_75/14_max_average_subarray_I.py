
"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a CONTIGUOUS subarray whose length is equal to k that has the MAXIMUM average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        ### TRICK: Simply advance through array ; check / update the max_mean @ each step. 
        ###      TRICK: Sliding Window approach. DON'T need to add all up obviously. 
        ###          Each iteration: Just subtract the first num of old array. & add one new number for a new array.
        
        latest_sum  = float(sum(nums[:k]))
        max_mean    = float(latest_sum / k)     ## init the result.

        for i in range(k, len(nums)):        ## contiguous subarray = can't terminate before 'k' obviously.
            latest_sum    =    latest_sum - nums[i - k] + nums[i]       ## no need to add all up obviously.
            max_mean = max(latest_sum / k, max_mean)

        return max_mean
    
soln = Solution()
assert  soln.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4) == 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

assert  soln.findMaxAverage(nums = [5], k = 1) == 5.00000
