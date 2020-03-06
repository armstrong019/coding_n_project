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

#BFS 用queue去实现。这个是后来写的， 比较好理解
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res  = []
        q = deque([root])
        while q:
            level = []
            while q:
                level.append(q.popleft())
            res.append([nd.val for nd in level])
            for node in level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
