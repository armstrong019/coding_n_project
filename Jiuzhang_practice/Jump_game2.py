class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        p = [0]
        for i in range(len(A) - 1):
            while(i + A[i] >= len(p) and len(p) < len(A)):
                p.append(p[i] + 1)
        print(p)
        return p[-1]