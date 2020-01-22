# 这里面有一个知识点， 是对于BST 他的inorder traversal 的visit的顺序是从小到大的
# 这个题目简单暴力的做法是三步走
# 1。 inorder traversal 打印出所以点的值
# 2。 Find mistake positions
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        minimum = -sys.maxsize
        maximum = sys.maxsize
        self.nums = []
        self.inorder_traversal(root)
        x, y = self.find_two_swapped()
        self.recover_tree(root, x, y)

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        self.nums.append(root.val)
        self.inorder_traversal(root.right)

    def find_mistake(self): # 两个例子 【1，2，3，4，5，6，17，8，10，11，12，14， 15，7，20】，【2，1，3】
        # 用前一个和后一个对比， 如果后一个小，那么第一次遇到的话是前一个有错， 第二次遇到这个情况是后一个有错。
        # 有一种特殊情况是相邻的两个数字被swap了 【2，1，3】， 这种情况特殊处理
        x = -1
        y = -1
        for i in range(len(self.nums) - 1):
            if self.nums[i] > self.nums[i + 1]:
                if x == -1:
                    x = self.nums[i]
                    temp = i
                else:
                    y = self.nums[i + 1]
        if y == -1: # 如果
            y = self.nums[temp + 1]
        return x, y

    def find_two_swapped(self):
        n = len(self.nums)
        x = y = -1
        for i in range(n - 1):
            if self.nums[i + 1] < self.nums[i]:
                y = self.nums[i + 1]
                # first swap occurence
                if x == -1:
                    x = self.nums[i]
                # second swap occurence
                else:
                    break
        return x, y

    def recover_tree(self, root, x, y):
        # 用dfs将错误改正，
        if root is None:
            return
        if root.val == x:
            root.val = y
        elif root.val == y: # 这类是elif 不是if
            root.val = x
        else:
            pass
        self.recover_tree(root.left, x, y)
        self.recover_tree(root.right, x, y)



