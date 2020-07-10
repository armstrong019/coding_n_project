# 这道题基本就是逻辑execution，分类讨论就可以。 第一个类型是两者长度相等，第二个是两者长度差1。
# easy to understand solution。

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False
        if abs(len(s) - len(t)) >= 2:
            return False
        if len(s) == len(t):
            # 两个string长度相等的情况
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
                if count >= 2:
                    return False
            return count == 1 # 有且仅有一个不同
        if len(s) < len(t):
            return self.is_one_edit_distance(s, t)
        else:
            return self.is_one_edit_distance(t, s)

    def is_one_edit_distance(self, s, t):
        # 两个string长度相差1的情况。
        offset = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                offset = 1
            if s[i] != t[i + offset]:
                return False
        return True
