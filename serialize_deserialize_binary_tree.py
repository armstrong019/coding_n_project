class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def __init__(self):
        self.string = []

    def serialize(self, root):
        # write your code here
        if root is None:
            self.string.append('#')
            return
        self.string.append(str(root.val))

        self.serialize(root.left)
        self.serialize(root.right)
        return self.string
#
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None
#
#
# class Solution:
#     def serialize(self, root):
#         # write your code here
#         if not root:
#             return ['#']
#         ans = [str(root.val)]
#         #ans.append(str(root.val))
#         ans += self.serialize(root.left)
#         ans += self.serialize(root.right)
#         return ans

    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        return self.dfs(data)

    def dfs(self, data):
        ch = data.pop(0)
        if ch == '#':
            return None
        else:
            root = TreeNode(ch)
        root.left = self.dfs(data)
        root.right = self.dfs(data)
        return root

x = TreeNode(1)
x.left =TreeNode(2)
x.right = TreeNode(3)
x.left.left = TreeNode(4)
x.left.right = TreeNode(5)

s = Solution()
print(s.serialize(x))

# 这道题目考量了dfs. serialize比较直接
# deserialize的时候利用深搜的顺序 每次pop出一个值将这个值赋予当前的root。 如果遇到# 说明已经到达树的最底端，要返回（None），然后根据深搜的顺序拼起树的还没完成的那部分。
#            当每一步完成的时候返回当前root