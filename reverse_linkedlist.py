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