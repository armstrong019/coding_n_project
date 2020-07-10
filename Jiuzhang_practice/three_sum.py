# 难写 面试的时候写最后一种
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        res = []
        for i in range(len(numbers)-2):
            if numbers[i] > 0:
                break
            # 在这一步也需要去重， 如果这个书依据
            if numbers[i] == numbers[i-1]:
                continue
            target=-numbers[i]
            left,right=i+1,len(numbers)-1
            while left < right:
                if numbers[left]+numbers[right]==target:
                    res.append([numbers[i],numbers[left],numbers[right]])
                    left+=1
                    right-=1
                    #注意这个去重 是当找到一个答案以后。 去掉和当前答案一样的所有答案
                    while left<right and numbers[left]==numbers[left-1]:
                        left+=1
                    while left<right and numbers[right]==numbers[right+1]:
                        right-=1
                elif numbers[left]+numbers[right]<target:
                    left+=1
                else:
                    right-=1
        return res

# 从左往右扫， 每次固定一个值，然后用two pointers，从左右夹击
# 核心在于如何去重。去重包括两种， 第一种是每次固定的值可能有重复，第二种是two pointer指向的值可能有重复


numbers = [-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5]
x= Solution()
x.threeSum(numbers)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for k in range(len(nums)-2):
            if nums[k]>0:
                continue
            if k != 0 and nums[k] == nums[k-1]:
                continue
            fix = -nums[k]
            ps = k+1
            pe = len(nums)-1
            while ps<pe:
                while ps<pe and ps != k+1 and nums[ps] == nums[ps-1]: # 先去重的方法 不是很建议
                    ps+=1
                if ps<pe:
                    if nums[ps]+nums[pe] == fix:
                        result.append([-fix, nums[ps], nums[pe]])
                        ps+=1
                        pe-=1
                    elif nums[ps]+nums[pe]<fix:
                        ps+=1
                    else:
                        pe-=1
        return result

# Jun28 又写了一遍 感觉去重还是有些困难。尤其是二分搜索去重
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) <= 2:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                fix = -nums[i]
                ps = i + 1
                pe = len(nums) - 1
                self.find_solutions(ps, pe, nums, fix, res)
        return res

    def find_solutions(self, ps, pe, nums, fix, res):
        # 用一个while循环，从外向内找解， 分三种类型讨论，相等，大于，小于。
        while ps < pe:
            if nums[ps] + nums[pe] == fix: # 已经加入一个结果了， 然后把和他相同的结果都去掉 【-1，0，0，0，1，1，1】可以考虑这个例子， -1 是fix 的值
                res.append([-fix, nums[ps], nums[pe]])
                ps += 1
                pe -= 1
                while ps < pe and nums[ps] == nums[ps - 1]: # 找到一个结果之后去重 这样写比较稳妥，而且去重只需要做一边就好了
                    ps += 1
            elif nums[ps] + nums[pe] < fix:
                ps += 1
            else:
                pe -= 1
