class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        return max(nums[start], nums[end])

# 找最大值， 二分法， 每次比较mid 和 mid+1， 注意以为状态是start+1《end， 所以mid+1 一定存在
# 最后比较start end的值谁大