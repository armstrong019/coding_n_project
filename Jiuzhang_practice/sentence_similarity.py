from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:

        similar = defaultdict(set)
        if len(words1) != len(words2):
            return False
        for w1, w2 in pairs:
            similar[w1].add(w2)
            similar[w2].add(w1)
        for i in range(len(words1)):
            if words1[i] != words2[i] and words2[i] not in similar[words1[i]]:
                return False
        return True
