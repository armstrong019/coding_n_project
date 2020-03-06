# 2020, Jan 27
# 这道题的解题思路和我的思路有点出入。我的思路是从最底部开始，儿标准答案s
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    import sys

    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True
        MIN = -sys.maxsize - 1
        MAX = sys.maxsize

        return self.dfs(root, MIN, MAX)

    def dfs(self, root, Min, Max):
        if root is None:
            return True
        if root.val <= Min or root.val >= Max:
            return False
        else:
            left_valid = self.dfs(root.left, Min, root.val)
            right_valid = self.dfs(root.right, root.val, Max)
            return left_valid and right_valid


# 判断一个tree是不是binary search tree
"""
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
"""
# 条件的满足： 一个root点左子节点和右侧子节点同时满足，并且子节点的子节点也要满足。
# 需要进行深搜。 巧妙的点是将当前节点需要满足的最大最小值都当成状态变量记录下来
# 当我们由上至下从一个root 向root.left搜索的时候， 我们会更新root.left 的最大值不能超过 当前值。 右侧同理。
# termination condition有两种： 一种是到达最底层， 另一种是找到其中一个节点不符合要求，那么则返回到上一级 （剪枝）不再继续向下搜索
