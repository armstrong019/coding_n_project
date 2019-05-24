class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a = self.find_node(root, A)
        b = self.find_node(root, B)
        if a and b:
            return self.lowestCommonAncestor(root, A, B)
        else:
            return None

    def find_node(self, root, node):
        if root is None:
            return None
        if root == node:
            return node
        left_node = self.find_node(root.left, node)
        right_node = self.find_node(root.right, node)
        return left_node or right_node

    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None

        if root == A or root == B:
            return root

        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)

        if left_result and right_result:
            return root
        if left_result:
            return left_result
        if right_result:
            return right_result

# 区别于lca， 这里面其中一个值有可能不存在。 那么这样我们可以分两步来解决
# 第一部查找是否存在该点， 第二步调用lca