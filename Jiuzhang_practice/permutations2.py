# 这道题目主要是去重， 提供几种方法。

#方法1 首先将nums 从小到大sort好， 然后去重
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort() # 之前首先要sort 一下
        self.result = []
        self.dfs([], nums)
        return self.result

    def dfs(self, current_perm, rest):
        if rest == []:
            self.result.append(current_perm[:])
        for i in range(len(rest)):
            if i == 0 or rest[i] != rest[i - 1]: #如果后一个数字和前一个一样， 那么这个分支就被剪掉了
                self.dfs(current_perm + [rest[i]], rest[:i] + rest[i + 1:])


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.result = []
        self.dfs([], nums)
        return self.result

    def dfs(self, current_perm, rest):
        if rest == []:
            if current_perm not in self.result: # 在结果处去重， 最简单也最慢
                self.result.append(current_perm[:])
        for i in range(len(rest)):
            self.dfs(current_perm + [rest[i]], rest[:i] + rest[i + 1:])

# checked on March 3rd
