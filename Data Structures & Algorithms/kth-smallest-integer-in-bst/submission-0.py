# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # first smallest is the far left, u have no idea about indexes tho 
        # if u want first smallest u go all the way to the left, but if u want second smallest, go all the way to the right. I believe u have 

        self.size = 0
        self.res = root.val
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.size += 1
            if self.size == k:
                self.res = node.val
            dfs(node.right)
        dfs(root)
        return self.res
