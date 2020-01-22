# 模版题。
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.result.append(root.val)
        self.dfs(root.right)
