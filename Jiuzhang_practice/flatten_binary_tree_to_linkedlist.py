# dfs的方法， recursively build tree
# 这个方法是post order traversal， 首先处理好左右子树，然后处理当前节点。
# 假设在一个node 左边和右边都已经搭好Linkedlist， 那么我们需要以下操作：
# 1。将左边list 的尾巴和右边node连起来 2。将右边node 重新定义为左边node， 3， 将左边node设为None


# helper function
# input: 当前的root
# output：end node of the flattened list（需要知道变换list的尾巴是什么）

# 以下的两种方法差不多， 第一种方法直接点
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.helper(root)

    def helper(self, root):
        if root.left is None and root.right is None:
            return root
        elif root.left is None:
            return self.helper(root.right) # return tail of the flattened list
        elif root.right is None:
            left_end = self.helper(root.left)
            root.right = root.left
            root.left = None
            return left_end
        else:
            left_end = self.helper(root.left)
            right_end = self.helper(root.right)
            temp = root.right
            root.right = root.left
            left_end.right = temp
            root.left = None
            return right_end


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)

    def dfs(self, root):
        if not root:
            return None

        left_tail = self.dfs(root.left)
        right_tail = self.dfs(root.right)

        if not left_tail and not right_tail:  # corner case 1
            return root
        elif not left_tail:  # corner case 2
            return right_tail
        elif not right_tail:  # corner case 3
            root.right = root.left
            root.left = None
            return left_tail
        else:  # normal case
            left_tail.right = root.right
            root.right = root.left
            root.left = None
            return right_tail


