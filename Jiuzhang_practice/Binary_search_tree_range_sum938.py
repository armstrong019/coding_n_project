# 这道题是一道简单的tree 的 bfs
# 最直接的想法是traverse tree 然后判断当前值是否 在两个给定值之间 是的话 就加上， 不是的话就不加 time complexity O（n）
# 可以做一些优化--剪枝， 如果当前值小于L， 那么我们只需要往右边走， 如果前值大于R， 那么我们只需要往左边走， 否则两边走
# 值得注意的是total sum 这个值的传递。 如果total_sum 是一个int 然后传递到function里面对其进行操作， 在外面的值是不会改变的
# total 相当于每次都创建了一个新的对象 （有了新的地址）
# 解决方法有两种， 一种是将结果作为dfs的输出传出来（略麻烦）， 另外一种是直接用一个list hold 这个值（方便）
# 参见 Nested List weight Sum 这道题
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        total_sum = [0]
        self.dfs(root, total_sum, L, R)
        return total_sum[0]

    def dfs(self, root, total_sum, L, R):
        if not root:
            return
        if root.val >= L and root.val <= R:
            total_sum[0] += root.val
            self.dfs(root.left, total_sum, L, R)
            self.dfs(root.right, total_sum, L, R)
        elif root.val < L:
            self.dfs(root.right, total_sum, L, R)
        else:
            self.dfs(root.left, total_sum, L, R)
