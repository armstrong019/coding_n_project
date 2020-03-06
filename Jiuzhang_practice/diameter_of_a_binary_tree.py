# 这道题和之前的maximum depth of bianry tree 基本一致稍作改动。
# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         self.longest_path = 0
#         p = self.dfs(root)
#         return self.longest_path
#
#     def dfs(self, root):
#         if not root:
#             return 0
#         left_max_len = self.dfs(root.left)
#         right_max_len = self.dfs(root.right)
#         total_len = left_max_len + right_max_len
#         if total_len > self.longest_path:
#             self.longest_path = total_len
#         return max(left_max_len, right_max_len) + 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def diameterOfBinaryTree0(root):
    diameter = 0
    def dfs(root):
        # 在这个function里面diameter可见 可以用于计算 但是不可以更改， 如果update了就会报错
        nonlocal diameter # 用nonlocal来解决这个问题
        if not root:
            return 0
        left_len = dfs(root.left)
        right_len = dfs(root.right)
        total_len = left_len + right_len
        if total_len > diameter:
            diameter = total_len
        return max(left_len, right_len) + 1
    _ = dfs(root)
    return diameter



def diameterOfBinaryTree(root):
    diameter = [0] # 另一个解决办法是用一个list
    def dfs(root, diameter):
        if not root:
            return 0
        left_len = dfs(root.left,diameter)
        right_len = dfs(root.right,diameter)
        total_len = left_len + right_len
        if total_len > diameter[0]:
            diameter[0] = total_len
        return max(left_len, right_len) + 1
    _ = dfs(root,diameter)
    return diameter[0]


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
x = diameterOfBinaryTree(root)
print(x)


