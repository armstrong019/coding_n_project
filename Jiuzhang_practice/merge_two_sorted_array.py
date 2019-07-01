class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        p1 = 0
        p2 = 0
        res = []
        while p1 <= len(A) - 1 and p2 <= len(B) - 1:
            if A[p1] <= B[p2]:
                res.append(A[p1])
                p1 += 1
            else:
                res.append(B[p2])
                p2 += 1
        if p1 <= len(A) - 1:
            res = res + A[p1:]
        if p2 <= len(B) - 1:
            res = res + B[p2:]

        return res