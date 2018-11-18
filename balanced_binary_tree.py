"""
comments:
helper function 记录两个内容： 一个是是否balance， 一个是当前高度, algorithm一直往下走， 走到子节点 然后再check balance 之后返回。

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        isbalanced, _ = self.validate(root)
        return isbalanced

    def validate(self, root):
        if root is None:
            return True, 0
        isbalancedh, lefth = self.validate(root.left)
        if not isbalancedh:
            return False, 0  # if false, depth does not matter
        isbalancedr, righth = self.validate(root.right)
        if not isbalancedr:
            return False, 0
        return abs(lefth - righth) <= 1, 1 + max(lefth, righth)
        # if root.left and root.right node all balanced, then check the current root node


