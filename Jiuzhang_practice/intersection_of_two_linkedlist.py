# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = {}
        i = 0
        while headA:
            dic[headA] = i
            headA = headA.next
            i += 1

        while headB:
            if headB in dic:
                return headB
            headB = headB.next

        return None

#用hashtable 来解决， 为什么用hastable 而不用list 以为list的搜索时间是O（n）， 而hashtable是O（1）
