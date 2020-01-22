# 这是一道典型用dfs的题目。
# 注意这个题目的test case 里面没有环的出现, 如果有环的话是有死循环的
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.res = []
        destination = len(graph) - 1
        curr_path = []
        self.dfs(0, destination, curr_path)
        return self.res

    def dfs(self, node, destination, curr_path):
        if node == destination:
            self.res.append(curr_path[:] + [node])
            return
        next_nodes = self.graph[node]
        for nd in next_nodes:
            self.dfs(nd, destination, curr_path + [node])

# 另一种类似的写法, 这种写法针对死循环， 就是要加入visited 这个cache， similar to nums of islands， the maze， etc
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.result = []
        visited = [0]
        self.dfs(graph, [0], 0, visited)
        return self.result

    def dfs(self, graph, current_path, node, visited):
        if node == len(graph) - 1:
            self.result.append(current_path[:])
            return
        next_nodes = graph[node]
        for nd in next_nodes:
            if nd not in visited:
                self.dfs(graph, current_path + [nd], nd)
                visited.append(nd)
        return []
