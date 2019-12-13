class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.left, p,q) #剪枝并且继续深搜
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root



# 这道题主要是充分用到了bst的特性， 当dfs递归的时候， 由上至下的过程，我们遇到的第一个 root.val in between p.val and q.val的root就是lca
# 那么这时候立刻返回root；
# 否则那么只能存在root.val 比两个都小或两个都大的情况， 这样就可以剪枝并且继续深搜

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None
        lca = self.dfs(root, A, B)
        return lca

    def dfs(self, root, A, B):
        if root is None:
            return None
        if root == A or root == B:
            return root

        left_node = self.dfs(root.left, A, B)
        right_node = self.dfs(root.right, A, B)
        if left_node and right_node:
            return root
        if left_node:
            return left_node
        if right_node:
            return right_node
        return None
