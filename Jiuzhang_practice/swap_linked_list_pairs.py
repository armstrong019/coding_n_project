#https://www.cnblogs.com/yrbbest/p/4434861.html

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pre->a->b->b.next (orginal)
        # pre->b->a->a.next (new order)

        Dummy = pre = ListNode(0)
        Dummy.next = head
        pre.next = head
        # print(Dummy.next, pre.next, pre.next.next)
        # while pre.next and pre.next.next:

        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            tmp1 = b.next
            tmp2 = a.next
            tmp3 = pre.next

            pre.next = tmp2
            a.next = tmp1
            b.next = tmp3

            pre = pre.next.next
            # print(Dummy.next, pre.next)
        return Dummy.next

# use tempary variable to store the address of each node

# 第二遍写还是不太会
#https://medium.com/@jimdaosui/swap-nodes-in-pairs-67b311fd02f7
# recursion 相对容易一点
# 和dfs 类似吧， 走到最后一步然后从尾巴到头把list重建起来
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        post = self.swapPairs(head.next.next)
        cur = head.next
        cur.next = head
        head.next = post
        return cur
