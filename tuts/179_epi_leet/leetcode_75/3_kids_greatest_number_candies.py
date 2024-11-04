"""
There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving 
the ith kid all the extraCandies, they will have the greatest number of candies 
among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        ### TRICK: SIMPLY ITERATE THROUGH THE ARRAY.
        ###    CHECK IF += NUMBER > THE BASELINE MAX.
        ###    APPEND THE true / false TO THE NEW ARRAY.
       
        result=[]
        greatestNumber =max(candies)
        for c in candies:
            if c + extraCandies >= greatestNumber:
                result.append(True)
            else:
                result.append(False)
        return result

sln=Solution()
assert [True,True,True,False,True] ==sln.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)
# Explanation: If you give all extraCandies to:
#    Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
#    Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
#    Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
#    Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
#    Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
assert [True,False,False,False,False]  ==sln.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1)
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

assert [True,False,True]  ==sln.kidsWithCandies(candies = [12,1,12], extraCandies = 10)

