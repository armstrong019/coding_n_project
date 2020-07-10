# 大致的想法是如果i 指向的字符已经出现过了， 那么将做指针update成出现位置的下一位， 这样可以保证当前位置没有重复

# 最简单的写法， 面试的时候写这个
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dic = {}
        max_len = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                ind = dic[s[i]]
                for key in list(dic):
                    if dic[key] <= ind:
                        del dic[key]
                dic[s[i]] = i
            max_len = max(max_len, len(dic))
        return max_len



# 另一种解法是不删除原来的数据， 只记录left 就可以
# 通向双指针的做法，p1 和i 之间夹的就是当前以i结尾的最长substring。 用hashtable记录当前的max substring 的位置

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dic = {}
        max_len = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                if dic[s[i]] >= left:
                    left = dic[s[i]] + 1
                dic[s[i]] = i
            max_len = max(max_len, i - left + 1)

        return max_len

