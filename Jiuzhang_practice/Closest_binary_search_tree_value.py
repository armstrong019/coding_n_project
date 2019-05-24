"""
Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return None
        ub = root.val  # 初始化lb and ub
        lb = root.val
        while root:
            if root.val < target:
                lb = root.val # 如果当前值比target小， 那么我么找到了一个新的lb
                root = root.right
            elif root.val > target:
                ub = root.val
                root = root.left
            else:
                return root.val
        print(lb, ub)
        if abs(ub - target) <= abs(lb - target):
            return ub
        else:
            return lb


# 这道题有两种解法
# 第一方法： 简单法利用binary tree的特性，如果当前值和target一样那么返回， 如果不一样那么则继续网下搜索：
#          如果当前值比target小，则往右走， 同时在这一点更新了lb（找到了一个新的lb） （注意binary tree搜索的时候lb会一直上升， ub会一直下降）


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code
        lower_node = self.find_lower(root, target)
        upper_node = self.find_upper(root, target)
        print(lower_node.val, upper_node.val)
        if lower_node is None:
            return upper_node.val
        elif upper_node is None:
            return lower_node.val
        else:
            if abs(lower_node.val - target) < abs(upper_node.val - target):
                return lower_node.val
            else:
                return upper_node.val

    def find_lower(self, root, target):
        if root is None:
            return root
        if root.val > target:
            return self.find_lower(root.left, target)
        else:
            lb = self.find_lower(root.right, target)
            if lb:
                return lb
        return root

    def find_upper(self, root, target):
        if root is None:
            return root
        if root.val < target:  #如果当前值小， 往右找，注意这里面有return， return到上一级，
            return self.find_upper(root.right, target)
        else:
            ub = self.find_upper(root.left, target)#如果当前值大， 往左找，如果找到了则返回， 如果没找到， 根据最后一行实际上返回的是当前的root
            if ub:
                return ub
        return root
# 第二种方法是深度优先算法， 用来找upper或者lower bound
# 这种方法比较巧妙不容易写对