
"""
comments: 2 method
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here
        upper = root
        lower = root
        while root:
            if root.val > target:
                upper = root
                root = root.left
            else root.val <= target:
                lower = root
                root = root.right
            else:
            return root.val

    if abs(upper.val - target) > abs(lower.val - target):
        return lower.val
    return upper.val





class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code
        lower_node = self.find_lower(root, target)
        upper_node = self.find_upper(root, target)

        if lower_node is None:
            return upper_node.val
        elif upper_node is None:
            return lower_node.val
        else:
            if abs(lower_node.val - target) < abs(upper_node.val - target):
                return lower_node.val
            else:
                return upper_node.val

    def find_lower(self, root, target):
        if root is None:
            return root
        if root.val > target:
            return self.find_lower(root.left, target)
        else:
            lb = self.find_lower(root.right, target)
            if lb:
                return lb
        return root

    def find_upper(self, root, target):
        if root is None:
            return root
        if root.val < target:
            return self.find_upper(root.right, target)
        else:
            ub = self.find_upper(root.left, target)
            if ub:
                return ub
        return root

