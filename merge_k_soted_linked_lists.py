import heapq

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        heap = []
        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, node))

        dummy = ListNode(0)
        head = dummy
        while len(heap) != 0:
            val, node = heapq.heappop(heap)
            dummy.next = node
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, node.next))
            dummy = dummy.next

        return head.next


# use heap. in the begining add all heads of the lists to the heap.
# then when heap is not empty, pop from the heap (first pop out the smallest value) (note here we can add more than 1 dimension (node.val, node)to the heap)
# after pop, add the next node in to the heap