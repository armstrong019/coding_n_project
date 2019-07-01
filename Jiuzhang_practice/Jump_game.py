class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        dp = [0 for i in range(len(A))]
        dp[0] = 1
        for i in range(len(A)):
            if dp[i] == 1 and A[i]!=0:
                dp[i+1:i+A[i]+1] = [1 for _ in range(A[i])]
            if dp[-1] == 1:
                return True
        return False