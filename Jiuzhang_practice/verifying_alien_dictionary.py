# 对词进行两两比较。
# 对于每两个词， 每个字符一一比较，
# 如果w1[j]对应的词语小于w2[j] 对应的位置，那么可以知道这两个词是符合要求的
# 如果w1[j]对应的词语大于w2[j] 对应的位置，那么可以知道这两个词是不符合要求的
# 如果一样 继续比较。
# 在最后要处理corner case， 就是比完之后 第一个词语里面还有字符， 那么可知道也是不符合的 （例如 aaac， aaa）
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for index, letter in enumerate(order):
            dic[letter] = index

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            is_valid = self.compare_two_words(w1, w2, dic)
            if not is_valid:
                return False
        return True

    def compare_two_words(self, w1, w2, dic):
        for j in range(min(len(w1), len(w2))):
            if dic[w1[j]] < dic[w2[j]]:
                return True
            elif dic[w1[j]] == dic[w2[j]]:
                pass
            else:
                return False
        if len(w1) > len(w2):
            return False
        return True
