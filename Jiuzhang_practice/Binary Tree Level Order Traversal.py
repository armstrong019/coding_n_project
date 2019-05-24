"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        queue = deque([root]) # 这里面必须要加方括号。
        res = []
        while queue:
            level = []
            for i in range(len(queue)):  # 注意queue在循环种变化， 但是len（queue）在第一次访问的时候就确定了
                root = queue.popleft() # 每一次拿出当前一级的一个点然后加入其对应的左右两个点
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(level)
        return res

#BFS 用queue去实现。