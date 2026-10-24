# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # at root, its a valid rv node, so add to res, run get next rv, 
        # dfs each node passes in its own height from 0 to n
        # its compared with len of res

        res = []

        def dfs(node, height):
            if not node:
                return
            if height == len(res):
                res.append(node.val)
            dfs(node.right, height + 1)
            dfs(node.left, height + 1)
            return

        dfs(root, 0)
        return res