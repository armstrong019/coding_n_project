Binary tree 如果是inorder traversal 那么得到的会是从小到大的排序。
这个问题我们需要用到一个stack 这个stack，一开始我们将tree的左边节点都放到stack里面 （最后一个点就是tree的最左边的点）。
每次next 时候， pop 出当前的节点， 这个点就是最小的， 然后同时将右边的节点以及以右节点为root的subtree 的左节点都放进stack 里面
这个操作 可以保证我们按照 左-中-右 的顺序来visit tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_to_stack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.push_to_stack(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack:
            return True
        return False

    def push_to_stack(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left
