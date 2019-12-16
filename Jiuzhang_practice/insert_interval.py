# 这个方法是自己写的 复杂度O（nlgn）， 但是最后通过了测试。
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        find_st = False
        find_ed = False
        for i in range(len(intervals)):
            st, ed = intervals[i]
            # if current interval does not interact with the new interval
            if newInterval[0] > ed or newInterval[1] < st:
                result.append(intervals[i])

            # find the starting point
            else:
                if not find_st:
                    if newInterval[0] <= ed:
                        insert_start = max(newInterval[0], st)
                        find_st = True
                    else:
                        find_st = False
                if find_st:
                    if newInterval[1] >= st and newInterval[1] <= ed:
                        insert_end = ed
                        find_ed = True
                    elif newInterval[1] < st:
                        insert_end = newInterval[1]
                        find_ed = True
                    else:
                        find_ed = False

                if find_st and find_ed:
                    result.append([insert_start, insert_end])

        if not find_st:
            result.append(newInterval)
        if find_st and not find_ed:
            result.append([insert_start, newInterval[1]])
        return sorted(result, key=lambda x: x[0])

x = Solution()
print(x.insert([[1,5]], [2,3]))


class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)

        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
