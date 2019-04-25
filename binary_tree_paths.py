

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        self.result = []
        current_path = [str(root.val)]
        self.dfs(root, current_path)
        return self.result

    def dfs(self, root, current_path):
        if root.left is None and root.right is None:
            self.result.append('<-'.join(current_path))
            current_path.pop()
            return
        if root.right is None:
            self.dfs(root.left, current_path+[str(root.left.val)])
            current_path.pop()
        elif root.left is None:
            self.dfs(root.right, current_path+[str(root.right.val)])
            current_path.pop()
        else:
            self.dfs(root.left, current_path+[str(root.left.val)])
            self.dfs(root.right, current_path+[str(root.right.val)])


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)

a.left = b
a.right = c
b.right = d

x = Solution()

print(x.binaryTreePaths(a))

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def __init__(self):
        self.result = []

    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        self.dfs(root, [str(root.val)])
        return self.result

    def dfs(self, root, path):
        if root.left is None and root.right is None:
            path_find = '->'.join(path)
            self.result.append(path_find)
        if root.left is not None:
            self.dfs(root.left, path + [str(root.left.val)])
        if root.right is not None:

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def __init__(self):
        self.result = []

    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        self.dfs(root, [])
        return self.result

    def dfs(self, root, path):
        path.append(str(root.val))
        if root.left is None and root.right is None:
            path_find = '->'.join(path)
            self.result.append(path_find)
        if root.left is not None:
            self.dfs(root.left, path)
        if root.right is not None:
            self.dfs(root.right, path)
        path.pop()

#这里面有三种解法： 第二三类似。 区别在于第二种在每一步前先把节点加入， 第三种是后把节点加入， 如果是后加的，那么要在最后一步把最后点pop出来