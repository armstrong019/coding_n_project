class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # from left to right, remove extra ")"
        s = list(s)
        p = 0
        for i in range(len(s)):
            if s[i] == '(':
                p += 1
            elif s[i] == ')':
                if p == 0:
                    s[i] = ''
                else:
                    p -= 1
            else:
                pass

        # from right to left, remove extra "("
        q = 0
        for j in range(len(s) - 1, -1, -1):
            if s[j] == ')':
                q += 1
            elif s[j] == '(':
                if q == 0:
                    s[j] = ''
                else:
                    q -= 1
            else:
                pass

        return ''.join(s)
