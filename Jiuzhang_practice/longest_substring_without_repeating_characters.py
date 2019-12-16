# 通向双指针的做法，p1 和i 之间夹的就是当前以i结尾的最长substring。 用hashtable记录当前的max substring 的位置
# 大致的想法是如果i 指向的字符已经出现过了， 那么将做指针update成出现位置的下一位， 这样可以保证当前位置没有重复
# 这道题目的写法和 longest substring without repeating characters 类似。

# 同向双指针的写法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        dic = {}
        left = 0  # p1 and p2 point to longest substring w/o repeating who ends at s[i]
        max_len = 1
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                ind = dic[s[i]]
                left = ind + 1
                for key in list(dic): # 注意删除的话 如果不加list系统会报错说dic size change inside loop
                    if dic[key] <= ind:
                        del dic[key]
                dic[s[i]] = i
            max_len = max(max_len, i - left + 1)
        return max_len


