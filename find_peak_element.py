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
            if A[mid]<A[mid+1]:
                start=mid
            else:
                end=mid
        if A[start]>A[end]:
            return start
        else:
            return end

# binary search, the comparison is made between mid and mid+1