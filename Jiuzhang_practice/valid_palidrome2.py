#个人感觉比1 容易写，主要是想通方法
class Solution:
    def validPalindrome(self, s: str) -> bool:
        ps = 0
        pe = len(s) - 1
        while ps < pe:
            if s[ps] == s[pe]:
                ps += 1
                pe -= 1
            else:
                # 左边或者右边必须能走通一个
                left_plus_one = self.check_palindrome(s, ps + 1, pe) # 从ps+1 到 pe 必须是palindrome
                right_minus_one = self.check_palindrome(s, ps, pe - 1)
                if left_plus_one or right_minus_one:
                    return True
                else:
                    return False
        return True

    def check_palindrome(self, s, ps, pe):
        while ps < pe:
            if s[ps] == s[pe]:
                ps += 1
                pe -= 1
            else:
                return False
        return True
