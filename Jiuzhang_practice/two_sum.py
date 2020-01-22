class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i, a in enumerate(numbers):
            for j,b in enumerate(numbers[i+1:]):
                print(i,j,a,b)
                if a+b == target:
                    return [i,j+i+1]

    def twoSum(self, numbers, target):
        # write your code here
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i,j]

# these two answers are the same
#这题要点主要是返回的是位置， 不能使用sort+two pointers 这样位置会打乱

# third solution, use hashtable, very straightforward
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(nums):
            look = target - val
            if look in dic:
                return [dic[look], i]
            else:
                dic[val] = i


