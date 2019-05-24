import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        heapq.heapify(nums)
        res = heapq.nlargest(k,nums)
        return res

# 用heapq， 或者sorting method