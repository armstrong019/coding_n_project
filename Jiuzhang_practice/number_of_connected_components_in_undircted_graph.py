# 第一种方法是dfs， friend cycle, sentence similarity, 相似， 都是无向图的遍历。
# 建立一个graph， 和sentence similarity一致。dic = {node: connected nodes}
# 然后遍历node， 每一个新的node 都去找 和他连接的所有点， 所有点再进行深搜， 在这个过程记录被visited的点
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        dic = defaultdict(set)
        for i, j in edges:
            dic[i].add(j)
            dic[j].add(i)
        count = 0
        visited = set()
        for node in dic:
            if node not in visited:
                count += 1
                self.dfs(node, dic, visited)
        isolated_comp = n - len(visited)
        return count + isolated_comp

    def dfs(self, node, dic, visited):
        visited.add(node) # 什么时候加很重要， 一般一开始就加进去，否则会Miss掉第一个点
        for node2 in dic[node]:
            if node2 not in visited:
                self.dfs(node2, dic, visited)


# 第二种是union find 这种方法
class Solution(object):

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Use this array and set it to the offset.
        data = [i for i in range(n)] # 这个是parent list
        # Time complexity:
        """Using path compression with arbitrary linking roughly on 𝑚 operations has a complexity of roughly 𝑂((𝑚+𝑛)log(𝑛))
        """

        # Use find function to find out parent
        def find(data, i):
            if i != data[i]:
                data[i] = find(data, data[i])
            return data[i]

        # 如果i j 当前没有链接 则将i 的parent 赋成 j
        def union(data, i, j):
            pi = find(data, i)
            pj = find(data, j)
            if pi != pj:
                data[pi] = pj

        for i, j in edges:
            union(data, i, j)
        #print(data)
        # 链接好了之后还要顺一遍才可以， 以防有的vertex没有被照顾到。
        for i in range(n):
            x = find(data, i)
            #print(x,data)

        return len(set(data))

data =[[0,1],[1,2],[3,4]]
x=Solution()
x.countComponents(5, data)


parent = [0,-1,0,-1,-1,-1,-1,2,7]
def find(x):
    if x != parent[x]:
         parent[x] = find(parent[x])
    return parent[x]

print(find(8))
print(parent)


# 下面是我自己写的一个方法， 两个点同时找的过程。
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        count = 0

        for node1, node2 in edges:
            if node1 not in visited and node2 not in visited:
                count += 1
                self.dfs(node1, visited, edges, node2)
                self.dfs(node2, visited, edges, node1)
        isolated_node = n - len(visited) # 注意corner case， 没有出现过的点
        return count + isolated_node

    def dfs(self, node, visited, edges, non_node):
        visited.add(node) # 什么时候加很重要， 一般一开始就加进去，否则会Miss掉第一个点
        for i, j in edges:
            if i == node and j != non_node and j not in visited:
                self.dfs(j, visited, edges, i)
            if j == node and i != non_node and i not in visited:
                self.dfs(i, visited, edges, j)
