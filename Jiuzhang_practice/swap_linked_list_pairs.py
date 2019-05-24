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