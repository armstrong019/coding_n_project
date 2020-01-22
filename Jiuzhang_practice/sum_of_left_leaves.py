# 用dfs 搜索， 只要是左半边点而且是叶节点 就加上

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum = 0
        self.dfs(root, False)
        return self.sum

    def dfs(self, root, flag):
        if not root:
            return
        if self.is_leaf(root) and flag:
            self.sum += root.val
        self.dfs(root.left, True)
        self.dfs(root.right, False)

    def is_leaf(self, root):
        if root is not None and root.left is None and root.right is None:
            return True
        return False

# 这种是别人的写法，
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        sum = self.dfs(root)
        return sum

    def dfs(self, root):
        if not root:
            return 0
        if self.is_leaf(root.left):
            return root.left.val + self.dfs(root.right)
        else:
            return self.dfs(root.left) + self.dfs(root.right)

    def is_leaf(self, root):
        if root is not None and root.left is None and root.right is None:
            return True
        return False
