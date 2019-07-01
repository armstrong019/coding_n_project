class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if A ==[]:
            return -1
        start = 0
        end = len(A)-1
        while start+1<end:
            mid = (start+end)//2
            if A[mid]<=target:
                start = mid
            else:
                end = mid
        left = start
        right = end
        n = len(A)-1
        res = []
        while len(res)<k:
            if left>=0 and right<=n:
                if abs(A[left]-target)<=abs(A[right]-target):
                    res.append(A[left])
                    left -= 1
                else:
                    res.append(A[right])
                    right += 1
            elif left>=0:
                res.append(A[left])
                left -= 1
            elif right<=n:
                res.append(A[right])
                right += 1
            else:
                print('wrong')
        return res

# find k closest elements: binary search, find nearest value
# then compare the absolute difference between left and right
# iteratively add to the result, until the result has k elements


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if k == 0:
            return []
        start = 0
        end = len(A)-1
        while start+1<end:
            mid = (start+end)//2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        # verify the values
        result = []
        while start>=0 and end<=len(A)-1:
            if abs(A[start]-target)<=abs(A[end]-target):
                result.append(A[start])
                start-=1
            else:
                result.append(A[end])
                end += 1
            if len(result)==k:
                return result
        while start>0:
            result.append(A[start])
            start -= 1
            if len(result)==k:
                return result
        while end<=len(A)-1:
            result.append(A[end])
            end += 1
            if len(result)==k:
                return result

# 第二种写法， 这两种写法是一致的。这种写法也比较直接