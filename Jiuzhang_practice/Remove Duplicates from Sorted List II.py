# 这道题目用两个指针就可以了，一个指向previous 一个指向current 同时考虑current。next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        current = head
        while current and current.next:# 注意termination condition，current 和current。next 在当前必须不能为None
            if current.val == current.next.val:
                while current and current.next and current.val == current.next.val: # 嵌套while loop 是为了简化code
                    current = current.next
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return dummy.next

