import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        List  = re.findall(r'\w+', paragraph.lower())
        word_list = {}
        for word in List:
            word = word.lower()
            if word not in word_list:
                word_list[word] = 1
            else:
                word_list[word] += 1
        freq = 0
        output = None
        for w in word_list:
            if w not in banned and word_list[w]>freq:
                output = w
                freq = word_list[w]
        return output

para = "Bob!"
banned = ["hit"]

result = Solution()
print(result.mostCommonWord(para, banned))

# 这到问题主要是熟悉re.findall 的用法. regular expression operation function



