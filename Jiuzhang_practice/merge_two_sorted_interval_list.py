"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        # write your code here
        i = 0
        j = 0
        res = []
        while i <= len(list1) - 1 and j <= len(list2) - 1:
            if list1[i].start < list2[j].start:
                self.push_back(res, list1[i])
                i += 1
            else:
                self.push_back(res, list2[j])
                j += 1
        while i <= len(list1) - 1:
            self.push_back(res, list1[i])
            i += 1
        while j <= len(list2) - 1:
            self.push_back(res, list2[j])
            j += 1
        return res

    def push_back(self, res, interval):
        if not res:
            res.append(interval)
        else:
            if res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end) # merge intervals

# push back if the new interval start time > end time of the last interval in result, then append
# else merge intervals