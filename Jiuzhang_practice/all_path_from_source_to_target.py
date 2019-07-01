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