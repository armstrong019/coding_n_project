# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(-1)
        dummy = head
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2

        # while l1:
        #     dummy.next = l1
        #     l1 = l1.next
        #     dummy = dummy.next
        # while l2:
        #     dummy.next = l2
        #     l2 = l2.next
        #     dummy = dummy.next

        return head.next




