# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #
        # Run ur search, if its false, run search on children, if any is true return true

        def search(node, s):
            if not s and not node:
                return True

            if not s or not node:
                return False

            if node.val == s.val:
                return search(node.left, s.left) and search(node.right, s.right)
            else:
                return False

        def dfs(node, s):
            if search(node, s): return True
            if not node:
                return False
            return dfs(node.left, s) or dfs(node.right, s)

        return dfs(root, subRoot)