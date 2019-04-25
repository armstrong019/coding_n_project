class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # write your code here
        if num is None:
            return []
        num.sort()
        self.result = []
        self.num = num
        self.dfs(0, target, [])
        return self.result

    def dfs(self, start, target, combination):
        if target == 0:
            if combination not in self.result:
                self.result.append(combination[:])
                return
        for i in range(start, len(self.num)):
            next_target = target - self.num[i]
            if next_target < 0:
                break
            else:
                combination.append(self.num[i])
                self.dfs(i + 1, next_target, combination) # 从下一个index开始搜索
                combination.pop()