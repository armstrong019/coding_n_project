
# 最简单的方法是 inorder traversal BST 得到sorted array
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        values = []
        self.dfs(root, values)
        return values[k - 1]

    def dfs(self, root, values):
        if not root:
            return False
        self.dfs(root.left, values)
        values.append(root.val)
        self.dfs(root.right, values)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    res = None
    count = 0
    def dfs(root, k):
        nonlocal res  # nonlocal 表示外层变量，他会从外层读取变量。当内部
        nonlocal count
        if root is None:
            return
        dfs(root.left, k)
        count += 1
        if count == k and root is not None:
            res = root.val
        dfs(root.right, k)

    dfs(root, k)
    return res

a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(2)

a.left = b
a.right = c
b.right = d

print(kthSmallest(a, 3))
