
"""
Given the root of a binary tree and an integer targetSum, 
return the number of paths 
where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, 
but it must go downwards (i.e., traveling only from parent nodes to child nodes).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, s):
            if node is None:
                return 0
            s += node.val
            ans = cnt[s - targetSum]
            cnt[s] += 1
            ans += dfs(node.left, s)
            ans += dfs(node.right, s)
            cnt[s] -= 1
            return ans

        cnt = Counter({0: 1})
        return dfs(root, 0)
        
soln = Solution()
assert soln.pathSum(root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8) == 3
# Explanation: The paths that sum to 8 are shown.

assert soln.pathSum(root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22) == 3
