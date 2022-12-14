# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                isLeftSame  = self.isSameTree(p.left, q.left)
                isRightSame = self.isSameTree(p.right, q.right)
                return isLeftSame and isRightSame
            else:
                return False
        else:
            return False