class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    # Time: O(k + h)
    def kthSmallest(self, root, k):
        # write your code here
        self.k = k
        self.result = None
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.result = root.val
        if self.k > 0:
            self.helper(root.right)

# go all the way down on the left side until hit the end of tree.
# 然后开始回溯。回溯的时候k-=1， 如果k还不等于0 那么向右边搜索， 一到右边以后就立马向左分支走到底 之后k-=1， 重复以上操作