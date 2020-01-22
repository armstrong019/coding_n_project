# 自己写的版本 类似于3sum。

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        min_diff = sys.maxsize
        result = 0
        for i in range(len(nums)-1):
            fix_n = nums[i]
            diff = target-fix_n
            ps = i+1
            pt = len(nums)-1
            while ps < pt:
                val = nums[ps]+nums[pt]
                if abs(diff-val)<min_diff: # update 结果 注意这里面每一次都要update一下
                    min_diff = abs(diff-val)
                    result = fix_n+val
                if fix_n+val < target: #
                    ps+=1
                elif fix_n+val >target:
                    pt-=1
                else:
                    return target
        return result
