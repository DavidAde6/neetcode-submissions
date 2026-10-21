# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # keep a lowest variable starting at 5, when u go down check if any of those values are bigger than 5, if yes search the bottom 2, and keep going, if no lowestVariable belongs to the side they both on

        self.lowest = root
        def find(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return self.lowest
            
            if p.val > node.val and q.val > node.val:
                if self.lowest == node:
                    self.lowest = node.right
                return find(node.right)
            
            if p.val < node.val and q.val < node.val:
                if self.lowest == node:
                    self.lowest = node.left
                return find(node.left)

            left = find(node.left)
            right = find(node.right)
            return left if left else right

        return find(root)
