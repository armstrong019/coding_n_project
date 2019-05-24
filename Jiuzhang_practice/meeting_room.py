class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        if intervals == []:
            return True
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            interval = intervals[i]
            next_interval = intervals[i + 1]
            if interval.end > next_interval.start:
                return False

        return True