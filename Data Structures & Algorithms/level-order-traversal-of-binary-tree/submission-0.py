# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursively pass in an index, a general array and yh
        res = []
        def getNext(index, node):
            if node is None:
                return

            if len(res) < index + 1:
                res.append([])

            res[index].append(node.val)

            getNext(index+1,node.left)
            getNext(index+1,node.right)

        getNext(0, root)
        return res