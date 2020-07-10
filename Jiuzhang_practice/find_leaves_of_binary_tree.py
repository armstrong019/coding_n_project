# 这道题我用了两种解法，
# 第一种比较麻烦， 用dfs的方法， loop through tree x times （x is the depth of the tree）
# 每次一旦找到一个leaf node 就将其设置为None， 然后将当前的leaf node记录进结果里面， 这样做的复杂度比较大

# 第二种方法是记录tree的深度。 根据每一个node的深度我们可以知道他应该在的位置， 面试的时候写这个
                1  （depth 3）
               / \
 （depth 2）  2   3 （depth 1）
             / \
（depth 1） 4   5  （depth 1）


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        # this method is used to find the depth of the binary tree
        level_record = []
        max_depth = self.dfs(root, level_record)
        result = [[] for _ in range(max_depth)]
        for i in range(len(level_record)):
            val = level_record[i][0]
            pos = level_record[i][1]
            result[pos].append(val)
        return result


    def dfs(self, root, level_record):
        if not root:
            return 0
        left_depth = self.dfs(root.left ,level_record)
        right_depth = self.dfs(root.right, level_record)
        current_depth = 1+ max(left_depth, right_depth)
        level_record.append((root.val, current_depth - 1))
        return current_depth

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict

def dfs(root, dic):
    if not root:
        return 0
    left_depth = dfs(root.left, dic)
    right_depth = dfs(root.right, dic)
    current_depth = 1+max(left_depth, right_depth)
    dic[current_depth].append(root.val)
    return current_depth

def find_leaves(root):
    dic = defaultdict(list)
    depth = dfs(root, dic)
    result = [[] for _ in range(depth)]
    for key in dic:
        result[key-1] = dic[key]
    return result

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e

print(find_leaves(a))

# 这个是复杂度高的写法
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        while root.left is not None or root.right is not None:
            current_path = []
            _ = self.dfs(root, current_path)
            result.append(current_path[:])
        result.append([root.val])
        return result

    def dfs(self, root, current_path):
        if not root:
            return False
        if root.left is None and root.right is None:
            current_path.append(root.val)
            return True

        is_left_leaf = self.dfs(root.left, current_path)
        is_right_leaf = self.dfs(root.right, current_path)
        if is_left_leaf:
            root.left = None
        if is_right_leaf:
            root.right = None
        return False





