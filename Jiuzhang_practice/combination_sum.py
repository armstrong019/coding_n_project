class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        if candidates == []:
            return []
        candidates.sort()
        self.candidates = candidates
        self.res = []
        self.dfs(0, [], target)
        return self.res

    def dfs(self, start, combination, target):
        if target == 0:
            if combination not in self.res:  #去重，比如[2,2,3]有可能是[2,3],[2,3]
                self.res.append(list(combination)) # deep copy, combination[:] works too.
                return
        for i in range(start, len(self.candidates)):
            if target - self.candidates[i] < 0:
                continue  # break works too
            else:
                combination.append(self.candidates[i])
                self.dfs(i, combination, target-self.candidates[i]) # the next time, starting index is i
                combination.pop() #backtrack
# 三个状态变量： start: 当前开始深搜的index
#              combination：当前已经记录的combination，是个list
#              target： 当前还差的值。


#另一种写法， 不用backtracking
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
            self.dfs(current_path+[self.candidates[i]],i, residual-self.candidates[i])
