class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        low = sys.maxsize
        total = 0
        for i in range(len(prices)):
            if low>prices[i]:
                low = prices[i]
            if prices[i]-low>total:
                total = prices[i]-low
        return total
