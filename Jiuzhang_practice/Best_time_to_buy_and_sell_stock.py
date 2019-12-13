# 如果是单减的， 那么返回0

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        maxP = 0 # 记录global的最大差距
        low = sys.maxsize # 记录当前新低
        for p in prices:
            if p < low:
                low = p
                diff = 0 # 一旦出现当前新低， 当前的diff就被reset成0
            else:
                diff = p-low
            if diff > maxP:
                maxP = diff
        return maxP

price =  [7,1,5,3,6,4]
x =  Solution()
print(x.maxProfit(price))
