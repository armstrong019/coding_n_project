'''
The problem solution is very simple - one could always insert new node as a child of the leaf. To define which leaf to use, one could follow the standard BST logic :

If val > node.val - go to insert into the right subtree.

If val < node.val - go to insert into the left subtree.
'''
# 第一种写法比较好看 第二种写法比较直接
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        ref = root
        while root is not None:
            if val>root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return ref
                root = root.right
            if val<root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return ref
                root = root.left

        return ref

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        ref = root
        while root is not None:
            if val>root.val and root.right is None:
                root.right = TreeNode(val)
                break
            elif val>root.val and root.right is not None:
                root = root.right
            elif val<root.val and root.left is None:
                root.left = TreeNode(val)
                break
            else:
                root = root.left
        return ref
