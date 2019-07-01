# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque([root])
        res = []
        while q:
            nd = q.popleft()
            res.append(nd.val)
            if nd.left:
                q.append(nd.left)
            if nd.right:
                q.append(nd.right)
        return res

a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)
x = Solution()
print(x.levelOrder(a))
# 遍历所有node bfs