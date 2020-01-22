# 双指针 第一个先走n步 然后同时走 直到不能走， 这里面需要注意的就是有可能会删掉head 必须引入dummy variable

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

