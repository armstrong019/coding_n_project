# dfs method to solve this problem.
# (a,b) (b,c), (c,d)
# 这道题目的实质是一个无向图， 所以我们需要构造graph 使其从 A-D 走通 从D-A 也要走通。
# first step is to create a graph {a:b, b:a}--{a:b, b:(a,c), c:b}--{a:b, b:(a,c), c:(b,d), d:c}
# we need to find if a is connect to d in this graph, need to keep a set called visited to avoid loop.
# from a I go to b, from b go to c from c go to d.

from collections import defaultdict
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        dic = defaultdict(set)
        for w1, w2 in pairs:
            dic[w1].add(w2)
            dic[w2].add(w1)

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            else:
                if words1[i] not in dic or words2[i] not in dic:
                    return False
                visited = set()
                is_same_group = self.dfs(words1[i], words2[i], dic, visited)
                if not is_same_group:
                    return False
        return True

    def dfs(self, word, target, dic, visited):
        visited.add(word)
        if word == target:
            return True
        for w in dic[word]:
            if w not in visited:
                is_same_group = self.dfs(w, target, dic, visited)
                if is_same_group:
                    return True
        return False

