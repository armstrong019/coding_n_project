# 这道题和graph clone 有点相似。
# 比较tricky 的点是 node。next 和node。random 都是指向另一个node
# 我们首先建立一个从旧点到新点的mapping （hashtable）， 然后我们再将link之间的关系建立起来

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # copy nodes, store the old-new mapping:
        dic = {}
        temp = head
        while temp is not None:
            val = temp.val
            new_node = Node(val, next=None, random=None)
            dic[temp] = new_node
            temp = temp.next

        # then reconstruct the linkedlist
        temp2 = head
        while temp2:
            # 有的node node.next 不指向null， 但是node。random 指向null 反之亦然
            if temp2.next is not None:
                dic[temp2].next = dic[temp2.next]
            if temp2.random is not None:
                dic[temp2].random = dic[temp2.random]
            temp2 = temp2.next

        return dic[head]
