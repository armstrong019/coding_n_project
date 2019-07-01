import heapq
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        heap = []
        for i in range(len(nums)):
            if len(heap)<n:
                heapq.heappush(heap, nums[i])
            else:
                if nums[i]>heap[0]:
                    heapq.heapreplace(heap, nums[i])
        return heap[0]