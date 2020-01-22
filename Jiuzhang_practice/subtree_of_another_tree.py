class Solution:
    def isSubtree(self, s, t):
        if s is None and t is None:
            return True
        if s is None and t is not None:
            return False
        is_same = self.is_same_tree(s,t)
        if is_same:
            return True
        else:
            is_sub_left = self.isSubtree(s.left, t)
            is_sub_right = self.isSubtree(s.right, t)
            return is_sub_left or is_sub_right

    def is_same_tree(self, root,t):
        if root is None and t is None:
            return True
        elif root is None and t is not None:
            return False
        elif root is not None and t is None:
            return False
        else:
            if root.val != t.val:
                return False
            else:
                is_left_same = self.is_same_tree(root.left, t.left)
                is_right_same = self.is_same_tree(root.right, t.right)
                return is_left_same and is_right_same

# 这道题借鉴了is_same_tree 的想法。 沿用dfs


# 第二次写， 个人感觉这种写法可读性更好
class Solution:
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s:
            return False
        if s.val == t.val:
            is_same = self.is_same_tree(s,t) # 找到一个点， 值相合，此时进行判断
            if is_same:
                return True
        is_left = self.isSubtree(s.left,t)
        is_right = self.isSubtree(s.right, t)
        return is_left or is_right

    def is_same_tree(self, root, t):
        if root is None and t is None:
            return True
        elif root is None and t is not None:
            return False
        elif root is not None and t is None:
            return False
        else:
            if root.val != t.val:
                return False
            else:
                is_left_same = self.is_same_tree(root.left, t.left)
                is_right_same = self.is_same_tree(root.right, t.right)
                return is_left_same and is_right_same







