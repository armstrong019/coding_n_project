from collections import defaultdict

# 以下是三种不同的写法。考试的时候写最后一种。 注意这里面是不去重的。 去重用set 就好
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

# revisited May 8th
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for i in range(len(strs)):
            encode  = [0 for _ in range(26)]
            for l in strs[i]:
                position = ord(l) -ord('a')
                encode[position] +=1
            encode = [str(k) for k in encode]  # ''.join(x) x must be a list of strings
            code = ''.join(encode)
            dic[code].append(strs[i])
        return list(dic.values())

# 一个简单的写法 sort string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())

