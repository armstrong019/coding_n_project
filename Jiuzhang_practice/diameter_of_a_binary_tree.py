# 这道题和之前的maximum depth of bianry tree 基本一致稍作改动。
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.longest_path = 0
        p = self.dfs(root)
        return self.longest_path

    def dfs(self, root):
        if not root:
            return 0
        left_max_len = self.dfs(root.left)
        right_max_len = self.dfs(root.right)
        total_len = left_max_len + right_max_len
        if total_len > self.longest_path:
            self.longest_path = total_len
        return max(left_max_len, right_max_len) + 1
