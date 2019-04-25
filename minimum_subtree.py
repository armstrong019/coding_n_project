"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        self.result = None
        self.min_value = sys.maxsize
        self.find_minimum(root)
        return self.result

    def find_minimum(self, root):
        if root is None:
            return 0
        left_value = self.find_minimum(root.left)
        right_value = self.find_minimum(root.right)
        total_subtree_value = root.val + left_value + right_value

        #以下code是为了更新最小值何其对应点的记录用的
        if total_subtree_value < self.min_value:
            self.min_value = total_subtree_value  # update min value
            self.result = root

        return total_subtree_value


# dfs (分治算法)
# find_minimum function返回的是root这个subtree的加和值（并不是subtree的最小值）
# 我们通过dfs遍历了每一个节点， 每当经过一个节点都记录subtree的值
# 那么这道题为什么不用bfs？--可以 但是bfs需要记录每一个level的值直到走到最后一个level， by nature 要用dfs over bfs
