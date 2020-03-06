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
                while ps<pe and ps != k+1 and nums[ps] == nums[ps-1]:
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
