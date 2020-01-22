class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        return self.dfs(root, 0, sum)

    def dfs(self, root, current_sum, sum):
        if root.left is None and root.right is None:
            if current_sum + root.val == sum:
                return True
            else:
                return False

        if root.left:
            is_left = self.dfs(root.left, current_sum + root.val, sum)
        if root.right:
            is_right = self.dfs(root.right, current_sum + root.val, sum)
        if root.left and root.right:
            return is_left or is_right
        if root.left:
            return is_left
        if root.right:
            return is_right

# 这道题类似于Binary tree path， 用dfs即可。
# 这里面主要是要注意 termination condition， 我们要在root.left and root.right 同时不存在的时候check

# 另一种写法
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.sum = sum
        return self.dfs(root, root.val)

    def dfs(self, root, current_sum):
        if root.left is None and root.right is None:
            if current_sum == self.sum:
                return True
            else:
                return False
        if root.left and root.right:
            left = self.dfs(root.left, current_sum + root.left.val)
            right = self.dfs(root.right, current_sum + root.right.val)
            return left or right
        if root.left:
            return self.dfs(root.left, current_sum + root.left.val)
        if root.right:
            return self.dfs(root.right, current_sum + root.right.val)

# 第三种写法， 后加值， 为什么不用backtrack？
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.sum = sum
        return self.dfs(root, 0)

    def dfs(self, root, current_sum):
        current_sum += root.val
        if root.left is None and root.right is None:
            if current_sum == self.sum:
                return True
            else:
                return False
        if root.left and root.right:
            left = self.dfs(root.left, current_sum)
            right = self.dfs(root.right, current_sum)
            return left or right
        if root.left:
            return self.dfs(root.left, current_sum)
        if root.right:
            return self.dfs(root.right, current_sum)
