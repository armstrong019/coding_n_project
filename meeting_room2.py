"""
919. Meeting Rooms II
中文English
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation:
Only need one meeting room

"""


import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        # sort the intervals by start time
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            if heap and interval.start >= heap[0]:
                heapq.heapreplace(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)

        return len(heap)

# 这道题目巧妙的运用了heap的结构。heap里面存的是meeting结束的时间
# 我们首先把meeting开始的时间进行sort
# 然后我们定义一个heap 里面存储的是meeting的结束时间。 注意这里面heap【0】永远是最小值
# 然后扫过这个已经排好序的list，我们首先看一下最早结束的meeting时间，如果当前开始时间 超过最小结束时间， 那么我们replace（pop出最小的结束时间然后换上新的结束时间）
#  如果meeting开始时间比最小的完成时间小， 那么说明我们需要多加一个meeting room
# 最后返回heap的长度


class Solution1:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        # sort the intervals by start time
        intervals.sort(key=lambda x: x[0])
        heap = []
        for interval in intervals:
            if heap ==[]:
                heapq.heappush(heap, interval[1])
            else:
                if interval[0] >= heap[0]:
                    heapq.heapreplace(heap, interval[1])
                else:
                    heapq.heappush(heap, interval[1])
            print(heap)
        return len(heap)


meetings = [[0,30],[5,10],[15,20],[7,11], [15,21],[12,18],[13,19]]
x = Solution1()
res = x.minMeetingRooms(meetings)
print(res)