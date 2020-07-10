
# 没有什么corner case 直接写就好了
# similar： Find Peak Element

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= A[mid + 1]:
                start = mid
            else:
                end = mid
        return end
