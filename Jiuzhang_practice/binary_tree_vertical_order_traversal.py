# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dic = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            nodes = []
            while queue:
                nodes.append(queue.popleft())

            for node, col in nodes:
                dic[col].append(node.val)
                if node.left:
                    queue.append([node.left, col - 1])
                if node.right:
                    queue.append([node.right, col + 1])
        res = dic.items()
        res = sorted(res, key=lambda x: x[0]) # 这个特容易写错。我当时写成了res.sort(key=lambda x: x[0]) 报错"dict——item does not have attribute sort"
        return [x[1] for x in res]
