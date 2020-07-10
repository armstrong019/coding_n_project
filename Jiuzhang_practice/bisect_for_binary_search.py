# interview question from apple

from random import uniform
import numpy as np
from bisect import bisect

# bisect 总结：找到 index where target>=nums[index-1] and target<nums[index]

def binary_search(nums, target):
    # same as bisect
    start = 0
    end = len(nums ) -1
    while start + 1 <end:
        mid = (start +end )//2
        if nums[mid ]>=target:
            end = mid
        else:
            start = mid
    # print(nums[start],nums[end],target)
    if nums[start ]<=target and nums[end]>=target:
        return end
    if target <nums[start]:
        return 0


def sample_index(L):
    freqs = [0 for _ in range(len(L))]
    intervals = np.cumsum(L)
    for i in range(10000):
        rnd = uniform(0, 1)
        index = binary_search(intervals ,rnd)  # index = bisect(intervals ,rnd)
        freqs[index]+=1
    print(freqs)



L =  [0.1, 0.2, 0.7]
sample_index(L)
