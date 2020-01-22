# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        ps = head
        pf = head

        while pf.next and pf.next.next:  # 最后termination一定是看快指针， 而且必须先看pf.next 是否存在
            pf = pf.next.next
            ps = ps.next
            if pf == ps:
                return True
        return False
