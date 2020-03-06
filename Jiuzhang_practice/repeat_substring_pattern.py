class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return True
        if len(s) == 1:
            return False
        length = len(s)//2
        for i in range(length):
            substring = s[:i+1]
            if substring[-1] == s[-1]:
                repeat_number = len(s)//len(substring)
                if len(s) % len(substring)==0:
                    reconstruct_s = ''
                    for j in range(repeat_number):
                        reconstruct_s+=substring
                    if reconstruct_s==s:
                        return True
        return False


