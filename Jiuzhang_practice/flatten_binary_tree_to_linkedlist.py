# dfs的方法， recursively build tree
# 假设在一个node 左边和右边都已经搭好Linkedlist
# 那么我们需要 1。 将左边list 的尾巴和右边node连起来 2。将右边node 重新定义为左边node， 3， 将左边node设为None

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
