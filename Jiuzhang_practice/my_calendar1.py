# 建立两个sorted list 分别记录开始和结束的时间
# 用start times 记录开始的时间（sorted）， 将新的start时间在里面进行2分搜索
# 分三类： 如果是比昨早的开始时间早， 那么新的结束时间在开始时间之前就行
# 如果开始时间比最晚的开始时间晚，那么开始时间在最晚结束时间之后就行
# 否则要两边都考虑。

from bisect import bisect
class MyCalendar:
    def __init__(self):
        self.start_times = []
        self.end_times = []

    def book(self, start: int, end: int) -> bool:
        if not self.start_times:
            self.start_times.append(start)
            self.end_times.append(end)
            return True
        ind = bisect(self.start_times, start)  # 66 77
        # print(self.start_times, ind)

        if ind == 0:
            if end <= self.start_times[0]:  # 结束时间在开始时间之前就行
                self.start_times.insert(0, start)
                self.end_times.insert(0, end)
                return True
            else:
                return False

        if ind == len(self.start_times):  # 开始时间在上一个结束时间之后就行
            if start >= self.end_times[ind - 1]:
                self.start_times.insert(ind, start)
                self.end_times.insert(ind, end)
                return True
            else:
                return False

        if start >= self.end_times[ind - 1] and end <= self.start_times[ind]:  # 开始时间在上一个结束时间之后， 结束时间在下一个开始时间之前
            self.start_times.insert(ind, start)
            self.end_times.insert(ind, end)
            return True
        return False

# 这种方法比较巧妙， 用新的开始时间和所有当前的结束时间进行比较， binary search 找到位置，
# 如果位置是在最后的结束时间之外， 那么return true
# 否则我们要考虑当前的结束时间和下一个开始时间是否overlap
from bisect import bisect
class MyCalendar:

    def __init__(self):
        self.start_times = []
        self.end_times = []

    def book(self, start: int, end: int) -> bool:
        ind = bisect(self.end_times, start)

        if ind == len(self.end_times) or end <= self.start_times[ind]:
            self.start_times.insert(ind, start)
            self.end_times.insert(ind, end)
            return True
        else:
            return False


