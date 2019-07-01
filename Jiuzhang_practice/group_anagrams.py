from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            coder = [0 for _ in range(26)]
            for i in s:
                ind = ord(i) - ord('a')
                coder[ind] += 1
            dic[tuple(coder)].append(s)

        res = []
        for k in dic.keys():
            res.append(dic[k])
        return res

# encode each word, store in dictionary