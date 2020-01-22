# 这道题是看graph 是不是一个valid tree
# 首先充要条件的如果有n个vertexes， 那么他的edge 的个数必须是 n-1， 大于或者小于都不对
# 其次， 如果edge 正好有n-1个， 那么不成立的条件是 里面 必然有闭环 并且有至少有两个或以上的separated graphs
# 那么我其实只要搞定任何一个都解决了 像这类问题dfs 和bfs 都可以解决
# 具体做法是随便挑选一个node 然后深搜， 或者宽搜， 同时mark 那些被visited的点，如果宽搜完成还有点没有被visited 那么说明不是valid tree

from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Write your code here
        if len(edges) != n - 1:
            return False

        nbs = defaultdict(list)
        for i, j in edges:
            nbs[i].append(j)
            nbs[j].append(i)

        visited = [0]
        q = deque([0])
        while q:
            node = q.popleft()
            for nb in nbs[node]:
                if nb not in visited:
                    visited.append(node) # bfs 这种写法要特别注意更新visited的位置， 如果在for loop 之前更新会出问题，防止出错统一都在for loop 里面更新
                    q.append(nb)
        return len(visited)==n

# 为什么把visited放在for loop 之前会出错， 出什么错？
# 错误写法如下：
        visited = []
        q = deque([0])
        while q:
            node = q.popleft()
            visited.append(node)
            for nb in nbs[node]:
                if nb not in visited:
                    q.append(nb)
        return len(visited)==n
# 这样会造成什么问题： 有些点有可能会被visited 两次， why？
# 假如我有一个点x 和当前点c 相连 那么我会把x 放到q里面去。
# 我的visited 每次只多加一个， 但是我的q 每次可以多加多个，
# 这样会导致一个问题就是在q里面的一些点 如x 没来得及被visited，然而被pop 出来的其他点 也同时和x 点相连，（比如有环的情况）
# 那么x 则会被加到 q 里面多次。多次被处理。
# 所以统一来说， 我们需要控制 visited 和 q 的同步性， 要用上面的写法。
