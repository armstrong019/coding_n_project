# binary search

class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        start,end=1,n
        while start+1<end:
            mid=(start+end)//2
            if not SVNRepo.isBadVersion(mid):
                start=mid
            else:
                end=mid
        if SVNRepo.isBadVersion(start):
            return start
        else:
            return end


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        if isBadVersion(end):
            return end
        return -1
