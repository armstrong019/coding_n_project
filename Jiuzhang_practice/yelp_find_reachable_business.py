#https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=563203&highlight=yelp%2BOA

import collections
class Business(object):
    def __init__(self, name, nearby):
        self.name = name
        self.nearby = nearby
a = Business("A", {})
b = Business("B", {})
c = Business("C", {})
d = Business("D", {})
e = Business("E", {})
f = Business("F", {})
g = Business("G", {})
h = Business("H", {})

a.nearby[b] = 5
a.nearby[c] = 4
a.nearby[d] = 3
b.nearby[f] = 3
a.nearby[f] = 15
f.nearby[g] = 20



def dfs(root, dist_left, result, visited):
    if root =={}:
        return
    if dist_left<0:
        return
    else:
        result.append(root.name)
    for nb in root.nearby.keys():
        if nb.name not in visited:
            visited.append(nb.name)
            dfs(nb, dist_left - root.nearby[nb], result, visited)

def find_reachable_business(root, dist):
    if dist ==0:
        return []
    result = []
    visited =['A']
    dfs(root, dist, result, visited)
    result.pop(0)
    return result

# 这个解法是网上给的 有错误
def find_reachable_business2(starting_business, distance):
    rb = []
    dis = {}
    dis[starting_business.name] = 0
    visited = set()
    q = collections.deque()
    q.append(starting_business)
    while q:
        root = q.popleft()
        visited.add(root.name)
        for bu in root.nearby:
            if bu.name not in visited:
                q.append(bu)
                if bu.name in dis:
                    newdis = dis[root.name] + root.nearby[bu]
                    if newdis < dis[bu.name]:
                        dis[bu.name] = newdis
                else:
                    dis[bu.name] = root.nearby[bu]
    print(dis)
    for name in dis:
        if dis[name] <= distance and name != starting_business.name:
            rb.append(name)
    return rb

# 这个解法是tree的解法
from collections import deque
def find_reachable_business3(root, dist):
    if dist == 0:
        return []
    res = []
    q = deque([(root,dist)])
    while q:
        node, current_dist = q.popleft()
        if current_dist>0:
            res.append(node.name)
            for nb in node.nearby.keys():
                q.append((nb, current_dist-node.nearby[nb]))
    res.pop(0)
    return res



# this one is dijstra algorithm，最短路径的变种
from collections import deque
def find_reachable_business4(root, r):
    if r == 0:
        return []
    q = deque([root])
    dist = {root.name: 0}
    while q:
        node = q.popleft()
        for nb in node.nearby.keys():
            arc_len = node.nearby[nb]
            if nb.name not in dist:
                dist[nb.name] = dist[node.name]+arc_len
                q.append(nb)
            else:
                if dist[node.name]+arc_len < dist[nb.name]:
                    dist[nb.name] = dist[node.name] + arc_len
                    q.append(nb)
                else:
                    continue
    print(dist)
    res = []
    for key in dist:
        if dist[key]<=r:
            res.append(key)
    res.pop(0)
    return res




rb = find_reachable_business4(a,17)
print(rb)





def find_reachable_business_2(root, r):
    dist = {root.name:0}
    q = deque([root])
    while q:
        current_node = q.popleft()
        for node in current_node.nearby:
            if node.name not in dist:
                dist[node.name] = dist[current_node.name] + current_node.nearby[node]
                q.append(node)
            else:
                current_dist = dist[current_node.name] + current_node.nearby[node]
                if current_dist < dist[node.name]:
                    dist[node.name] = current_dist
                    q.append(node)
    res =[]
    for name in dist:
        if name != root.name and dist[name] <=r:
            res.append(name)
    return res
rb = find_reachable_business4(a,17)
print(rb)




