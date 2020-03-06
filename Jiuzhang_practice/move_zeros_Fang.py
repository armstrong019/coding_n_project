# beat 100% of the submissions!

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        p0 = 0  # point to 0 elements
        p = 0  # point to nonezero elements
        # make sure p>=p0 all the time
        while p0 <= len(nums) - 1 and p <= len(nums) - 1:
            if nums[p0] == 0 and nums[p] != 0:
                nums[p0], nums[p] = nums[p], nums[p0]
                p0 += 1
                p += 1
            elif nums[p0] != 0:
                p0 += 1
                if p < p0: p = p0 # make sure you move p along with p0
            else:
                p += 1

# to pointer, one search for 0 another search for nonzero,
# the swap these two when applies
# make sure p>= p0 for always

# 下面是一个规范的写法。 之后用这个方法， 一个go through list 一个pindex 用来记录需要该写的位置
# 这个写法不是最intuitive的， 却是最规范的， 最难的就是对于开始为非0情况的理解。
# 如果开始为非0 那么跟自己进行swap 相当于把非0 点跳过
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return []
        pindex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pindex], nums[i] = nums[i], nums[pindex]
                pindex += 1

# 这个解法和上面一样但是好理解
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i <= len(nums) - 1:
            if nums[i] != 0:
                i += 1
            else:
                break
        if i == len(nums): # did not find 0 in list
            return

        start = i
        for j in range(i, len(nums)):
            if nums[j] != 0:
                nums[start], nums[j] = nums[j], nums[start]
                start += 1


