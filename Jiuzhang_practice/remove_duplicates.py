# O(n) time, O(n) space
class Solution:
    # result point to duplicate number, result does not change when duplicate appears, when
    # a new number is found, then nums[result] = new number
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1

        return result