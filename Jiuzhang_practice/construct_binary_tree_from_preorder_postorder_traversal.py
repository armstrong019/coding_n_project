class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None
        else:
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root
            else:
                index = pre.index(post[-2])
                root.left = self.constructFromPrePost(pre[1:index], post[:index - 1])
                root.right = self.constructFromPrePost(pre[index:], post[-1 - (len(pre) - index):-1])
                return root


#这道题用bfs
        # preorder： root， left sub， right sub
        # inorder： left sub， root， right sub
        # postorder： left sub， right sub， root
# inorder 把tree分成左右两部分， 左边是left sub inorder tree， 右边是right sub inoder tree
