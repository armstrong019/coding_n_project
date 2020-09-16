# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.
# 参见find in mountain array

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        start = 0
        end = len(nums)-1
        while start+1<end:
            # 分四类讨论
            mid = (start+end)//2
            if nums[mid-1]<nums[mid] and nums[mid] >nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid] and nums[mid] <nums[mid+1]:
                start = mid
            elif nums[mid-1]>nums[mid] and nums[mid] >nums[mid+1]:
                end = mid
            else:  #往哪边走都可以。
                end = mid
        # 涵盖了只有两个点的情况
        if nums[start] < nums[end]:
            return end
        else:
            return start

# binary search, the comparison is made between mid and mid+1

    def binary_search(self, start, end, nums):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:
                end = mid
            elif nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                start = mid
            else:
                ind = self.binary_search(start, mid, L)
                ind2 = self.binary_search(mid, end, L)
                if ind == -1 and ind2 == -1:
                    return -1
                else:
                    return max(ind, ind2)
        return -1

# # revisted May 29th.
# 这个版本是更加general 的版本， 没有用到题目里的隐含条件， 而是assume起点和终点都能是peak
# 这样的话 要分四种情况： nums[mid -1]， nums[mid] ，nums[mid + 1] 上升关系， 下降关系， 中间高（找到结果） 两边高： 左右都要找（但是根据题目定义其实找一边就可以）。
class Solution0:
    def findPeakElement(self, nums: List[int]) -> int:
        ind = self.binary_search(0, len(nums) - 1, nums)
        if ind != -1:
            return ind
        else:  # check for two end pts
            if len(nums) == 1:
                return 0
            if nums[1] < nums[0]:
                return 0
            if nums[-2] < nums[-1]:
                return len(nums) - 1
        return ind

    def binary_search(self, start, end, nums):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:
                end = mid
            elif nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                start = mid
            else: #中间底 两边都要找。
                ind = self.binary_search(start, mid, nums)
                ind2 = self.binary_search(mid, end, nums)
                if ind == -1 and ind2 == -1:
                    return -1
                else:
                    return max(ind, ind2)
        return -1


x= Solution0()
nums = [1,2,1,2,1]
x.findPeakElement(nums)

# 这个是九章的写法， 我个人不是很喜欢， 过于简单 不便于记忆
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start,end=0,len(A)-1
        while start+1<end:
            mid=(start+end)//2
            if A[mid]<A[mid+1]: #因为这里的termination condition是start+1<end，所以mid+1一定存在
                start=mid
            else:
                end=mid
        if A[start]>A[end]:
            return start
        else:
            return end
