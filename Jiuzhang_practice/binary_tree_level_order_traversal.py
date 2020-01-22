"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

#Binary tree level order traversal 2
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result= []
        q=deque([root])
        while q:
            level =[]
            while q: # 一次将queue 里面的东西都清空。 比较容易理解的做法。
                temp = q.popleft()
                level.append(temp)
            result.append([x.val for x in level])
            for node in level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return (result[::-1])
