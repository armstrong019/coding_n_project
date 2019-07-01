"""
comments：
注意这里面A和B一定存在
dfs recursion function 输入是root， A，B； 输出是结果： 如果先找到A 则为A； 先找到B则为B 没找到则为None
这里面是分置算法， 左右两边分别深搜， 找到A或者B其中一个即返回。
e.g. 如果left-result 或者right-result其中一个为A， 另外一个为B， 那么当前的root即为lca
     如果left-result 或者right-result其中一个为A（或B）， 另外一个为None， 那么A和B在以当前root为subtree的里面。当前的root就是lca 返回result到上一级


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root == []:
            return None
        lca = self.dfs(root, A, B)
        return lca

    def dfs(self, root, A, B):
        if root == A or root == B:
            return root
        if root is None:
            return None
        left_node = self.dfs(root.left, A, B)
        right_node = self.dfs(root.right, A, B)

        if left_node and right_node:
            return root
        if left_node:
            return left_node
        if right_node:
            return right_node
        return None

# 这道题充分利用了dfs backtrack的特性。
# recursion function 的输入是root， A，B， 输出是以 root为顶的subtree 是否存在 A，B 的 lowest common ancestor， 如果存在返回lca， 不存在返回None
# 在dfs回溯的过程中，如果root.left 和 root.right都有返回点， 那么root就一定是lca， 除此之外其他任何一个点都不具备这个特点。