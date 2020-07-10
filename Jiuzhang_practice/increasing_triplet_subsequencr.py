class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = sys.maxsize
        min2 = sys.maxsize
        for i in range(len(nums)):
            if nums[i]<=min1: #等于号不能丢
                min1 = nums[i]
            else:
                if nums[i] <= min2:
                    min2 = nums[i]
                else:
                    print(i)
                    return True
        return False

# 这道题就是把逻辑想清楚就好了
# min1 min2分别代表第一小第二小的数字，
# 从前往后缕，如果遇到比第一小的数字， 更新第一小，如果遇到在第一小 和第二小之间的数字， 更新第二小，
# 如果遇到比第二小大的数字， 则已经找到了。
