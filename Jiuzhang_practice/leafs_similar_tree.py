# 简单的方法， 分别找leafs
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        result1, result2 = [], []
        self.find_leaves(root1, result1)
        self.find_leaves(root2, result2)
        return result1 == result2

    def find_leaves(self, root, result):
        if root.left is None and root.right is None:
            result.append(root.val)
            return
        if root.left is not None:
            self.find_leaves(root.left, result)
        if root.right is not None:
            self.find_leaves(root.right, result)

