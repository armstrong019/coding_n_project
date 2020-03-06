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

# 另一种写法， 不用backtrack
class Solution(object):
    def combinationSum2(self, candidates, target):
        self.result = []
        self.candidates = sorted(candidates)
        self.target = target
        self.dfs([],0, target)
        return self.result

    def dfs(self, current_path, ind, residual):
        if residual == 0:
            if current_path not in self.result:
                self.result.append(current_path[:])
            return
        for i in range(ind, len(self.candidates)):
            if residual-self.candidates[i]<0:
                break
            #把当前的数字放进去，然后下次考虑下一个数字
            self.dfs(current_path+[self.candidates[i]], i+1, residual-self.candidates[i])

# Jan/29
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        result = []
        self.dfs(0, [], candidates, target, result)
        return result

    def dfs(self, ind, path, candidates, target, result):
        if sum(path) == target:
            if path not in result:
                result.append(path[:])
            return
        # if sum(path)>target:
        #     return
        for i in range(ind, len(candidates)):
            if sum(path) + candidates[i] > target:
                break
            else:
                self.dfs(i + 1, path + [candidates[i]], candidates, target, result)
