# Cut, reverse and connect. Straightforward solution
# 找到开始， 开始之前，和结束的位置

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if m == n:
            return head
        dummy = ListNode(-1, next=head)
        temp = dummy
        # find the node before start
        for i in range(m - 1):
            temp = temp.next
        start_prev = temp # 开始之前的位置
        start = temp.next # 开始的位置

        # now start to reverse
        prev = start # 2 pointer 的方法
        cur = prev.next
        steps = n - m # 走的步数
        while steps > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            steps -= 1

        start_prev.next = prev # 将开始之前和结尾连起来
        start.next = cur # 将反转的之后的末端和结束点下一个点连起来。
        return dummy.next
