# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        dummy = head
        residual = 0
        while l1 or l2:
            v = 0
            if l1:
                v = l1.val
            if l2:
                v += l2.val
            v += residual
            value = v % 10
            residual = v // 10

            dummy.next = ListNode(value)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if residual != 0:
            dummy.next = ListNode(residual)
        return head.next

# 这道题主要是考察linked list
