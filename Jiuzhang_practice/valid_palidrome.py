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
