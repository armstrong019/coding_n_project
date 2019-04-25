import collections


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self._is_symmetric(root.left, root.right)

    def _is_symmetric(self, l, r):
        if not l and not r:
            return True
        if l and not r:
            return False
        if r and not l:
            return False
        if l.val != r.val:
            return False
        return self._is_symmetric(l.right, r.left) and \
               self._is_symmetric(l.left, r.right)

#这道题比较容易的是拆分成左右两个nodes a和b symmetric的定义是如果a.right = b.left 并且a.left=b.right 那么a，b 两个点就满足条件
#用深搜