# 用wiki 上的定义：
#1、将其发表的所有SCI论文按被引次数从高到低排序；
# 2、从前往后查找排序后的列表，直到某篇论文的序号大于该论文被引次数。
# 所得序号减一即为H指数。

class Solution:
    def hIndex(self, citations: List[int]) -> int:
            if not citations:
                return 0
            citations.sort(reverse=True)
            for i in range(len(citations)):
                if citations[i]<=i:
                    return i # wiki 上的定义用的是1，2，。 我们用的是0，1，2。。所以不用减少 一

            return len(citations)

# 自己总结的：sort array from large to small
# L[i]>=i+1 and L[i+1]<=i+1 then i+1 is the index
# but need to consider corner case
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        else:
            if min(citations) >= len(citations):
                return len(citations)  # index is n

            citations.sort(reverse=True)
            for i in range(len(citations) - 1):
                if citations[i] >= i + 1 and citations[i + 1] <= i + 1:
                    return i + 1 # index exist and index is not n
            return 0 # all 0 array
