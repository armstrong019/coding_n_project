# Binary tree right side view
# 第一种方法是利用BFS 遍历 然后记录每层的最后一个value
# 第二种方法是利用DFS 遍历，每次都先走最右边。关键的点是要理解 如果在每个节点上都是选择右边先走， 那么每层第一个被
# visit 的一定是最右边的点（举例子看看），这一点很巧妙。

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity O(N), space complexity: O(D): diameter of the tree: 树的最宽的一层
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            level = [] # 一次处理一层
            while q:
                current_node = q.popleft()
                level.append(current_node)
            res.append(level[-1].val) # 将这一层的最后一个元素放进结果里面
            for node in level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

# time complexity O(N), space complexity: O(H): height of the tree: 树的最宽的一层
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if len(res) == level:
            res.append(root.val)
        if root.right:
            self.dfs(root.right, level + 1, res)
        if root.left:
            self.dfs(root.left, level + 1, res)


