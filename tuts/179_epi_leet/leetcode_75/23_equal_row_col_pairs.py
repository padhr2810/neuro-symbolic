
"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        ### TRICK: BRUTE FORCE CHECK (I.E. NESTED LOOP)
        ###         BUT USE 'all' SYNTAX FOR EFFICIENT ONE LINER INSIDE LOOP
        
        n = len(grid)
        ans = 0
        
        for i in range(n):
            for j in range(n):
                ans += all(grid[i][k] == grid[k][j] for k in range(n))
        return ans

        
soln = Solution()
        
assert soln.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]) == 1
# Explanation: There is 1 equal row and column pair:
#  (Row 2, Column 1): [2,7,7]

assert soln.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
# Explanation: There are 3 equal row and column pairs:
#  (Row 0, Column 0): [3,1,2,2]
#  (Row 2, Column 2): [2,4,2,2]
#  (Row 3, Column 2): [2,4,2,2]
