# 双指针 第一个先走n步 然后同时走 直到走在前面的指针指向最后一个element， 这里面需要注意的就是有可能会删掉head 必须引入dummy variable

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        steps = 0
        dummy = ListNode(-1)
        dummy.next = head
        ps = dummy
        pf = dummy
        while pf.next:
            if steps < n:
                pf = pf.next
                steps += 1
            else:
                pf = pf.next
                ps = ps.next
        ps.next = ps.next.next
        return dummy.next

# 自己写的方法， 面试写这个， 不需要dummy
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pf, ps = head, head
        for i in range(n):
            pf = pf.next

        if pf is None:
            return head.next

        while pf.next is not None:
            ps = ps.next
            pf = pf.next

        ps.next = ps.next.next

        return head
