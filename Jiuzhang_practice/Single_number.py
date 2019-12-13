class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i, val in enumerate(nums):
            if val in dic:
                del dic[val]
            else:
                dic[val] = True

        for key in dic.keys():
            return key
# 简单 用hash map 就行
