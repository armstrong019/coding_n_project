"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if not head:
            return head
        ps = head
        pf = head
        while pf.next and pf.next.next:
            pf = pf.next.next
            ps = ps.next
        return ps

# two pointer, one move every step one move two steps each time. 