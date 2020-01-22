# # 第一种方法是dfs， 和数小岛的方法一样。这种方法效率比较慢
# class Solution(object):
#     def countComponents(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: int
#         """
#         count = 0
#         visited = []
#         for edge in edges:
#             if edge[0] not in visited:
#                 count += 1
#                 self.dfs(edge[0], edges, visited)
#         isolated_node = n - len(visited)
#         return count + isolated_node
#
#     def dfs(self, start, edges, visited):
#         visited.append(start)
#         for eg in edges:
#             if start in eg:
#                 next_start = [x for x in eg if x != start][0]
#                 if next_start not in visited:
#                     self.dfs(next_start, edges, visited)

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
