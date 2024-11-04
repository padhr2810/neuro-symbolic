
"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(root, l, r):
            if root is None:
                return
            nonlocal ans
            ans = max(ans, l, r)
            dfs(root.left, r + 1, 0)
            dfs(root.right, 0, l + 1)

        ans = 0
        dfs(root, 0, 0)
        return ans
        
soln = Solution()
assert soln.longestZigZag(root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]) == 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

assert soln.longestZigZag(root = [1,1,1,null,1,null,null,1,1,null,1]) == 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

assert soln.longestZigZag(root = [1]) == 0
