# 这道题dfs 的部分很简单， 但是后面处理的部分比较复杂，我用了list 没有用dictionary。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        self.dfs(root, 0, 0)
        sorted_result = sorted(self.result)
        res = [[sorted_result[0][2]]]
        for i in range(1, len(sorted_result)):
            if sorted_result[i][0] > sorted_result[i - 1][0]:
                res.append([sorted_result[i][2]])
            else:
                res[-1].append(sorted_result[i][2])
        return res

    def dfs(self, root, x, y):
        if not root:
            return
        self.result.append((x, y, root.val))
        self.dfs(root.left, x - 1, y + 1)
        self.dfs(root.right, x + 1, y + 1)
