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

# mock 的时候又写了一遍， 开始没有想到dummy的情况, [1,2] 1 case没过.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next and n == 1:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        p0 = dummy
        p1 = dummy

        while n != 0:
            p1 = p1.next
            n -= 1
        while p1.next:
            p0 = p0.next
            p1 = p1.next

        p0.next = p0.next.next
        return dummy.next
