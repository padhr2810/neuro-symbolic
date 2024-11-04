"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to 
the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # TRICK: INITIALISE 'LEFT_SUM" AS ZERO, AND 'RIGHT_SUM' AS SUM OF ALL VALUES
        #           THEN SIMPLY ITERATE THROUGH ARR WITH '+=' AND '-=' UNTIL THEY'RE EQUAL.
        
        left_sum, right_sum = 0, sum(nums)
        for i, x in enumerate(nums):
            right_sum -= x
            if left_sum == right_sum:
                return i
            left_sum += x
        return -1
   
soln = Solution()
assert soln.pivotIndex(nums = [1,7,3,6,5,6]) ==   3 
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

assert soln.pivotIndex(nums = [1,2,3]) ==   -1
# There is no index that satisfies the conditions in the problem statement.

assert soln.pivotIndex(nums = [2,1,-1]) ==   0
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
