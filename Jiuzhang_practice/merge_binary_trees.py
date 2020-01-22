# 以下这两种写法 都可以。第二种写法更巧妙一点
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = self.dfs(t1,t2)
        return root
    def dfs(self, root1, root2):
        if not root1 and not root2:
            return None
        elif not root2:
            root = TreeNode(root1.val)
            root.left = self.dfs(root1.left, None)
            root.right = self.dfs(root1.right, None)
        elif not root1:
            root = TreeNode(root2.val)
            root.left = self.dfs(None, root2.left)
            root.right = self.dfs(None, root2.right)
        else:
            root = TreeNode(root1.val+root2.val)
            root.left = self.dfs(root1.left, root2.left)
            root.right = self.dfs(root2.left, root2.right)
        return root

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = self.dfs(t1,t2)
        return root
    def dfs(self, root1, root2):
        if not root1 and not root2:
            return None
        elif not root2:
            return root1
        elif not root1:
            return root2
        else:
            root = TreeNode(root1.val+root2.val)
            root.left = self.dfs(root1.left, root2.left)
            root.right = self.dfs(root1.right, root2.right)
            return root

