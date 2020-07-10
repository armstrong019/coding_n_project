# 这道题目的又是属于time interval找 overlap的情况。
# 具体方法是two pointers。 选取两个intervals 然后判断是否有overlap。
# 然后移动 pointer， 如何移动呢， 那就要考虑选中两个intervals 谁先结束， 先结束的pointer往后移动一位。
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[1])
        p1, p2 = 0, 0
        while p1 <= len(slots1) - 1 and p2 <= len(slots2) - 1:
            start1 = slots1[p1][0]
            end1 = slots1[p1][1]
            start2 = slots2[p2][0]
            end2 = slots2[p2][1]
            overlap = self.has_overlap(start1, end1, start2, end2)
            if overlap != []:
                if overlap[1] - overlap[0] >= duration:
                    return [overlap[0], overlap[0] + duration]
            # 先结束的pointer 往后移动一位。
            if end1 < end2:
                p1 += 1
            elif end1 > end2:
                p2 += 1
            else:
                p1 += 1
                p2 += 1

        return []


    def has_overlap(self, start1, end1, start2, end2):
        if start1 <= start2:
            if end1 > start2:
                return [start2, min(end1, end2)]
            else:
                return []
        else:
            return self.has_overlap(start2, end2, start1, end1) # 注意这里面要加上return 否则返回None

# 这个可以算是标准答案了
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        if not slots1 or not slots2:
            return []

        i = j = 0

        while i < len(slots1) and j < len(slots2):
            if slots1[i][0] >= slots2[j][1]:
                j += 1
            elif slots2[j][0] >= slots1[i][1]:
                i += 1
            else:
                # 一定存在overlap
                start = max(slots1[i][0], slots2[j][0])
                end = min(slots1[i][1], slots2[j][1])
                if end - start >= duration:
                    return [start, start + duration]
                elif slots1[i][1] > slots2[j][1]:
                    j += 1
                else:
                    i += 1

        return []
