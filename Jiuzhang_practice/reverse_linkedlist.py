# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list_pointer = None
        while head:
            current = head
            # current hold the head address reference
            head = head.next
            # head to move to next node
            current.next = new_list_pointer
            # to assign current.next to new_list_pointer
            # the initial new_list_pointer is None, means it is the end of list
            # new_list_pointer initially points to the later node and it goes from back to front
            new_list_pointer = current
            # assign current to new_list_pointer after the procedure is done
        return new_list_pointer

#current: 用于存当前的点。
# head：用于指向下一个点
# new_list_pointer：用来记录前一个点
# 具体操作如下： 首先将当前点记录下来， 然后将head挪到下一个点， 第三步让当前点的下一个点变成前一个点， 最后将new_list_pointer指向当前点。
# 注意操作的顺序，否则容易出错

#自己写的版本， 具体的思路是把 current 这个指针指向prev， 因为需要向下进行搜索， 我们需要暂时保存nxt （current。nxt已经被改写）
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        prev = None
        cur = head
        while cur:
            nxt = cur.next # 暂时的保存这个node 因为cur.next 会被改写
            cur.next = prev
            prev = cur
            cur = nxt
        return prev # 注意最后返回的是prev

# 自己写的另一个版本
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        current = head
        prev = None
        nxt = head.next
        while True:
            current.next = prev
            prev = current
            current = nxt
            if nxt is not None:
                nxt = nxt.next
            else:
                break
        return prev
