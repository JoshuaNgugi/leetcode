# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if root is None else self.mirrorVisit(root.left, root.right)

    def mirrorVisit(self, left, right):
        if left is None and right is None:
            return True
        try:
            return bool(
                left.val == right.val
                and self.mirrorVisit(left.left, right.right)
                and self.mirrorVisit(left.right, right.left)
            )
        except:
            return False