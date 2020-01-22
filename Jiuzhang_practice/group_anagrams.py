from collections import defaultdict

# 以下是两种不同的写法。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            coder = [0 for _ in range(26)] # 将字符编码
            for i in s:
                ind = ord(i) - ord('a')
                coder[ind] += 1
            dic[tuple(coder)].append(s)  # 这里面tuple 不可以省略。 因为list不能作为hashtable的key

        res = []
        for k in dic.keys():
            res.append(dic[k])
        return res

# encode each word, store in dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            coder = ''.join(sorted(s)) #将字符sort之后是一个list，然后在join起来
            dic[coder].append(s)
        return dic.values()
