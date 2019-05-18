
#Meeting list: [[S1, S2], [S3, S4]...] --non-overlapping, New meeting: [[Sx, Sy]]. Write a function that returns boolean whether the meeting can be scheduled or not.

def find_conflits(meeting_list, new_meeting):
    if meeting_list == []:
        return True
    meeting_list.sort(key=lambda x: x[0])
    start = new_meeting[0]
    end = new_meeting[1]
    for i in range(len(meeting_list)):
        if start>=meeting_list[i][0] and start>=meeting_list[i][1]:
            continue
        if start< meeting_list[i][0]:
            if end <= meeting_list[i][0]:
                return True
        else:
            return False

    return True

meetings = [[2,3],[3,4]]
new_meeting = [2.5,3]

print(find_conflits(meetings, new_meeting))