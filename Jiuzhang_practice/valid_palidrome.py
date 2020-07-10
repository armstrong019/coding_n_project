#two pointer的经典写法， 参考 3sum
# corner case 的验证： ".,"
# 这道题写起来要比较细心。考试的时候写第1种

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
            # 在结束上面的写法之后 either ps<pe or ps=pe
            if ps < pe: # 在这个点一定要再判断一次
                if s[ps].lower() != s[pe].lower():
                    return False
                else:
                    ps += 1
                    pe -= 1
            else:
                continue
        return True

# 第三遍写 Jun 28。 two pointer的经典写法， 参考 3sum
# corner case 的验证： ".,"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ps = 0
        pe = len(s) - 1
        while ps < pe:
            while not (s[ps].isalpha() or s[ps].isdigit()) and ps < pe: # 这里面一定要判断ps《pe
                ps += 1
            while not (s[pe].isalpha() or s[pe].isdigit()) and ps < pe:
                pe -= 1
            if s[ps].lower() == s[pe].lower():
                ps += 1
                pe -= 1
            else:
                return False
        return True

# 官方写法， 个人不喜欢容易出错
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        start = 0
        end = len(s)-1
        while start < end:
            while start<end and (not s[start].isalpha() or not s[start].isdigit()): # need to add ()
                start += 1
            while start<end and (not s[end].isalpha() or not s[end].isdigit()):
                end -= 1
            if start<end and s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True
