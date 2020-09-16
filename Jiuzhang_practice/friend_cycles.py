# 构建无向图然后dfs 遍历。 和number of connected components， sentience similarity2 一样。

from collections import defaultdict
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        dic = defaultdict(set)
        for i in range(len(M)):
            for j in range(len(M[i]))
                if M[i][j] != 0:
                    dic[i].add(j)
                    dic[j].add(i)
        count = 0
        visited = set()
        for node in dic:
            if node not in visited:
                count += 1
                self.dfs(node, visited, M, dic)
        return count

    def dfs(self, node, visited, M, dic):
        visited.add(node)
        for next_node in dic[node]:
            if next_node not in visited:
                self.dfs(next_node, visited, M, dic)

# 之前写的一种方法， 不建议考试写。不是很规范的写法。
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        visited = [0 for _ in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                count += 1
                self.dfs(i, visited, M)
        return count

    def dfs(self, i, visited, L):
        visited[i] = 1
        for j in range(len(L[i])):
            if i == j or L[i][j] == 0:
                continue
            else:
                if visited[j] == 0:
                    self.dfs(j, visited, L)
