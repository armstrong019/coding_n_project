class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = head
        current = head.next
        while current: # 注意termination condition，current 在当前必须不能为None
            if prev.val == current.val:
                prev.next = current.next
                current = current.next
            else:
                prev = prev.next
                current = current.next
        return head
