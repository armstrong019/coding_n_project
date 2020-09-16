# # dfs 解法 这道题比较闹别扭的一点是result 怎么计算， 一种方法是把 result 当成内部变量 self.result 这个需要一个class
# 另外的方法是 改变dfs function的定义， 将当前的和的值进行输出


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total_result = 0
        for x in nestedList:
            val = self.helper(x, 1)
            total_result += val
        return total_result

    def helper(self, x, depth):
        if x.isInteger():
            return x.getInteger() * depth
        else:
            val = 0
            for k in x.getList():
                val += self.helper(k, depth + 1)
            return val


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.result = 0
        for x in nestedList:
            self.helper(x, 1)
        return self.result

    def helper(self, x, depth):
        if x.isInteger():
            self.result += x.getInteger() * depth
        else:
            for k in x.getList():
                self.helper(k, depth + 1)
