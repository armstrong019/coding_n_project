from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        count = 1
        res = []
        while queue:
            level = []
            while queue:
                node = queue.popleft()
                level.append(node)
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count%2 == 0:
                temp = [x.val for x in level]
                res.append(temp[::-1])
            else:
                res.append([x.val for x in level])
            count +=1
        return res
