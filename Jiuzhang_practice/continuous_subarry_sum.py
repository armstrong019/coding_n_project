
# 很麻烦的一道题 主要是k=0 的情况很麻烦,不推荐这道题， 考试照着超吧
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if k != 0:
                res = cum_sum % k
            else:
                res = cum_sum
            if res in dic:
                if i - dic[res] >= 2:
                    return True
                else:
                    pass # 注意这个情况我们不对dictionary 进行更新
            else:
                dic[res] = i
        return False


