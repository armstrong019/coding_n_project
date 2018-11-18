"""
Definition of TreeNode:

"""


# class Solution:
#     """
#     @param root: the root of the binary tree
#     @return: all root-to-leaf paths
#     """
#
#     def binaryTreePaths(self, root):
#         # write your code here
#         self.paths = []
#         self.find_paths(root, [])
#         return self.paths
#
#     def find_paths(self, root, prev_path):
#         if root.left is None and root.right is None:
#             self.paths.append(prev_path+[root.val])
#             return
#         if root.left is None:
#             self.find_paths(root.right, prev_path + [root.val])
#         elif root.right is None:
#             self.find_paths(root.left, prev_path + [root.val])
#         else:
#             self.find_paths(root.left, prev_path + [root.val])
#             self.find_paths(root.right, prev_path + [root.val])


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


