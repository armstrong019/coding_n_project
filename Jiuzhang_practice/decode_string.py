# 这道题的题目意思不难 主要用stack，
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                # get letters,
                seq = ''
                while True:
                    if stack and stack[-1].isalpha():
                        seq = stack[-1]+seq
                        stack.pop()
                    else:
                        break
                stack.pop() # get rid of '['
                # get numbers
                digit = ''
                while True: #这里面avoid problem 是不着急pop stack 只有当情况满足才pop
                    if stack and stack[-1].isdigit():
                        digit = stack[-1]+digit
                        stack.pop()
                    else:
                        break
                number = int(digit) # get integer
                reconstructed_seq = number*seq
                stack.append(reconstructed_seq)
        return ''.join(stack)





