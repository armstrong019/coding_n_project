# 这道题的关键点就是要防止 两个不同的pattern 对应同一个string 的情况 （多对一不可以）

class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        str0 = teststr.split(" ")
        word_dict = {}
        for ind, i in enumerate(pattern):
            if i in word_dict:
                if word_dict[i] != str0[ind]:
                    return False
            else:
                if str0[ind] in word_dict.values():
                    return False
                word_dict[i] = str0[ind]
        return True

# using hashtable
# two scenarios:
# 1. when we a pattern is already seen, need to make sure the pattern and word is matched
# 2. when a pattern is not seen, need to make sure the word have not appeared before
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# 两个
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic = {} # 记录pattern string matching
        dic2 = {} # 记录已经出现过的str
        List = str.split() # squeeze the space in between
        if len(pattern) != len(List):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if List[i] in dic2:
                    return False
                dic[pattern[i]] = List[i]
                dic2[List[i]] = pattern
            else:
                if dic[pattern[i]] != List[i]:
                    return False
        return True

# 这种 写法更直接 我们要验证从List1-List2 是一对一的 同时 List2-List1 也是一对一的
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic = {}
        List2 = [s for s in pattern]
        List1 = str.split()
        return self.validate_mapping(List1, List2) and self.validate_mapping(List2, List1)

    def validate_mapping(self, L1, L2):
        dic = {}
        if len(L1) != len(L2):
            return False
        for i in range(len(L1)):
            if L1[i] not in dic:
                dic[L1[i]] = L2[i]
            else:
                if dic[L1[i]] != L2[i]:
                    return False
        return True
