# 这道题的方法就是expand around the center， center 有两种， 第一种是每一个字母本身（N）个：组成的substring是奇数长度，
# 第二种是每两个字母的间隔（N-1）个， 组成的substring是偶数长度。

class Solution:
    def countSubstrings(self, s: str) -> int:
        # expand around the center method:
        count = 0
        for i in range(len(s)):
            j = 0
            while self.is_valid_index(i - j, i + j, s):
                if s[i - j] == s[i + j]:
                    count += 1
                    j += 1
                else:
                    break
        for k in range(len(s) - 1):
            q = 0
            while self.is_valid_index(k - q, k + q + 1, s):
                if s[k - q] == s[k + q + 1]:
                    count += 1
                    q += 1
                else:
                    break
        return count

    def is_valid_index(self, start, end, s):
        if start >= 0 and start <= len(s) - 1 and end >= 0 and end <= len(s) - 1:
            return True
        return False
