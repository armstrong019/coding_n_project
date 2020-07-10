# 这道题主要就是把方法想清楚
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dic = {}
        for val in nums:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] += 1

        max_len = 0
        for key in dic.keys():
            if key + 1 in dic:
                current_length = dic[key] + dic[key + 1]
                max_len = max(max_len, current_length)
        return max_len
