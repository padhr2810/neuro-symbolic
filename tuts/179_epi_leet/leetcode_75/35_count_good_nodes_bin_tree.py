
"""
Given a binary tree root, a node X in the tree is named good if 
in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, mx: int):
            if root is None:
                return
            nonlocal ans
            if mx <= root.val:
                ans += 1
                mx = root.val
            dfs(root.left, mx)
            dfs(root.right, mx)

        ans = 0
        dfs(root, -1000000)
        return ans
        
soln = Solution()
assert soln.goodNodes(root = [3,1,4,3,null,1,5]) == 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

assert soln.goodNodes(root = [3,3,null,4,2]) == 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

assert soln.goodNodes(root = [1]) == 1
# Explanation: Root is considered as good.
