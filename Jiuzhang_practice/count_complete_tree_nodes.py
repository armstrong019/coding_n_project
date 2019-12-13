# 方法一： 直接上深搜
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = self.dfs(root)
        return count

    def dfs(self, root):
        if root is None:
            return 0
        count_left = self.dfs(root.left)
        count_right = self.dfs(root.right)
        return count_left + count_right + 1


# 方法二： 最直接方法
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        left_depth = 0
        right_depth = 0

        node1 = root # 计算当前节点为root的tree 的最左支的高度，和最右支的高度
        while node1:
            node1 = node1.left
            left_depth += 1

        node2 = root
        while node2:
            node2 = node2.right
            right_depth += 1
        if left_depth == right_depth: #如果两个高度一样，那么 则是完全树，节点个数可以计算出来， 返回
            return 2 ** left_depth - 1
        else: # 如果不一样那么是左边的节点数加上右边的节点数+1
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# 方法三： divide and conque, 利用complete tree的性质。
class Solution:
    def countNodes(self, root):
        leftdepth = self.getdepth(root, True) # 求一个tree最左边那支的长度。
        rightdepth = self.getdepth(root, False)# 求一个tree最右边那支的长度。

        if leftdepth == rightdepth:
            return 2 ** leftdepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getdepth(self, root, isLeft):
        if root is None:
            return 0
        if isLeft:
            return 1 + self.getdepth(root.left, isLeft)
        else:
            return 1 + self.getdepth(root.right, isLeft)
