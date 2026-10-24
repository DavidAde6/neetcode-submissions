# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # recursion, go down, is None return 0
        # return max of the node itself, the node plus its left, the node plus its right.
        # update max to be the max of the above including the max between the left and right, and its self

        self.res = root.val
        def dfs(node):
            if not node:
                return 0
            
            nodeMax = node.val
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            bothMax = nodeMax + leftMax + rightMax

            maxEach = max(nodeMax, nodeMax + leftMax, nodeMax + rightMax)
            self.res = max(maxEach, bothMax, self.res)

            return maxEach

        dfs(root)
        return self.res