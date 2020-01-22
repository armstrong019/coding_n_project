# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

class Solution(object):
    def combinationSum(self, candidates, target):
        self.result = []
        self.candidates = sorted(candidates)
        self.target = target
        self.dfs([],0, target)
        return self.result

    def dfs(self, current_path, ind, residual):
        if residual == 0:
            self.result.append(current_path[:])
            return
        if residual < 0:
            return
        for i in range(ind, len(self.candidates)):
            self.dfs(current_path+[self.candidates[i]], i, residual-self.candidates[i])



# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination
# 每个数字只可以用一次
class Solution(object):
    def combinationSum2(self, candidates, target):
        self.result = []
        self.candidates = sorted(candidates)
        self.target = target
        self.dfs([], 0, target)
        return self.result

    def dfs(self, current_path, ind, residual):
        if residual == 0:
            self.result.append(current_path[:])
            return
        if residual < 0:
            return
        for i in range(ind, len(self.candidates)):
            self.dfs(current_path + [self.candidates[i]], i+1, residual - self.candidates[i])

# best time to buy and sell stock 1, 只可以买卖各一次， 买要在卖之前。
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        maxP = 0 # 记录global
        low = 100
        for p in prices:
            if p < low:
                low = p
                diff = 0
            else:
                diff = p-low
            if diff > maxP:
                maxP = diff
        return maxP

price =  [7,1,5,3,6,4]
x =  Solution()
print(x.maxProfit(price))


# longest common prefix
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if j>len(strs[0])-1 or strs[j][i]!= letter:
                    return res
            res += letter
        return res


# merge k sorted linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        heap = []
        head = ListNode(-1)
        dummy = head
        # push the head of all list into heap
        count = 0
        for list_head in lists:
            if list_head:
                heapq.heappush(heap, (list_head.val, count, list_head))
                count += 1

        while heap:
            val, _, list_head = heapq.heappop(heap)
            dummy.next = list_head
            if list_head.next:
                heapq.heappush(heap, (list_head.next.val, count, list_head.next))
                count += 1
            dummy = dummy.next
        return dummy.next


