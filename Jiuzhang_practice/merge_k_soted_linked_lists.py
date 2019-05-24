"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        heap = []
        count = 0 # 这里面加count 是为了 break tie
        for list in lists:
            if list: # list 存在的时候才加
                heapq.heappush(heap, (list.val, count, list))
                count += 1

        dummy = ListNode(-1)
        temp = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            if node.next: # next 存在的时候才加
                heapq.heappush(heap, (node.next.val, count, node.next))
            temp.next = node
            temp = temp.next
            count += 1
        return dummy.next



        # use heap. in the beginning add all heads of the lists to the heap.
# then when heap is not empty, pop from the heap (first pop out the smallest value) (note here we can add more than 1 dimension (node.val, node)to the heap)
# after pop, add the next node in to the heap