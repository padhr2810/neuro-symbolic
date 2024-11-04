
"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""


class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        # TRICK: USE SUBTRACTION OPERATOR FOR SETS.
        
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
        
soln = Solution() 
assert soln.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]) == [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, 
# whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. 
# Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, 
# whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. 
# Therefore, answer[1] = [4,6].

assert soln.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]) == [[3],[]]
# For nums1, nums1[2] and nums1[3] are not present in nums2. 
# Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
