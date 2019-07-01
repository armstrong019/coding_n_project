class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if A == []:
            return [-1, -1]
        start, end = 0, len(A) - 1
        first, last = start, end
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        print(start, end)
        if A[start] == target:
            first = start
        elif A[end] == target:
            first = end

        else:
            return [-1, -1]

        print(first)

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            last = end
        elif A[start] == target:
            last = start
        else:
            return [-1, -1]

        return [first, last]