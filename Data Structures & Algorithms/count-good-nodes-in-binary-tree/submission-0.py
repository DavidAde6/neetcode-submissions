# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # increase on its descent
        # create a recursive function, pass in a var called bar, which is the current thing to compare with, which is the max of the nodes connections.
        # i want a solution that works with me just passing in root and its val
        # global var count

        self.count = 0

        def dfs(node, val):
            if not node:
                return
            if node.val >= val:
                self.count += 1
                val = node.val
                print(val)
            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, root.val)
        return self.count