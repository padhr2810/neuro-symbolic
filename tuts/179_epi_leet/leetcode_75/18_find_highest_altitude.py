
"""
There is a biker going on a road trip. 
The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in 
altitude between points i and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.
"""
import itertools 
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        ### TRICK: USE THE "initial=0" PARAMETER OF "accumulate" 
        ###             OTHERWISE INITIALISES AS THE FIRST VALUE OF ARRAY, WHICH IS PROB NOT ZERO.

        """
        highest = 0
        current = 0
        for g in gain:
            current += g
            if current > highest:
                highest = current
        return highest
        """
        return max(itertools.accumulate(gain, initial=0))  # MORE COMPACT CODE...

soln = Solution()
assert soln.largestAltitude(gain = [-5,1,5,0,-7]) == 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

assert soln.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]) == 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
