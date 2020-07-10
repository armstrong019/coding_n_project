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

            dummy.next = ListNode(value) # 这一点需要注意， 具体list node 是怎么create 又是怎么联系起来的
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if residual != 0:  # 如果两个list都走完了， 还需要考虑进位的情况。
            dummy.next = ListNode(residual)
        return head.next

# 这道题主要是考察linked list
