class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.left, p,q) #剪枝并且继续深搜
        if root.val>p and root.val>q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root

# 这道题主要是充分用到了bst的特性， 当dfs递归的时候， 由上至下的过程，我们遇到的第一个 root.val in between p.val and q.val的root就是lca
# 那么这时候立刻返回root；
# 否则那么只能存在root.val 比两个都小或两个都大的情况， 这样就可以剪枝并且继续深搜