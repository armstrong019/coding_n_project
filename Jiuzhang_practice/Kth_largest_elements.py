# 两种写法， 差不多 第一种更优
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


import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

