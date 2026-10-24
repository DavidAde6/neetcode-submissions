# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # left and right
        # the height of a node is 1 + the height of 
        # dfs has a length attribute. If none, height is 0, if 1, height is 1
        # if height of left and right difference is 2 or more, balanced = false
        self.balanced = True
        def dfs(node):
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            if abs(rightHeight - leftHeight) >= 2:
                self.balanced = False
            return max(leftHeight, rightHeight) + 1

        dfs(root)
        return self.balanced