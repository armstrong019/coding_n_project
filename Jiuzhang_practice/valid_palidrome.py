class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        start = 0
        end = len(s)-1
        while start < end:
            while start<end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start<end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start<end and s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True


s =  ".,"
x = Solution()
print(x.isPalindrome(s))

# 第二遍写。Feb 24th
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        ps = 0
        pe = len(s) - 1
        while ps < pe:
            while ps < pe and not (s[ps].isalpha() or s[ps].isnumeric()):
                ps += 1
            while ps < pe and not (s[pe].isalpha() or s[pe].isnumeric()):
                pe -= 1
            if ps < pe: # 在这个点一定要再判断一次
                if s[ps].lower() != s[pe].lower():
                    return False
                else:
                    ps += 1
                    pe -= 1
            else:
                continue
        return True
