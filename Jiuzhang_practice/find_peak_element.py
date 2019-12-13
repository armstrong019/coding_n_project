# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

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

# binary search, the comparison is made between mid and mid+1
