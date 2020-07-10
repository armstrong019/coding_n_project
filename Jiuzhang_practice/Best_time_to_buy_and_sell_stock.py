# 当前值 - 之前出现的最小值 = 当前如果卖的profit

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

# revisited May 8th
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_value = prices[0] # 第0个时间点不买也不卖， profit = 0， min_value 就是第一个值
        for i in range(1, len(prices)): #
            min_value = min(prices[i], min_value) # 当一个新的价格出现时，更新最小值
            max_profit = max(max_profit, prices[i]- min_value) # 如果现在卖出去的收益是prices[i]- min_value
        return max_profit
