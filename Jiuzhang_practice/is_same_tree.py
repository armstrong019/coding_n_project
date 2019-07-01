# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None and q is not None or q is None and p is not None or p.val != q.val:
            return False

        compare_left = self.isSameTree(q.left, p.left)
        compare_right = self.isSameTree(p.right, q.right)

        return compare_left and compare_right

