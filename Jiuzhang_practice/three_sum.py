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
            if numbers[i] == numbers[i-1]:
                continue
            target=-numbers[i]
            left,right=i+1,len(numbers)-1
            while left < right:
                if numbers[left]+numbers[right]==target:
                    res.append([numbers[i],numbers[left],numbers[right]])
                    left+=1
                    right-=1
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
