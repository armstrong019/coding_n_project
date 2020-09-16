# Given an array of integers with possible duplicates,
# randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.

# 这道题有两种解法， 第一种是直接法， 创建一个dictionary， key 是num value是他对应的indexes
# 然后随机挑一个
from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i in range(len(nums)):
            self.dic[nums[i]].append(i)

    def pick(self, target: int) -> int:
        indexes = self.dic[target]
        ind = random.randint(0, len(indexes) - 1)
        return indexes[ind]

# 第二种方法是reservior sampling
# 这种方法适用于很长list的情况。这样我们不需要extra space 去store hashtable
# reservior sampling 的基本思路：
   # 第一次出现target 选取当前index的几率是1
   # 第二次出现target 选取当前index的几率是1/2
   # 第三次出现target 选取当前index的几率是1/3
# 证明 第一个index 被保留的几率是： 1*1/2*2/3 = 1/3
#      第二个index 被保留的几率是： 1/2*2/3 = 1/3
#      第三个index 被保留的几率是： 1/3

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) == 0:
                    res = i
                count += 1
        return res
