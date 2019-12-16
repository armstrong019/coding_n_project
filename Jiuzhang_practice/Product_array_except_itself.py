# 这道题主要就是考察观察力。
# List1记录从左边来的阶乘（不包括当前值）， List2 记录从右边来的阶乘（不包括当前值）， 两个的乘积即为结果。
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        List1 = [1]
        for i in range(1, len(nums)):
            List1.append(nums[i - 1] * List1[-1])
        List2 = [1]
        for j in range(len(nums) - 1, 0, -1):
            List2.insert(0, nums[j] * List2[0])
        return [List1[i] * List2[i] for i in range(len(nums))]

