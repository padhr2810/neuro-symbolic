
"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height) -> int:
    
        ### TRICK: 2x POINTERS AT OPPOSITE END
        ###         AREA = (MINIMUM HEIGHT) * (HORIZONTAL DISTANCE)
        ###    EACH STEP, ADVANCE ONLY ONE POINTER ( @ THE SMALLER VERTICAL HEIGHT)
        
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            horizontal_len = (j-i)
            latest_area = horizontal_len * min(height[i], height[j])
            max_area = max(max_area, latest_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
        
soln = Solution()


assert soln.maxArea([1,8,6,2,5,4,8,3,7]) == 49
## Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
## In this case, the max area of water (blue section) the container can contain is 49.

assert soln.maxArea([1,1]) == 1
