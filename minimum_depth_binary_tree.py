"""
comment: basic dfs structure
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return 0
        minh_left = self.helper(root.left)
        minh_right = self.helper(root.right)
        if root.left is None:
            # is left is None, then by definition, the depth is defined by the right side
            return 1 + minh_right
        if root.right is None:
            return 1 + minh_left
        return 1 + min(minh_left, minh_right)
