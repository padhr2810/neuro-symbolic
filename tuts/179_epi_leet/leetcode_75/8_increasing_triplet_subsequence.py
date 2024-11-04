
"""
type: greedy // array.
"""


"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
"""

"""
The time complexity of the given code is O(n) where n is the number of elements in the nums list. 
This is because the code iterates through the entire nums list once with a single loop, 
and within each iteration, it performs a constant number of operations.

The space complexity of the given code is O(1) regardless of the size of the input list. 
It uses only two extra variables, mi and mid, which consume a constant amount of space.
"""

"""
Intuition
As we iterate through the array, we can update smaller_of_3 and mid_of_3 whenever possible. 
The idea here is to maintain the lowest possible values for smaller_of_3, mid_of_3 as we move forward, 
giving us the best chance to find a number that would be greater than both, thus forming our triplet.

If the current number (num) is less than or equal to smaller_of_3, it becomes the new smaller_of_3 
because we're always interested in the smallest starting point of the potential triplet.
If num is greater than smaller_of_3 but less than mid_of_3, we have found 
a possible middle part of our triplet, so we set mid_of_3 to this new number.
If num is greater than mid_of_3, this means we have successfully found a triplet and we can return true.
This efficient approach uses a greedy-like method to continuously look for the most optimal smaller_of_3 and mid_of_3 
with the hope of finding a third number that could fit the sequence. 
It does so using a LINEAR SCAN and constant extra space, WITHOUT the need for sorting or extra arrays.

No additional data structures are necessary, 
making this solution notably efficient with O(n) time complexity (due to single iteration through the array) 
    and O(1) space complexity (using only two extra variables).
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ### TRICK - DONT NEED ALL 3 TO BE TOGETHER
        ###     CAN HAVE OTHERS IN BETWEEN
        ###     INITIALISE SMALL AND MID TO INF.
        ### WHEN FIND A NEW "smallest"
        ###     1. SET THE SMALLEST. 
        ###     BUT 2. DON'T RESET THE 'mid' - HENCE KEEP THE INFO FROM EARLIER "smallest" IN USE
        ###        GREEDY :D --- THIS TRACKS MULTIPLE MIN AT THE SAME TIME ESSENTIALLY I.E. RETAIN THE EARLIER 'mid' AND CAN USE THIS TO "return True"
        ###   USE <= (NOT <) SO IT DOESN'T INTERFERE WITH THE MID (I.E. DON'T TRIGGER THE 'ELSE' BELOW)

        smaller_of_3, mid_of_3 = float('inf'), float('inf')
        for num in nums:            ### CHECK ONE NUM AT A TIME.
        
            if num > mid_of_3:          ### FOUND THE BIGGEST.
                print(f"small = {smaller_of_3}; mid = {mid_of_3}; big = {num}")
                return True             ### MUST BE ASCENDING ORDER - SO ONLY THIRD (BIGGEST) NUM CAN TRIGGER "return True"
            
            if num <= smaller_of_3:         ###  FIND A NEW "smallest"
                smaller_of_3 = num          ### 
                
            else:                           ### OTHERWISE FOUND THE MIDDLE OBVIOUSLY.
                mid_of_3 = num
            
        return False
    
soln = Solution()
assert soln.increasingTriplet(nums = [1,2,3,4,5]) == True
# Explanation: Any triplet where i < j < k is valid.

assert soln.increasingTriplet(nums = [5,4,3,2,1]) == False 
# Explanation: No triplet exists.

assert soln.increasingTriplet(nums = [2,1,5,0,4,6]) == True  
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

assert soln.increasingTriplet(nums = [2,1,5,0,6]) == True  
#   Explanation: values = 2, 5, 6 ... ie indices 0, 2, 4

assert soln.increasingTriplet(nums = [2,3,1,5,0,4]) == True   
assert soln.increasingTriplet(nums = [2,3,3,5,0,4]) == True  

assert soln.increasingTriplet(nums = [1,2,3]) == True  
assert soln.increasingTriplet(nums = [2,1,3]) == False   
assert soln.increasingTriplet(nums = [2,1,0,3]) == False   
assert soln.increasingTriplet(nums = [2,2,0,3]) == False   



