import collections
import heapq


class Solution:
    def topKFrequent(self, nums,k):
        count = collections.Counter(nums)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True) # 记住这个写法
        res = []
        for i in range(k):
            res.append(sorted_count[i][0])
        return res

# 这道题就是用heap 或者hashtable比较合适
