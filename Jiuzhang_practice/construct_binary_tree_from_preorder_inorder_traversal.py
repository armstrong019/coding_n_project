class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

class Pre:
    def preorder(self, root):
        self.res = []
        self.dfs(root)
        return self.res
    def dfs(self, root):
        self.res.append(root.val)
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)

x = Pre()
print(x.preorder(a))


res = []
class In:
    def inorder(self, root):
        self.res = []
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if root.left:
            self.dfs(root.left)
        self.res.append(root.val)
        if root.right:
            self.dfs(root.right)

x = In()
print(x.inorder(a))


res = []
class Post:
    def postorder(self, root):
        self.res = []
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
        self.res.append(root.val)


x = Post()
print(x.postorder(a))


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(preorder[0]) # preorder 的第一个值是root
        root_pos = inorder.index(preorder[0]) # 利用index 找到左边subtree的大小
        root.left = self.buildTree(preorder[1:1 + root_pos], inorder[:root_pos])
        root.right = self.buildTree(preorder[root_pos + 1:], inorder[root_pos + 1:])
        return root

#这道题用bfs
        # preorder： root， left sub， right sub
        # inorder： left sub， root， right sub
        # postorder： left sub， right sub， root
# inorder 把tree分成左右两部分， 左边是left sub inorder tree， 右边是right sub inoder tree