
"""
Given an array of integers arr, return TRUE if the number of 
occurrences of each value in the array is unique or FALSE otherwise.
"""

from collections import Counter 
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        # TRICK: USE INBUILT 'COUNTER'
        #        THEN COMPARE LEN OF LIST VS LEN OF SET, TO CHECK IF DUPS.
        
        cnt = Counter(arr)
        return len(set(cnt.values())) == len(cnt)
        

soln = Solution()
assert soln.uniqueOccurrences(arr = [1,2,2,1,1,3]) == True 
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
# No two values have the same number of occurrences.

assert soln.uniqueOccurrences(arr = [1,2]) == False 
assert soln.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]) == True  
