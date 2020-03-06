# 简单题目 没什么难点。
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {}
        for i in range(len(list1)):
            dic1[list1[i]] = i
        res = []
        min_ind = sys.maxsize
        for j in range(len(list2)):
            if list2[j] in dic1:
                if j + dic1[list2[j]] < min_ind:
                    min_ind = j + dic1[list2[j]]
                    res = [list2[j]] #如果发现了一个新低， 那么override 之前的result
                elif j + dic1[list2[j]] == min_ind:
                    res.append(list2[j])
                else:
                    continue
        return res
