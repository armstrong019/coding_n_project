"""
Definition for a undirected graph node
deep copy of a graph
the graph may have loop, need to consider "remove duplicate"

"""

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        root = node
        nodes = self.getNodes(node)

        # copy nodes, store the old->new mapping information in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node):
        from collections import deque
        queue = deque([node])
        result = [node]

        while queue:
            nd = queue.popleft()
            result.append(nd)
            #print("result is ",[r.label for r in result])

            for nb in nd.neighbors:
                #print(nb.label)
                #print([q.label for q in queue])
                if nb not in result:
                    #print(nb.label,"has been put into",[r.label for r in result])
                    #result.append(nb)
                    queue.append(nb)
                    #print(nb)

        return result


a = UndirectedGraphNode(0)
b = UndirectedGraphNode(1)
c = UndirectedGraphNode(2)

a.neighbors.append(b)
a.neighbors.append(c)

b.neighbors.append(c)
c.neighbors.append(c)
c.neighbors.append(b)


x = Solution()
x.cloneGraph(a)
