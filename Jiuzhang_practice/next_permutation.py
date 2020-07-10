class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        pivot = None
        for i in range(len(nums)-1, 0, -1): # 从右往左找到第一个下降的点的位置， 叫做pivot
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        if pivot is None: # 如果没找到， 说明是5，4，3，2，1 的case， 反转整个list, 注意这里面不可以使用 if pivot， 如果pivot=0 也会返回False
            nums.reverse()  # inplace 反转一个list
        else:
            for j in range(len(nums)-1, 0, -1): # 如果找到，
                if nums[j]>nums[pivot]:
                    nums[pivot],nums[j] = nums[j],nums[pivot] #那么再次从右往左找，找到第一个比pivot大的值
                    nums[pivot+1:] = nums[pivot+1:][::-1] # 之后将pivot+1之后的位置 反转， 由于不是反转整个list， nums 的address不变。
                    break


这道题纯粹考察总结
1　　2　　7　　4　　3　　1

1　（2）　7　　4　（3）　1

1　　3　（7　　4　　2　　1） # 反转这一部分

1　　3　　1　　2　　4　　7

