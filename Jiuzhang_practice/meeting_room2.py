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

# 这道题目巧妙的运用了heap的结构。heap里面存的是meeting结束的时间
# 我们首先把meeting开始的时间进行sort
# 然后我们定义一个heap 里面存储的是meeting的结束时间。 注意这里面heap【0】永远是最小值
# 如果heap 是空的说明当前没有meeting， 把当前meeting的结束时间加入进去
# heap代表从开始到当前所用过的meeting rooms 的个数。
# 然后扫过这个已经排好序的list，我们首先看一下最早结束的meeting时间，如果当前开始时间 超过最小结束时间， 那么我们replace（pop出最小的结束时间然后换上新的结束时间）
#  如果meeting开始时间比最小的完成时间小， 那么说明我们需要多加一个meeting room
# 最后返回heap的长度，heap的长度代表从开始到当前开过的meeting room的 个数

# 面试写这个方法
# time complexity: Nlog(k):- k is number of maximum meeting room needed
# space complexity: O(k)
import heapq
# Jan/29th
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
                if interval[0] >= heap[0]: # 如果heap非空 并且最早结束的meeting时间晚于开始时间， 则占用这个meeting room
                    heapq.heapreplace(heap, interval[1])
                else: # 如果meeting开始时间比 当前最早的完成时间小， 那么说明我们需要多加一个meeting room
                    heapq.heappush(heap, interval[1])
        return len(heap)


meetings = [[0,30],[5,10],[15,20],[7,11], [15,21],[12,18],[13,19]]
x = Solution1()
res = x.minMeetingRooms(meetings)
print(res)


# 另一种方法：
# 大致相同heap的定义略有不同， 这里面heap代表当前时刻同时进行的meeting room的个数
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
        max_rooms = 0
        for interval in intervals:
            if heap ==[]:
                heapq.heappush(heap, interval[1])
            else:
                while len(heap)>=1 and interval[0] >= heap[0]: # 如果heap非空 并且最早结束的meeting时间晚于开始时间， 则占用这个meeting room， 并且同时将比当前开始时间晚的 那些room都清空
                    heapq.heappop(heap)
                heapq.heappush(heap, interval[1])
            if len(heap)>max_rooms:
                max_rooms = len(heap)
        return max_rooms

# 最直接容易理解的方法。
# time complexity: 2Nlog(2N), 因为要对2N个点 开始，结束 进行排序， 所以是2N
# space complexity： 2N
class Solution1:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        # sort the intervals by start time
        if not intervals:
            return 0
        temp = []
        for i in range(len(intervals)):
            temp.append((intervals[i][0], 1))
            temp.append((intervals[i][1], -1))
        temp.sort(key=lambda x: [x[0], x[1]])
        max_rooms = 0
        cum_sum = 0
        for j in range(len(temp)):
            cum_sum += temp[j][1]
            if max_rooms<cum_sum:
                max_rooms = cum_sum
        return max_rooms



