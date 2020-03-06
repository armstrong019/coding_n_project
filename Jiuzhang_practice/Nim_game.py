class Solution:
    def canWinNim(self, n: int) -> bool:
        if n==0:
            return False
        if n<=3:
            return True
        res = n%4
        if res==0:
            return False
        else:
            return True
