class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            if needle == '': # 这个是特殊情况
                return 0
            l = len(needle)
            for i in range(len(haystack) - l + 1):
                if haystack[i:i + l] == needle:
                    return i
        else:
            return -1

# 自己写的， 超时了， 但是比较合理。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        if haystack == "" and needle != "":
            return -1
        if haystack != "" and needle == "":
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                is_valid = self.is_remaining_valid(haystack, needle, i)
                if is_valid:
                    return i
        return -1

    def is_remaining_valid(self, haystack, needle, i):
        p0 = i
        p1 = 0
        while True:
            if p1 > len(needle) - 1:
                return True
            elif p0 > len(haystack) - 1:
                return False
            elif haystack[p0] == needle[p1]:
                p0 += 1
                p1 += 1
            else:
                return False
