class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        if A == []:
            return -1
        min_ind = self.find_minimum_index(A)
        ind = self.binary_search(A, target, min_ind)
        return ind

    def find_minimum_index(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]:
                start = mid
            else:
                end = mid
        if A[start] <= A[end]:
            return start
        else:
            return end

    def binary_search(self, A, target, min_ind):
        if A[min_ind] <= target <= A[-1]:
            start = min_ind
            end = len(A) - 1
        else:
            start = 0
            end = min_ind - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if target == A[start]:
            return start
        if target == A[end]:
            return end
        return -1


# two steps: first find out the minimum index of the array
#            then identify which segment the target value fall into