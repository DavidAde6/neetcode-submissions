# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def length(self, root):
        if not root:
            return 0

        return max(1 + self.length(root.left), 1 + self.length(root.right))


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        currDiameter = self.length(root.left) + self.length(root.right)

        return max(currDiameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
