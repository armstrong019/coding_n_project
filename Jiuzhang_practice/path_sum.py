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
