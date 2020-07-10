# 中位数 如果是偶数个是两个中间数的平均， 如果是奇数个，是中间数。
# 这道题目的基本思想是将已经见到过的数字拆成两半， 值小的一半和大的一半，
# 值小的一半用maxheap 保存， 这样方便得到最大值
# 值大的一半用minheap 保存， 这样方便得到最小值
# maxheap minheap 的 大小相等要不然就是差1
# 如果maxheap 大， 那么中位数就是其最大值， 否则是maxheap 的最大值和minheap的最小值的平均值

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        if len(self.h1) == len(self.h2):
            if self.h1 == [] or num < self.h2[0]:
                heapq.heappush(self.h1, -num)
            else:
                heapq.heappush(self.h1, -heapq.heappop(self.h2))
                heapq.heappush(self.h2, num)

        elif len(self.h1) > len(self.h2):
            if num >= -self.h1[0]:
                heapq.heappush(self.h2, num)
            else:
                heapq.heappush(self.h2, -heapq.heappop(self.h1))
                heapq.heappush(self.h1, -num)
        else:
            print('error!')

    def findMedian(self) -> float:
        if len(self.h1) == len(self.h2):
            return float(-self.h1[0] + self.h2[0]) / 2
        else:
            return float(-self.h1[0])


