# 这道题目和那个kth largest element 类似，都是用heap
# 这道题本应该是maxheap： 因为每次我们要get rid off 那个heap里面的最大值
# 但是python 没有， 所以只好将distance弄成负的， 然后做成maxheap

import numpy as np
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def euclidean_dist(point):
            x = point[0]
            y = point[1]
            return np.sqrt(x**2+y**2)
        distances = [-euclidean_dist(point) for point in points]
        heap = []
        for i in range(len(points)):
            if len(heap) < K:
                heapq.heappush(heap, (distances[i], points[i][0], points[i][1]))
            else:
                if distances[i] > heap[0][0]: # 这个符号不要写反了
                    heapq.heapreplace(heap, (distances[i], points[i][0], points[i][1]))
        res = []
        while heap:
            _,x,y = heapq.heappop(heap)
            res.append([x,y])
        return res




