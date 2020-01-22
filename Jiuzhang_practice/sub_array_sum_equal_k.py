# 第一种方法超时了
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = []
        cum_sum.append(nums[0])
        for i in range(1, len(nums)):
            cum_sum.append(cum_sum[-1]+nums[i])
        count = 0
        for i in range(len(nums)):
            for j in range(i):
                if cum_sum[i]-cum_sum[j]==k:
                    count+=1
            if cum_sum[i] == k:
                count+=1
        return count

# 这种方法借用了hastable，
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = []
        cum_sum.append(nums[0])
        for i in range(1, len(nums)):
            cum_sum.append(cum_sum[-1]+nums[i])
        count = 0
        dic = {} # 记录值： 其出现的次数
        for i in range(len(nums)):
            val = cum_sum[i]
            if val == k: # 如果本身就是k 那么+1
                count+=1
            if val-k in dic:
                count+= dic[val-k]
            if val in dic:
                dic[val]+=1
            else:
                dic[val]=1
        return count

