from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = Counter(list(s))
        c2 = Counter(list(t))
        for k in c1:
            if k not in c2:
                return False
            else:
                if c1[k] != c2[k]:
                    return False
        return True

#这个主要是counter的用法 Counter 就是一个dictionary
