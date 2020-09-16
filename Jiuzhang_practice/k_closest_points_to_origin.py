# 这道题目和那个kth largest element 类似，都是用heap
# 这道题本应该是maxheap： 因为每次我们要get rid off 那个heap里面的最大值
# 但是python 没有， 所以只好将distance弄成负的， 然后做成maxheap

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            if len(q) < K:
                heapq.heappush(q, (-dist, [x, y]))
            else:
                val, point = q[0]
                if dist < -val: # 这个符号不要写反了
                    heapq.heapreplace(q, (-dist, [x, y]))
        res = []
        while q:
            _, point = heapq.heappop(q)
            res.append(point)
        return res

