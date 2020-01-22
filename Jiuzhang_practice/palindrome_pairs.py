# 此题目分类讨论，
# 1。 word 的inverse 也在例子里面
# 2。 word 的 prefix 是个palindrome 那么考察后面的那部分inverse 是否在list里面， 这里面注意 test case里面有空字符 "" 的例子，要考虑这种情况
# 3。 word 的 suffix 是个palindrome 那么考察前面的那部分inverse 是否在list里面
# 时间复杂度：O（nk），n： list里面词的个数 k：最长次的长度
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        hash_table = {x: i for i, x in enumerate(words)}
        for i, word in enumerate(words):
            # this is the first scenairo
            if word[::-1] in hash_table and hash_table[word[::-1]] != i:
                pairs.append([i, hash_table[word[::-1]]]) # 这里面注意不要重复加
            # below is the 2nd scenario
            valid_suffixs = self.find_valid_suffixs(word)
            for p in valid_suffixs:
                if p[::-1] in hash_table:
                    pairs.append([hash_table[p[::-1]], i])
            # below is the 3rd scenario
            valid_prefixs = self.find_valid_prefix(word)
            for q in valid_prefixs:
                if q[::-1] in hash_table:
                    pairs.append([i, hash_table[q[::-1]]])
        return pairs

    def find_valid_suffixs(self, word):
        valid_suffixs = []
        for i in range(len(word)): # 一开始我写的是range(len(word)-1)， 但是由于"" 是valid input， 所以要吧整个word 都考虑进去
            if word[:i + 1] == word[:i + 1][::-1]:
                valid_suffixs.append(word[i + 1:])
        return valid_suffixs

    def find_valid_prefix(self, word):
        valid_prefixs = []
        for i in range(len(word)):
            if word[i:] == word[i:][::-1]:
                valid_prefixs.append(word[:i])
        return valid_prefixs
