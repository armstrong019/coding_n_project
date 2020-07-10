# 这道题目的解题关键就是要画图 见下
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# two pointer, one move every step one move two steps each time.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next is None:
            return slow
        else:
            return slow.next

# revisited Jun 24th
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ps = head
        pf = head
        while pf.next and pf.next.next:
            ps = ps.next
            pf = pf.next.next

        if pf.next is None:
            return ps
        else:
            return ps.next

#          1-2-3-4-5-None
#            s f
#              s   f

#          1-2-3-4-5-6-None
#            s f
#              s   f
#                s     f

#          1-2-None
#            s f

#          1-2-3-None
#            s f
