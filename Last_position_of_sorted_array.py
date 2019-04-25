class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):
        # write your code here
        if nums == []:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if target == nums[end]:
            return end
        elif target == nums[start]:
            return start
        else:
            return -1


# binary search:
# 几个要点： 第一 终止条件：start+1《end
# 第二：如果是last position 那么将 nums【mid】和target比较的时候等号要注意
# 第三： 最后在判断的时候先判断end的情况
# 第三： 最后在判断的时候先判断end的情况