# 这道题看到后即想到用dfs去解。 这道题的精髓主要就是定义好状态变量，
# 这里面的状态变量有三个， current_path，左括号的剩余个数， 右边口号的剩余个数
# 我一开始的想法用permutation的方法 用list记录变量 【'（'，'（'，'）'，'）'】 每次从不同的index位置取出一个， 但是这样做的结果是会有很多重复，
# 并且状态变量的去重复很麻烦。

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs('', n, n, result)
        return result

    def dfs(self, current_path, unused_left, unused_right, result):
        if unused_left == 0 and unused_right == 0:
            result.append(current_path)
            return
        if unused_left > unused_right: # 如果左边剩下的比右边多， 那么说明解不可能。
            return
        if unused_left > 0:
            self.dfs(current_path + '(', unused_left - 1, unused_right, result)
        if unused_right > 0:
            self.dfs(current_path + ')', unused_left, unused_right - 1, result)


# 下面是我最初的想法， 这个写法的基础是permutation, 一开始是【（（（ ）））】， 然后每一次从中间选取一个， 然后把剩下的当做没有用到的记录下来。
# 这样会有很多重复的状态 我们用visited 记录状态signature = （current_path， unused）
from collections import Counter

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [] # result 必须要传进去。
        visited = []
        unused = ['(' for _ in range(n)] + [')' for _ in range(n)]
        self.dfs('', unused, result, visited) # 注意这个visited 是传进去的， 如果不传 也是可以的给个其实状态【】就可以了，
        return result

    def dfs(self, current_path, unused, result, visited):
        signiture = current_path + '0' + ''.join(unused) # 0 是为了区别两者
        if signiture in visited:
            return
        else:
            visited.append(signiture)

        if unused == []:
            if current_path not in result:
                result.append(current_path)
            return
        dic = Counter(unused)
        if dic['('] > dic[')']:
            return
        for i in range(len(unused)):
            self.dfs(current_path + unused[i], unused[:i] + unused[i + 1:], result, visited)

